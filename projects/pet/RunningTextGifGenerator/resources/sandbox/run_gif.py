import base64
import json
# from io import BytesIO


def running_text_gif_json(
    json_fragments: str,
    columns: int = 120,
    rows: int = 9,
    loop: bool = True,
):
    try:
        json_content: list[dict[str, str | bool | int]] = json.loads(json_fragments)
        assert isinstance(json_content, list), "not a list"
        assert 1 <= len(json_content) <= 20, "1 <= . <= 20"
        assert all(isinstance(i, dict) for i in json_content), "not all a dict"
        assert all(
            set(i.keys()) - {"text", "direction", "intro", "outro", "duration", "speed"} == set()
            for i in json_content
        ), "set"
        assert all(
            1 <= len(i["text"]) <= 150
            and (
                ("direction" in i and i["direction"] in ["left", "right", "up", "down", "none"]) or True
            )
            and (
                ("intro" in i and isinstance(i["intro"], bool)) or True
            )
            and (
                ("outro" in i and isinstance(i["outro"], bool)) or True
            )
            and (
                ("duration" in i and 20 <= i["duration"] <= 1000) or True
            )
            and (
                ("speed" in i and 1 <= i["speed"] <= 5) or True
            )
            for i in json_content
        ), "wrong arg"
    except (json.JSONDecodeError, AssertionError):
        raise

    # print(json_content)

    gif = GIF(columns, rows, loop=loop)  # noqa

    for content in json_content:
        gif.add_text_fragment(
            text=content["text"],
            font_path="/fonts/Monocraft.otf",
            # font_path="arial",
            **{"direction": content["direction"]} if content.get("direction") else {},
            **{"intro": content["intro"]} if content.get("intro") else {},
            **{"outro": content["outro"]} if content.get("outro") else {},
            **{"duration": content["duration"]} if content.get("duration") else {},
            **{"speed": content["speed"]} if content.get("speed") else {},
        )
    # file = BytesIO()
    gif.save("export.git")

    with open("export.git", "rb") as file:
        return "data:image/gif;base64," + base64.b64encode(file.read()).decode()
