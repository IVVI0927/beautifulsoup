import sys
from pathlib import Path
from typing import Iterable

from bs4 import BeautifulSoup, Tag, NavigableString, Comment, Doctype


def describe(node) -> str:
    if isinstance(node, Tag):
        return f"<{node.name}>"
    if isinstance(node, Comment):
        return f"<!--{node}-->"
    if isinstance(node, Doctype):
        return f"<!DOCTYPE {node}>"
    if isinstance(node, NavigableString):
        text = str(node).strip()
        return f'"{text}"' if text else '""'
    return node.__class__.__name__


def walk(nodes: Iterable) -> None:
    for idx, node in enumerate(nodes):
        print(f"{idx:04d}: {describe(node)}")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python -m apps.m4.walk_nodes <input_file>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"Input file not found: {input_path}")
        sys.exit(1)

    markup = input_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(markup, "html.parser")
    walk(soup)


if __name__ == "__main__":
    main()
