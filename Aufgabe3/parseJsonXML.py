import xml.dom.minidom
import json

with open("json.txt", "r", encoding="utf-8") as jsonFile:
    data = json.load(jsonFile)
    for key in data.items():
        print(key)


dom = xml.dom.minidom.parse("563579_JonasLiebermann.xml")
pretty_xml_as_string = dom.toprettyxml()
print(pretty_xml_as_string)