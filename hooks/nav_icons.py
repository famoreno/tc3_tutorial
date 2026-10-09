import re


ICON_PATTERN = re.compile(r"^:(fontawesome-solid|custom)-([a-z0-9-]+):\s*(.*)$")


def on_nav(nav, config, files):
    def apply_icons(items):
        for item in items:
            match = ICON_PATTERN.match(item.title)
            if match:
                icon_set, icon_name, item.title = match.groups()
                metadata = getattr(item, "meta", None)
                if metadata is None:
                    metadata = {}
                    item.meta = metadata
                if icon_set == "fontawesome-solid":
                    metadata["icon"] = f"fontawesome/solid/{icon_name}"
                else:
                    metadata["icon"] = f"custom/{icon_name}"

            apply_icons(getattr(item, "children", None) or [])

    apply_icons(nav.items)
    return nav
