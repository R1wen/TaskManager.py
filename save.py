import json

def save(taches):
    with open("taches.json","w") as fichier:
        json.dump(taches, fichier, indent=2)