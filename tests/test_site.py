import json
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]


class AssetParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.assets = []
        self.external_assets = []
        self.csp = None
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"])
        if tag in {"link", "script"}:
            asset = values.get("href") or values.get("src")
            if asset and asset.startswith("./"):
                self.assets.append(asset)
            if (
                asset
                and urlparse(asset).scheme in {"http", "https"}
                and (
                    tag == "script"
                    or values.get("rel")
                    in {"stylesheet", "preconnect", "modulepreload"}
                )
            ):
                self.external_assets.append(asset)
        if tag == "meta" and values.get("http-equiv") == "Content-Security-Policy":
            self.csp = values.get("content")


class SiteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
        cls.app = (ROOT / "docs" / "app.mjs").read_text(encoding="utf-8")
        cls.parser = AssetParser()
        cls.parser.feed(cls.html)

    def test_local_assets_exist(self):
        for asset in self.parser.assets:
            path = urlparse(asset).path.removeprefix("./")
            self.assertTrue((ROOT / "docs" / path).is_file(), asset)

    def test_security_policy_and_dom_sinks(self):
        self.assertIsNotNone(self.parser.csp)
        self.assertIn("object-src 'none'", self.parser.csp)
        self.assertIn("script-src 'self'", self.parser.csp)
        self.assertEqual(self.parser.external_assets, [])
        for unsafe in ["innerHTML", "outerHTML", "insertAdjacentHTML", "eval(", "new Function"]:
            self.assertNotIn(unsafe, self.app)

    def test_required_interaction_landmarks_exist(self):
        self.assertTrue(
            {
                "catalog",
                "paper-dialog",
                "paper-list",
                "paper-search",
                "paper-template",
                "topic-list",
            }.issubset(self.parser.ids)
        )

    def test_manifest_is_valid(self):
        manifest = json.loads(
            (ROOT / "docs" / "site.webmanifest").read_text(encoding="utf-8")
        )
        self.assertEqual(manifest["start_url"], "./")
        self.assertEqual(manifest["display"], "standalone")
        self.assertTrue(manifest["icons"])

    def test_faint_text_meets_contrast_target(self):
        css = (ROOT / "docs" / "styles.css").read_text(encoding="utf-8")
        faint = re.search(r"--faint: (#[0-9a-f]{6})", css).group(1)

        self.assertGreaterEqual(contrast_ratio(faint, "#171d23"), 4.5)


def contrast_ratio(foreground, background):
    lighter, darker = sorted(
        [relative_luminance(foreground), relative_luminance(background)],
        reverse=True,
    )
    return (lighter + 0.05) / (darker + 0.05)


def relative_luminance(color):
    channels = [int(color[index : index + 2], 16) / 255 for index in (1, 3, 5)]
    linear = [
        channel / 12.92
        if channel <= 0.04045
        else ((channel + 0.055) / 1.055) ** 2.4
        for channel in channels
    ]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


if __name__ == "__main__":
    unittest.main()
