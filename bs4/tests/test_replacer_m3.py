import unittest
from bs4 import BeautifulSoup
from bs4.replacer import SoupReplacer

class TestSoupReplacerM3(unittest.TestCase):
    def test_name_xformer_renames_b_to_blockquote(self):
        html = "<p>Hello <b>How are you</b></p>"
        r = SoupReplacer(name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name)
        soup = BeautifulSoup(html, "html.parser", replacer=r)
        self.assertIsNotNone(soup.find("blockquote"))
        self.assertIsNone(soup.find("b"))

    def test_attrs_xformer_add_role(self):
        html = "<p>hello</p>"
        def add_role(shim):
            attrs = dict(shim.attrs)
            attrs.setdefault("role", "note")
            return attrs
        r = SoupReplacer(attrs_xformer=add_role)
        soup = BeautifulSoup(html, "html.parser", replacer=r)
        self.assertEqual(soup.p.get("role"), "note")

    def test_attrs_xformer_modify_class(self):
        html = '<p class="old"></p>'
        def modify_class(shim):
            attrs = dict(shim.attrs)
            classes = attrs.get("class", [])
            if isinstance(classes, str):
                classes = [classes]
            # replace 'old' with 'new'
            classes = ["new" if c == "old" else c for c in classes]
            if "new" not in classes:
                classes.append("new")
            attrs["class"] = classes
            return attrs
        r = SoupReplacer(attrs_xformer=modify_class)
        soup = BeautifulSoup(html, "html.parser", replacer=r)
        self.assertIn("new", soup.p.get("class", []))

    def test_attrs_xformer_delete_class(self):
        html = '<p class="c" data-x="1"></p>'
        def drop_class(shim):
            attrs = dict(shim.attrs)
            attrs.pop("class", None)
            return attrs
        r = SoupReplacer(attrs_xformer=drop_class)
        soup = BeautifulSoup(html, "html.parser", replacer=r)
        self.assertIsNone(soup.p.get("class"))
        self.assertEqual(soup.p.get("data-x"), "1")

    def test_xformer_side_effect_delete_class(self):
        html = '<p class="c">hi</p>'
        def remove_class(tag):
            if "class" in tag.attrs:
                del tag.attrs["class"]
        r = SoupReplacer(xformer=remove_class)
        soup = BeautifulSoup(html, "html.parser", replacer=r)
        self.assertIsNone(soup.p.get("class"))

    def test_combined_name_and_attrs(self):
        html = '<b class="c">x</b>'
        def force_blockquote(shim):
            return "blockquote" if shim.name == "b" else shim.name
        def add_role(shim):
            a = dict(shim.attrs)
            a["role"] = "note"
            return a
        r = SoupReplacer(name_xformer=force_blockquote, attrs_xformer=add_role)
        soup = BeautifulSoup(html, "html.parser", replacer=r)
        bb = soup.find("blockquote")
        self.assertIsNotNone(bb)
        self.assertEqual(bb.get("role"), "note")


if __name__ == "__main__":
    unittest.main()