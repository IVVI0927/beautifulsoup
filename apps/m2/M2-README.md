# Milestone-2

### Part2: API Locations

| API / Class          | File         | Line | Notes |
|----------------------|--------------|------|-------|
| class BeautifulSoup  | bs4/__init__.py | 133  | BeautifulSoup entry; inherits Tag |
| find_all(...)        | bs4/element.py  | 2715 | Public search API used in M1/M2 |
| find_parent(...)     | bs4/element.py  | 992  | Parent navigation API |
| prettify(...)        | bs4/element.py  | 2601 | Pretty HTML output |
| replace_with(...)    | bs4/element.py  | 552  | Replace a tag with another node(s) |
| get(...)             | bs4/element.py  | 2160 | Returns the value of an attribute safely |
| get_text(...)        | bs4/element.py  | 524  | Extracts inner text from a tag |
| class SoupStrainer   | bs4/filter.py   | 313  | Used via BeautifulSoup(..., parse_only=...) |

### Part3: SoupReplacer

1.New API: bs4/replacer.py
2.Tests: bs4/tests/test_replacer.py
```bash
pytest bs4/tests/test_replacer.py -q
```
Expected: 2 passed
