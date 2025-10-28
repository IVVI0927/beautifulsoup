import sys
from bs4 import BeautifulSoup, SoupStrainer

"""
Print all tags that have an 'id' attribute, parsing only elements that might have attributes.
"""

def main():
    if len(sys.argv) != 2:
        print("Usage: python task4.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Choose parser based on file extension
    is_xml = input_file.lower().endswith('.xml')
    parser = 'xml' if is_xml else 'html.parser'

    # SoupStrainer that filters tags having an 'id' attribute
    only_with_id = SoupStrainer(id=True)

    # Parse only tags that have id attributes
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f, parser, parse_only=only_with_id)

    # Find all tags that still have id attribute (redundant but clearer)
    tags_with_id = soup.find_all(id=True)

    print(f"Found {len(tags_with_id)} tags with id attribute:\n")

    for tag in tags_with_id:
        print(f"<{tag.name} id='{tag['id']}'>")

if __name__ == "__main__":
    main()