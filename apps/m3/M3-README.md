# Milestone-3

## What changed
- **M2:** Only rename a tag. Example: `<b>` → `<blockquote>`.
- **M3:** Let users pass small functions to change things **during parsing**:
  - `name_xformer(tag) -> str` (new tag name)
  - `attrs_xformer(tag) -> dict` (new attributes)
  - `xformer(tag) -> None` (edit the created tag)

## Why this is better
- Works for more cases (not only rename).
- Clean place to add rules (one small function per rule).
- Easy to test.

## How it works
Parser calls the replacer in this order:
1) `map_name()` → maybe change the tag name.
2) `map_attrs()` → maybe change attributes.
3) Create the tag.
4) `on_tag_created()` → last chance to edit the live tag.

## Files I changed
- `bs4/replacer.py` – new API with three functions.
- `bs4/__init__.py` – pass `replacer=` into the parser.
- `bs4/builder/_htmlparser.py` – call the three hooks during parsing.
- `bs4/tests/test_replacer_m3.py` – 6 tests (rename, add/modify/delete attrs, side‑effect, combine).
- `apps/m3/task7.py` – small app: add `class="test"` to all `<p>`.

## How to run
From the project root `beautifulsoup/`:
```bash
python -m unittest bs4.tests.test_replacer_m3
python -m apps.m3.task7 input.html output.html
```

## Example usages
Rename `<b>` to `<blockquote>`:
```python
SoupReplacer(name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name)
```
Delete all `class` attributes:
```python
SoupReplacer(xformer=lambda tag: tag.attrs.pop("class", None))
```
Add `role="note"` to every tag:
```python
SoupReplacer(attrs_xformer=lambda tag: {**tag.attrs, "role": "note"})
```

## My recommendation
I recommend keeping and extending the M3 functional design.  
Compared to the old M2 approach, the new API is more general and flexible, because it lets users define **small, composable transformation functions** instead of hard‑coding replacements.  

This design has several long‑term benefits:
- **Scalability:** It can support more complex HTML normalization tasks (e.g., cleaning attributes, adding accessibility metadata) without changing core code.
- **Maintainability:** Developers can test and reuse transformer functions independently.
- **Extensibility:** The same interface could easily integrate with other parsers (like `lxml` or `html5lib`) by just calling the same hooks.
- **Backward compatibility:** If needed, a simple wrapper can still support the old M2 pair‑mapping style.

In summary, M3’s design fits real engineering needs better. It balances simplicity and power, and makes BeautifulSoup more like a framework that users can extend safely during parsing.