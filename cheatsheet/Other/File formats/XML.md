<h1>XML - eXtensible Markup Language</h1>
<p>Расширяемый язык разметки, который используется для хранения и обмена структурированными данными.
Он использует теги для определения структуры данных и может быть использован для хранения
всех видов данных, включая текст, изображения и мультимедиа.
<code>XML</code> широко используется в Интернете для хранения и обмена данными между веб-сервисами и приложениями.</p>
<pre><code class="language-xml">&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;note&gt;
&lt;to&gt;Tove&lt;/to&gt;
&lt;from&gt;Jani&lt;/from&gt;
&lt;heading&gt;Reminder&lt;/heading&gt;
&lt;body&gt;Don't forget me this weekend!&lt;/body&gt;
&lt;/note&gt;
</code></pre>
<pre><code class="language-python"># config = ET.Element(&quot;config&quot;)
# bot = ET.SubElement(config, &quot;BOT&quot;)
# ET.SubElement(bot, &quot;bot_name&quot;).text = &quot;&quot;
# ET.SubElement(bot, &quot;token&quot;).text = &quot;&quot;
# tree = ET.ElementTree(config)

import xml.etree.ElementTree as xml

def dict_to_xml(dct, root_node=None):
    if root_node is None:
        root_node = xml.Element(&quot;root&quot;)
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
        dct[root.tag].update((&quot;@&quot; + k, v) for k, v in root.attrib.items())
    if root.text:
        text = root.text.strip()
        if children or root.attrib:
            if text:
                dct[root.tag][&quot;#text&quot;] = text
        else:
            dct[root.tag] = text
    return dct

config = {&quot;BOT&quot;: {&quot;bot_name&quot;: &quot;&quot;, &quot;token&quot;: &quot;&quot;}}
config = dict_to_xml(config)
tree = xml.ElementTree(config)

with open(&quot;config.xml&quot;, &quot;wb&quot;) as file:
    tree.write(file, encoding=&quot;utf-8&quot;, xml_declaration=True)

with open(&quot;config.xml&quot;, &quot;r&quot;) as file:
    tree = xml.parse(file)

root = tree.getroot()
config = xml_to_dict(root)
print(config)
</code></pre>