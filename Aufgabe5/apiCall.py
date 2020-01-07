import requests

lat = "52.51"
lng = "13.40"
dist = "25"
url = "https://openmensa.org/api/v2/canteens?near[lat]=%s&near[lng]=%s&near[dist]=%s" % (lat, lng, dist)
response = requests.request("GET", url)

canteenID = "30"
date = "2019-1-10"
url = "https://openmensa.org/api/v2/canteens/%s/days/%s/meals" % (canteenID, date)
response1 = requests.request("GET", url)


#Die Semantik wird durch ein json Schema in den Docs beschrieben (https://doc.openmensa.org/api/v2/)

print(response1.text.encode('utf8'))
print(response.text.encode('utf8'))

#1. Abfrage der Mensen einmalig und in DB speichern, da dies eine statische Information ist
#2. Abfrage der Gerichte eines Tages täglich, da immer nur ein Tga gleichzeitig abgefragt werden kann.