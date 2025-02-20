import requests

def atkritumu_skirosanas_punkti():
    url = "https://data.gov.lv/dati/lv/api/3/action/datastore_search?resource_id=92ac6e57-c5a5-444e-aaca-ae90c120cc3d"
    
    try:
        atbilde = requests.get(url, timeout=10)
        atbilde.raise_for_status()
        dati = atbilde.json()
        
        if not dati.get("result") or not dati["result"].get("records"):
            print("API atbildēja ar tukšu datu kopu.")
            return
        
        ieraksti = dati["result"]["records"]
        
        print("Atkritumu šķirošanas punkti, kuros var nodot baterijas, riepas vai metālu:")
        
        for ieraksts in ieraksti:
            adrese = ieraksts.get("Adrese", "Nav norādīts")
            novads = ieraksts.get("Municipalitāte", "Nav norādīts")
            var_nodot = {
                "Baterijas un akumulatori": ieraksts.get("8 : Baterijas un akumulatori") == "x",
                "Nolietotās riepas": ieraksts.get("10 : Nolietotās riepas") == "x",
                "Metāls": ieraksts.get("3 : Metāls") == "x"
            }
            
            if any(var_nodot.values()):
                print(f"Adrese: {adrese}, Novads: {novads}")
                for atkritumu_veids, pieejams in var_nodot.items():
                    if pieejams:
                        print(f"  - Pieņem: {atkritumu_veids}")
                print("-")
                
    except requests.exceptions.RequestException as kluda:
        print(f"Kļūda, piekļūstot API: {kluda}")

if __name__ == "__main__":
    atkritumu_skirosanas_punkti()
