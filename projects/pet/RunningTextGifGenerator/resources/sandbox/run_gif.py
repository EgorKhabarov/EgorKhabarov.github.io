import base64
import json
# from io import BytesIO
from js import send_err  # noqa


def running_text_gif_json(
    json_fragments: str,
    columns: int = 120,
    rows: int = 9,
    loop: bool = True,
):
    try:
        json_content: list[dict[str, str | bool | int]] = json.loads(json_fragments)
        assert isinstance(json_content, list), "JSON must be a list of fragments"
        assert 1 <= len(json_content) <= 20, "The number of fragments must be greater than 1 and less than 20"
        assert all(isinstance(i, dict) for i in json_content), "All fragments must be JSON dictionaries"
        assert all(
            set(i.keys()) - {"text", "direction", "intro", "outro", "duration", "speed"} == set()
            for i in json_content
        ), "Check the parameter names"
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
        ), "Check the parameter values"
    except (json.JSONDecodeError, AssertionError) as e:
        send_err(f"AssertionError: {e}\n")
        # raise
        return

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
