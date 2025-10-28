from bs4 import BeautifulSoup
from bs4.replacer import SoupReplacer


def test_b_to_blockquote_multiple_places():
    html = "<div><b>hello</b><p><b>world</b></p></div>"
    r = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=r)
    assert str(soup) == (
        "<div><blockquote>hello</blockquote><p><blockquote>world</blockquote></p></div>"
    )


def test_noop_when_no_matching_tag():
    html = "<div><i>text</i><span>ok</span></div>"
    r = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=r)
    assert str(soup) == "<div><i>text</i><span>ok</span></div>"
