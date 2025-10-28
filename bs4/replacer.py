class SoupReplacer:
    """
    A very small API, similar in spirit to SoupStrainer, but for *changing* tag names
    during parsing. For Milestone-2 we keep it intentionally simple: replace all
    occurrences of `og_tag` with `alt_tag`.

    Example:
        replacer = SoupReplacer("b", "blockquote")
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    """

    def __init__(self, og_tag, alt_tag):
        self.og_tag = og_tag
        self.alt_tag = alt_tag

    def should_replace(self, name: str) -> bool:
        return name == self.og_tag

    def replace(self, name: str) -> str:
        return self.alt_tag if self.should_replace(name) else name