<pre><code class="language-python">import logging

import requests
from requests.exceptions import MissingSchema


def download_emoji(emoji: str) -&gt; bool:
    emoji_name = &quot;-&quot;.join(str(hex(ord(c)))[2:] for c in emoji)
    print(emoji_name)
    link = f&quot;https://web.telegram.org/a/img-apple-64/{emoji_name}.png&quot;
    headers = {
        &quot;User-Agent&quot;: (
            &quot;Mozilla/5.0 (Windows NT 10.0; Win64; x64) &quot;
            &quot;AppleWebKit/537.36 (KHTML, like Gecko) &quot;
            &quot;Chrome/120.0.0.0 Safari/537.36 Edg/113.0.1774.42&quot;
        )
    }
    try:
        with open(f&quot;emojis/{emoji_name}.png&quot;, &quot;wb&quot;) as file:
            file.write(requests.get(link, headers=headers).content)
        return True
    except MissingSchema as e:
        logging.error(f&quot;{e}&quot;)
    except ConnectionError:
        logging.error(&quot;404&quot;)
    return False
</code></pre>