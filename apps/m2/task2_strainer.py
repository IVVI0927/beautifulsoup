import sys
from bs4 import BeautifulSoup, SoupStrainer

"""
Print all <a> (hyperlink) tags, but parse ONLY <a> nodes to save time/memory
on large HTML files.
"""

# Entry point & basic arg check
if len(sys.argv) != 2:
    print("Usage: python task2.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

# Choose parser based on file extension
is_xml = input_file.lower().endswith('.xml')
parser = 'xml' if is_xml else 'html.parser'

# Build a SoupStrainer that only keeps <a> tags
only_a = SoupStrainer("a")

# Parse directly from the file handle to avoid loading the whole file into a big string
# (BeautifulSoup will still read it, but we avoid an extra full-size copy in memory.)
with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
    soup = BeautifulSoup(f, parser, parse_only=only_a)

# With SoupStrainer, the soup already contains only <a> nodes
links = soup.find_all('a')  # still fine to call find_all; it walks a much smaller tree now

print(f"Found {len(links)} hyperlinks:\n")
for link in links:
    href = link.get('href', 'No href attribute')
    text = link.get_text(strip=True) or 'No text'
    print(f"Text: '{text}' -> URL: {href}")
