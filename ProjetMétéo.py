import requests

def structure(nom_ville, code_pays):
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={nom_ville},{code_pays}&appid=c7430fbbf22309097858b612e7387e28&units=metric&lang=fr"
        )
        if response.status_code == 200:
            data = response.json()
            temp_actuelle = data["main"]["temp"]
            description = data["weather"][0]["description"]
            humidite = data["main"]["humidity"]
            pression = data["main"]["pressure"]
            return temp_actuelle, description, humidite, pression
        else:
            print("La ville recherchée est inexistante ou une autre erreur est survenue.")
            return None
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        return None

def affichage(nom_ville, code_pays, temp_actuelle, description, humidite, pression):
    print(f"Température : {temp_actuelle}°C")
    print(f"Description : {description}")
    print(f"Humidité : {humidite}%")
    print(f"Pression : {pression} hPa")

    ligne = (
        f"Ville : {nom_ville}\n"
        f"Code ISO du pays : {code_pays}\n"
        f"Température : {temp_actuelle}°C\n"
        f"Description : {description}\n"
        f"Humidité : {humidite}%\n"
        f"Pression : {pression} hPa\n"
    )
    return ligne

def ecriture(ligne):
    try:
        with open('RapportMétéo.txt', 'w', encoding='utf-8') as f:
            f.write(ligne)
        print("Le fichier a bien été créé !")
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier : {e}")

# Programme principal
nom_ville = input("Veuillez saisir le nom de la ville : ")
code_pays = input("Veuillez saisir le code ISO du pays : ")

resultat = structure(nom_ville, code_pays)

if resultat:
    temp_actuelle, description, humidite, pression = resultat
    ligne = affichage(nom_ville, code_pays, temp_actuelle, description, humidite, pression)
    ecriture(ligne)
