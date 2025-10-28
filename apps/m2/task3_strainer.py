import sys
from bs4 import BeautifulSoup
from collections import Counter

def main():
    if len(sys.argv) != 2:
        print("Usage: python task3.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Read and parse the file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if input_file.lower().endswith('.xml'):
        soup = BeautifulSoup(content, 'xml')
    else:
        soup = BeautifulSoup(content, 'html.parser')   
            
    # Get all tags
    all_tags = [tag.name for tag in soup.find_all()]
    
    # Count occurrences
    tag_counts = Counter(all_tags)
    
    print(f"Total tags found: {len(all_tags)}\n")
    print("Unique tags and their counts:")
    
    for tag, count in sorted(tag_counts.items()):
        print(f"  <{tag}>: {count}")

if __name__ == "__main__":
    main()