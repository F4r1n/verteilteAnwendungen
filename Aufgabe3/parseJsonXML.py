import xml.dom.minidom
import json

# work around since I had some issues with .json files
#edit: turns out it works with json files too
with open("./Aufgabe3/s0563822_Pansegrau.json", "r", encoding="utf-8") as jsonFile:
    data = json.load(jsonFile)
    for key in data.items():
        print(key)


dom = xml.dom.minidom.parse("./Aufgabe3/s0563822_Pansegrau.xml")
pretty_xml_as_string = dom.toprettyxml()
print(pretty_xml_as_string)
