.PHONY: collect render test

collect:
	python3 scripts/collect.py

render:
	python3 scripts/collect.py --render-only

test:
	python3 -m unittest discover -s tests -v
	node --test tests/site.test.mjs
