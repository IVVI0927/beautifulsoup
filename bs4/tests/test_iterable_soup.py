import unittest
from bs4 import BeautifulSoup, Tag, NavigableString, Comment, Doctype

class TestIterableSoup(unittest.TestCase):
    def _label(self, node):
        if isinstance(node, Tag):
            return node.name
        if isinstance(node, NavigableString):
            return f'"{str(node)}"'
        return type(node).__name__

    def test_depth_first_iteration_includes_all_nodes(self):
        soup = BeautifulSoup(
            "<root><section><p>one</p><p>two<b>bold</b></p></section><footer/></root>",
            "xml",
        )
        labels = [self._label(node) for node in soup]
        self.assertEqual(
            labels,
            [
                "[document]",
                "root",
                "section",
                "p",
                '"one"',
                "p",
                '"two"',
                "b",
                '"bold"',
                "footer",
            ],
        )

    def test_iteration_yields_special_nodes(self):
        html = "<!DOCTYPE html><html><body><!--comment--><p>hey</p></body></html>"
        soup = BeautifulSoup(html, "html.parser")
        nodes = list(soup)
        self.assertTrue(any(isinstance(node, Doctype) for node in nodes))
        self.assertTrue(any(isinstance(node, Comment) for node in nodes))
        self.assertTrue(any(isinstance(node, NavigableString) and str(node) == "hey" for node in nodes))

    def test_iter_returns_fresh_generator_each_time(self):
        soup = BeautifulSoup("<root><child/></root>", "xml")
        first = iter(soup)
        second = iter(soup)
        self.assertIsNot(first, second)
        self.assertEqual(next(first).name, "[document]")
        self.assertEqual([self._label(node) for node in second], ["[document]", "root", "child"])

    def test_iteration_reflects_mutations_midstream(self):
        soup = BeautifulSoup("<root><a/><b/></root>", "xml")
        iterator = iter(soup)
        next(iterator)  # [document]
        root = next(iterator)  # root
        new_tag = soup.new_tag("c")
        root.append(new_tag)
        remaining = [self._label(node) for node in iterator]
        self.assertIn("c", remaining)

    def test_large_tree_counts_expected_nodes(self):
        xml = "<root>" + "".join(f"<item>{i}</item>" for i in range(50)) + "</root>"
        soup = BeautifulSoup(xml, "xml")
        tag_count = sum(1 for node in soup if isinstance(node, Tag))
        # 50 items + root + [document]
        self.assertEqual(tag_count, 52)


if __name__ == "__main__":
    unittest.main()
