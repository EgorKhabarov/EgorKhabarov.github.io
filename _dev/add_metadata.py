# noinspection PyUnresolvedReferences
from _dev.utils import add_metadata, get_h_tags

path = (
    """

""".strip()
    .removeprefix("https://egorkhabarov.github.io/cheatsheet/?")
    .removeprefix("http://localhost:5000/cheatsheet/?")
    .removesuffix(".md")
    .removesuffix(".html")
    .replace("%20", " ")
)
add_metadata(
    path,
    {
        "color": "",
        "tags": [
            """


""",
            # *get_h_tags(path),
        ],
    },
)
