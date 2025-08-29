[Gradient text generator](https://www.birdflop.com/resources/rgb/)

| color name   |                                                                           | color | chat | hex code           | rgb           | motd      | decimal    |
|--------------|---------------------------------------------------------------------------|:-----:|:----:|--------------------|---------------|-----------|------------|
| dark_red     | <div style="background-color: #AA0000;width: 4.2em;height: 1.3em;"></div> | `&4`  | `§4` | `AA0000` `#AA0000` | `170 0 0`     | `\u00A74` | `11141120` |
| red          | <div style="background-color: #FE5555;width: 4.2em;height: 1.3em;"></div> | `&c`  | `§c` | `FF5555` `#FF5555` | `255 85 85`   | `\u00A7c` | `16733525` |
| gold         | <div style="background-color: #FFAA00;width: 4.2em;height: 1.3em;"></div> | `&6`  | `§6` | `FFAA00` `#FFAA00` | `255 170 0`   | `\u00A76` | `16755200` |
| yellow       | <div style="background-color: #FFFF55;width: 4.2em;height: 1.3em;"></div> | `&e`  | `§e` | `FFFF55` `#FFFF55` | `255 255 85`  | `\u00A7e` | `16777045` |
| green        | <div style="background-color: #55FF55;width: 4.2em;height: 1.3em;"></div> | `&a`  | `§a` | `55FF55` `#55FF55` | `0 170 0`     | `\u00A7a` | `5635925`  |
| dark_green   | <div style="background-color: #00AA00;width: 4.2em;height: 1.3em;"></div> | `&2`  | `§2` | `00AA00` `#00AA00` | `85 255 85`   | `\u00A72` | `43520`    |
| aqua         | <div style="background-color: #55FFFF;width: 4.2em;height: 1.3em;"></div> | `&b`  | `§b` | `55FFFF` `#55FFFF` | `85 255 255`  | `\u00A7b` | `5636095`  |
| dark_aqua    | <div style="background-color: #00AAAA;width: 4.2em;height: 1.3em;"></div> | `&3`  | `§3` | `00AAAA` `#00AAAA` | `0 170 170`   | `\u00A73` | `43690`    |
| blue         | <div style="background-color: #5555FF;width: 4.2em;height: 1.3em;"></div> | `&9`  | `§9` | `5555FF` `#5555FF` | `0 0 170`     | `\u00A79` | `5592575`  |
| dark_blue    | <div style="background-color: #0000AA;width: 4.2em;height: 1.3em;"></div> | `&1`  | `§1` | `0000AA` `#0000AA` | `85 85 255`   | `\u00A71` | `170`      |
| light_purple | <div style="background-color: #FF55FF;width: 4.2em;height: 1.3em;"></div> | `&d`  | `§d` | `FF55FF` `#FF55FF` | `255 85 255`  | `\u00A7d` | `16733695` |
| dark_purple  | <div style="background-color: #AA00AA;width: 4.2em;height: 1.3em;"></div> | `&5`  | `§5` | `AA00AA` `#AA00AA` | `170 0 170`   | `\u00A75` | `11141290` |
| white        | <div style="background-color: #FFFFFF;width: 4.2em;height: 1.3em;"></div> | `&f`  | `§f` | `FFFFFF` `#FFFFFF` | `255 255 255` | `\u00A7f` | `16777215` |
| gray         | <div style="background-color: #AAAAAA;width: 4.2em;height: 1.3em;"></div> | `&7`  | `§7` | `AAAAAA` `#AAAAAA` | `170 170 170` | `\u00A77` | `11184810` |
| dark_gray    | <div style="background-color: #555555;width: 4.2em;height: 1.3em;"></div> | `&8`  | `§8` | `555555` `#555555` | `85 85 85`    | `\u00A78` | `5592405`  |
| black        | <div style="background-color: #000000;width: 4.2em;height: 1.3em;"></div> | `&0`  | `§0` | `000000` `#000000` | `0 0 0`       | `\u00A70` | `0`        |

|            |                                                                  |
|------------|------------------------------------------------------------------|
| color name | string code, mostly used banner and items                        |
| chat       | start with the `§` character, used for chat, books and signs     |
| motd       | Used in the server config for setting message of the day         |
| hex code   | paint color and web css colors                                   |
| decimal    | used for nbt data tags, setting potion and leather armour colors |

| style         |                                                                                                                    | color | chat   | motd      |
|---------------|--------------------------------------------------------------------------------------------------------------------|-------|--------|-----------|
| Obfuscated    | <div style="font-family: monospace;user-select: none;max-height: 15px;max-width: 27px;" id="obfuscated">text</div> | `&k`  | `§k`   | `\u00A7k` |
| Bold          | <div style="font-family: monospace;font-weight: bolder;">text</div>                                                | `&l`  | `§l`   | `\u00A7l` |
| Strikethrough | <div style="font-family: monospace;text-decoration: line-through;">text</div>                                      | `&m`  | `§m`   | `\u00A7m` |
| Underline     | <div style="font-family: monospace;text-decoration: underline;">text</div>                                         | `&n`  | `§n`   | `\u00A7n` |
| Italic        | <div style="font-family: monospace;font-style: italic;">text</div>                                                 | `&o`  | `§o`   | `\u00A7o` |
| Reset         |                                                                                                                    | `&r`  | `§r`   | `\u00A7r` |

<svg style="cursor: pointer;" id="obfuscateButton" onclick="obfuscateButton.remove();const galacticChars = ['ᔑ', 'ʖ', 'ᓵ', '↸', 'ᒷ', '⎓', '⊣', '⍑', '╎', '⋮', 'ꖌ', 'ꖎ', 'ᒲ', 'リ', '𝙹', '!', '¡', 'ᑑ', '∷', '⨅', '҉', '҂', '☍', '⟊', '≋', '꘎', '⚍', '⧫', '⟁', '⸸',];const element = document.getElementById('obfuscated');const originalText = element.textContent;function getRandomGalacticChar() {return galacticChars[Math.floor(Math.random() * galacticChars.length)];}function obfuscateText(text) {return text.split('').map(() => getRandomGalacticChar()).join('');} setInterval(() => {element.textContent = obfuscateText(originalText);}, 150);" xmlns="http://www.w3.org/2000/svg" width="97" height="20" role="img" aria-label="Start animation"><title>Start animation</title><linearGradient id="s" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient><clipPath id="r"><rect width="97" height="20" rx="3" fill="#fff"/></clipPath><g clip-path="url(#r)"><rect width="0" height="20" fill="#1ad71e"/><rect x="0" width="97" height="20" fill="#1ad71e"/><rect width="97" height="20" fill="url(#s)"/></g><g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110"><text aria-hidden="true" x="485" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="870">Start animation</text><text x="485" y="140" transform="scale(.1)" fill="#fff" textLength="870">Start animation</text></g></svg>

![colors.png](Other/Minecraft/colors.png)

