import sys
from bs4 import BeautifulSoup
from bs4.replacer import SoupReplacer

"""
Replace all <b> tags with <blockquote> tags during parsing using SoupReplacer.
"""

def main():
    if len(sys.argv) != 3:
        print("Usage: python task6_replacer.py <input_file> <output_file>")
        sys.exit(1)

    input_file, output_file = sys.argv[1], sys.argv[2]

    # Create a replacer that swaps <b> -> <blockquote>
    replacer = SoupReplacer("b", "blockquote")

    # Parse the file with BeautifulSoup using your new replacer API
    with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
        soup = BeautifulSoup(f, "html.parser", replacer=replacer)

    # Write the modified HTML to output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    print(f"✅ Replaced all <b> tags with <blockquote> tags.")
    print(f"Output written to: {output_file}")

if __name__ == "__main__":
    main()