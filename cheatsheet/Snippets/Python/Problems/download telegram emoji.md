```python
import logging
from pathlib import Path

import requests
from requests.exceptions import MissingSchema


def download_emoji(emoji: str) -> bool:
    emoji_name = "-".join(str(hex(ord(c)))[2:] for c in emoji)
    print(emoji_name)
    link = f"https://web.telegram.org/a/img-apple-64/{emoji_name}.png"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36 Edg/113.0.1774.42"
        )
    }
    path = Path(f"emojis/{emoji_name}.png")
    path.parent.mkdir(exist_ok=True)
    try:
        with open(path, "wb") as file:
            file.write(requests.get(link, headers=headers).content)
        return True
    except MissingSchema as e:
        logging.error(f"{e}")
    except ConnectionError:
        logging.error("404")
    return False
```
