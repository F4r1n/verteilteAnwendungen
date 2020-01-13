import xml.dom.minidom
import json

# work around since I had some issues with .json files
with open("json.txt", "r", encoding="utf-8") as jsonFile:
    data = json.load(jsonFile)
    for key in data.items():
        print(key)


dom = xml.dom.minidom.parse("s05635822_Pansegrau.xml")
pretty_xml_as_string = dom.toprettyxml()
print(pretty_xml_as_string)
