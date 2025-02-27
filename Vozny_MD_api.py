import requests


def iegut_augstskolas(valsts, nosaukums=""):
    url = "http://universities.hipolabs.com/search"
    params = {"country": valsts, "name": nosaukums}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Kļūda: {response.status_code}")
        return []


latvija = iegut_augstskolas("Latvia")
print(f"Latvijā ir {len(latvija)} augstskolas")


print("Augstskolas Latvijā:")
for augstskola in latvija:
    print(augstskola['name'])


francija = iegut_augstskolas("France")
print(f"Francijā ir {len(francija)} augstskolas")


eu = sum(1 for augstskola in francija if augstskola['web_pages'][0].endswith('.eu'))
print(f"Francijā {eu / len(francija) * 100:.2f}% augstskolu ir mājas lapa ar .eu virsdomēnu")


paris = sum(1 for augstskola in francija if 'Paris' in augstskola['name'])
print(f"Francijā {paris} augstskolu nosaukumos ir 'Paris'")


school = sum(1 for augstskola in francija if 'School' in augstskola['name'])
print(f"Augstskolu skaits ar 'School' nosaukumā: {school}")


https = sum(1 for augstskola in francija if augstskola['web_pages'][0].startswith('https'))
print(f"Francijā {https / len(francija) * 100:.2f}% augstskolu mājas lapām ir https")


valstis = ["Latvia", "France", "Germany", "Italy", "Spain"] 
max_skaits = 0
max_valsts = ""

for valsts in valstis:
    augstskolas = iegut_augstskolas(valsts)
    if len(augstskolas) > max_skaits:
        max_skaits = len(augstskolas)
        max_valsts = valsts

print(f"Visvairāk augstskolu ir valstī {max_valsts} ar {max_skaits} augstskolām")