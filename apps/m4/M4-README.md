# Milestone-4

## Iterable soup
- Added `BeautifulSoup.__iter__`, which performs an explicit depth-first traversal using a small stack so we never materialize the full node list.
- Iteration yields every node (`[document]`, tags, strings, comments, doctypes, etc.) in document order, enabling `for node in soup` streaming scenarios.
- Because we reuse the live tree structure, mutations that occur mid-iteration are observed immediately—useful for progressive transformations.

## Tests
- New suite: `python -m unittest bs4.tests.test_iterable_soup`
  - Covers preorder ordering, inclusion of special node types, iterator freshness, mid-iteration mutations, and large-tree counts.
- Existing Milestone 3 tests still pass: `python -m unittest bs4.tests.test_replacer_m3`

## Sample app
- `python -m apps.m4.walk_nodes input.html`
  - Streams every node with its index and a short description, showcasing the new iterable behavior without building auxiliary structures.

## Recommendation
- Keeping `BeautifulSoup` iterable lowers the barrier for clients who need single-pass analyses (linting, accessibility audits, metrics) on arbitrarily large documents.
- The stack-based approach keeps memory proportional to tree depth, meeting the “no intermediate list” constraint while remaining easy to reason about and test.
