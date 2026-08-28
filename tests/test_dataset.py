import csv
import json
import unittest
from pathlib import Path

from scripts.collect import paper_sort_key


ROOT = Path(__file__).resolve().parents[1]


class DatasetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(
            (ROOT / "data" / "papers.json").read_text(encoding="utf-8")
        )
        cls.papers = cls.payload["papers"]

    def test_dataset_version_and_required_fields(self):
        required = {
            "id",
            "version",
            "title",
            "authors",
            "abstract",
            "categories",
            "primary_category",
            "published",
            "updated",
            "url",
            "pdf_url",
            "doi",
            "journal_ref",
            "comment",
            "topics",
            "relevance_score",
        }

        self.assertEqual(self.payload["schema_version"], 1)
        self.assertGreater(len(self.papers), 0)
        for paper in self.papers:
            self.assertEqual(set(paper), required)
            self.assertTrue(paper["authors"])
            self.assertTrue(paper["categories"])
            self.assertTrue(paper["topics"])
            self.assertGreaterEqual(paper["relevance_score"], 4)

    def test_ids_are_unique_and_records_are_sorted(self):
        ids = [paper["id"] for paper in self.papers]

        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(
            self.papers,
            sorted(self.papers, key=paper_sort_key, reverse=True),
        )

    def test_csv_matches_json_order(self):
        with (ROOT / "data" / "papers.csv").open(encoding="utf-8", newline="") as file:
            rows = list(csv.DictReader(file))

        self.assertEqual(
            [row["id"] for row in rows],
            [paper["id"] for paper in self.papers],
        )


if __name__ == "__main__":
    unittest.main()
