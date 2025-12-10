# XML - eXtensible Markup Language

Расширяемый язык разметки, который используется для хранения и обмена структурированными данными
Он использует теги для определения структуры данных и может быть использован для хранения всех видов данных, включая текст, изображения и мультимедиа
`XML` широко используется в Интернете для хранения и обмена данными между веб-сервисами и приложениями

```xml
<?xml version="1.0" encoding="UTF-8"?>
<note>
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
</note>
```

```python
# config = ET.Element("config")
# bot = ET.SubElement(config, "BOT")
# ET.SubElement(bot, "bot_name").text = ""
# ET.SubElement(bot, "token").text = ""
# tree = ET.ElementTree(config)

import xml.etree.ElementTree as xml


def dict_to_xml(dct, root_node=None):
    if root_node is None:
        root_node = xml.Element("root")
    for key, value in dct.items():
        node = xml.SubElement(root_node, key)
        if isinstance(value, dict):
            dict_to_xml(value, node)
        else:
            node.text = str(value)
    return root_node


def xml_to_dict(root):
    from collections import defaultdict
    dct = {root.tag: {} if root.attrib else None}
    children = list(root)
    if children:
        dd = defaultdict(list)
        for dc in map(xml_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        dct = {root.tag: {k: v[0] if len(v) == 1 else v for k, v in dd.items()}}
    if root.attrib:
        dct[root.tag].update(("@" + k, v) for k, v in root.attrib.items())
    if root.text:
        text = root.text.strip()
        if children or root.attrib:
            if text:
                dct[root.tag]["#text"] = text
        else:
            dct[root.tag] = text
    return dct


config = {
    "config": {
        "name": "John Smith",
        "age": 30,
        "city": "New York",
    },
}
config = dict_to_xml(config)
tree = xml.ElementTree(config)


with open("config.xml", "wb") as file:
    tree.write(file, encoding="utf-8", xml_declaration=True)


with open("config.xml", "r") as file:
    tree = xml.parse(file)


root = tree.getroot()
config = xml_to_dict(root)
print(config)
```
