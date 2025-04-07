# UKOL 2
import requests
import json

def vyhledej_podle_ico ():
    ico = input ("Zadej IČO: ").strip()
    url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        obchodni_jmeno = data.get ("obchodniJmeno", "Nezmáne jméno.")
        adresa = data.get ("sidlo", {}).get ("textovaAdresa", "Nezmána adresa")
        print (f"\n{obchodni_jmeno}\n{adresa}\n")
    else:
        print ("Zadané IČO neexistuje, skús to později.")

def vyhledej_podle_jmena ():
    nazev = input ("Zadej nazev nebo jeho část: ").strip()
    url = " https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"
    
    headers = {"accept" : "application/json", "Content-Type" : "application/json"}

    dotaz = {"obchodniJmeno" : nazev}
    data = json.dumps(dotaz)
    data = data.encode ("utf-8")

    response = requests.post (url, headers=headers, data=data)

    if response.status_code == 200:
        vysledek = response.json()
        pocet = vysledek.get ("pocetCelkem", 0)
        subjekty = vysledek.get ("ekonomickeSubjekty", [])

        print (f"\nPočet subjektů: {pocet}")
        for subjekt in subjekty:
            jmeno = subjekt.get ("obchodniJmeno", "Nezmáne jméno")
            ico = subjekt.get ("ico", "Nezmáne IČO")
            print (f"{jmeno}, {ico}")

    else:
        print (f"Zkontroluj název nebo to zkus znova.")

def main ():
    print (" ---ARES---")
    print ("1 Vyhledej subjekt podle IČO.")
    print ("2 Vyhledej subjekt podle názvu.")
    volba = input ("Zadej volbu 1 nebo 2: ").strip ()

    if volba == "1":
        vyhledej_podle_ico()
    elif volba == "2":
        vyhledej_podle_jmena()
    else:
        print ("Neplatná volba")

if __name__ == "__main__":
    main()