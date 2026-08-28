## Summary

Describe the collector, query, taxonomy, documentation, or test change.

## Selection impact

Describe expected false-positive, false-negative, or reclassification effects.
Use "None" for changes that do not affect paper selection.

## Verification

- [ ] `python3 -m unittest discover -s tests -v`
- [ ] `python3 scripts/collect.py --render-only`
- [ ] Generated files are included and `git diff` is expected
