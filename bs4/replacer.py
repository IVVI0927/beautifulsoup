class SoupReplacer:
    """
    During parsing transforms. Two usage styles:
      (A) Pair mode (M2): SoupReplacer("b", "blockquote")
      (B) Transformer mode (M3):
          SoupReplacer(
              name_xformer=lambda tag: ... or tag.name,
              attrs_xformer=lambda tag: ... or tag.attrs,
              xformer=lambda tag: side effects on tag; returns None
          )
    """
    __slots__ = ("og", "alt", "name_xformer", "attrs_xformer", "xformer")

    # M2 pair-mode still supported; M3 adds optional transformers.
    def __init__(self, og_tag=None, alt_tag=None,
                 name_xformer=None, attrs_xformer=None, xformer=None):
        self.og = (og_tag or "").lower() if og_tag else None
        self.alt = (alt_tag or "").lower() if alt_tag else None
        self.name_xformer = name_xformer
        self.attrs_xformer = attrs_xformer
        self.xformer = xformer

    # -------- hooks used by the builder during parsing --------
    # 1) before tag object is created: transform name & attrs
    def map_name(self, name: str, attrs: dict) -> str:
        # transformer mode takes precedence
        if self.name_xformer is not None:
            # In transformer mode we pass a lightweight proxy-like view
            # but name_xformer expects a tag-like object; we relax and pass a shim
            class _Shim:
                def __init__(self, nm, at):
                    self.name, self.attrs = nm, at
            nm = self.name_xformer(_Shim(name, attrs))
            return nm if nm else name
        # fallback to M2 pair-mode
        if self.og and name and name.lower() == self.og and self.alt:
            return self.alt
        return name

    def map_attrs(self, name: str, attrs: dict) -> dict:
        if self.attrs_xformer is not None:
            class _Shim:
                def __init__(self, nm, at):
                    self.name, self.attrs = nm, dict(at)
            new_attrs = self.attrs_xformer(_Shim(name, dict(attrs)))
            return new_attrs if isinstance(new_attrs, dict) else attrs
        return attrs

    # 2) after tag object is created: allow side-effect xformer(tag)
    def on_tag_created(self, tag) -> None:
        if self.xformer is not None and tag is not None:
            self.xformer(tag)