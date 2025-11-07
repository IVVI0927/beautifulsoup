import sys
from bs4 import BeautifulSoup
from bs4.replacer import SoupReplacer

def add_class_to_p(tag):
    """Side-effect transformer: add or replace class='test' for <p> tags."""
    if tag.name == "p":
        tag["class"] = "test"


def main():
    if len(sys.argv) != 3:
        print("Usage: python task7.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Read the file
    with open(input_file, "r", encoding="utf-8") as f:
        html = f.read()

    # Create a replacer that modifies tags during parsing
    replacer = SoupReplacer(xformer=add_class_to_p)

    # Parse the document using our new SoupReplacer API
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    # Write the modified HTML
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    print(f"Transformation complete. Output written to {output_file}")


if __name__ == "__main__":
    main()