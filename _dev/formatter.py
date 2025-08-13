import re
from pathlib import Path


cheatsheet_path = (
    """

""".strip()
    .removeprefix("https://egorkhabarov.github.io/cheatsheet/?")
    .removeprefix("http://localhost:5000/cheatsheet/?")
    .removeprefix("cheatsheet/")
    .removesuffix(".md")
    .removesuffix(".html")
    .replace("%20", " ")
)
path = Path("../cheatsheet/", f"{cheatsheet_path}.md")
text = path.read_text(encoding="UTF-8")

end_space_regex = re.compile(r"(?m) +$")
end_dot_regex = re.compile(r"(?m)\.$")
header_regex = re.compile(r"(#+|\*|\d+\.) \*\*(?:\d\.){0,2} ?([^\n]+)\*\*")
hr_regex = re.compile(r"\n\n---")
quotes_regex = re.compile(r"'[^'\n]*?'")
# re.compile(r"(?<=# )[^а-яa-z`]+")


def table_bold_func(s: str) -> str:
    return re.sub(
        r"\|([^\n]*)\|(\n\|[-:| ]+\|)",
        lambda m: f"|{re.sub(r"\*\*([^|]*?)\*\*", r"\1    ", m[1])}|{m[2]}",
        s,
    )


text = end_space_regex.sub("", text)
text = end_dot_regex.sub("", text)
text = header_regex.sub(r"\1 \2", text)
text = hr_regex.sub("", text)
text = table_bold_func(text)

# print(text)
path.write_text(text, encoding="UTF-8")
