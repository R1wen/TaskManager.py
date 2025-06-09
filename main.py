from addTask import addTasks
from deleteTask import deleteTask
from markedTask import markedTask
from save import save
import time
import json
import os

taches = []

nom_fichier = "taches.json"

if os.path.exists(nom_fichier):
    with open(nom_fichier, "r") as fichier:
        try:
            taches = json.load(fichier)
        except json.JSONDecodeError:
            print("Erreur lors du chargement des taches")
else:
    print("Fichier de sauvegarde introuvable")


def main():
    print("\n***BIENVENUE DANS LE NOTEBOOK RWN***")
    print("***CHOISSISEZ UNE OPTION***\n")
    options = [
        "1. Afficher les taches",
        "2. Ajouter une tache",
        "3. Marquer une tache comme terminée",
        "4. Supprimer une tache",
        "5. Quitter",
    ]
    for option in options:
        print(option)
    choix = int(input("\nVotre choix: "))

    match choix:
        case 1:
            print("***Voici la liste des taches***")
            for i in range(len(taches)):
                print(f"Tache {i+1}: {taches[i]}")
            time.sleep(5)
            main()

        case 2:
            addTasks(taches, main)

        case 3:
            for i in range(len(taches)):
                print(f"Tache {i+1}: {taches[i]}")

            numero = int(input("Quelle avez vous finie(chiffre) ?: "))
            markedTask(taches, numero, main)

        case 4:
            for i in range(len(taches)):
                print(f"Tache {i+1}: {taches[i]}")

            numero = int(input("Quelle tache supprimer(chiffre) ?: "))
            deleteTask(taches, numero, main)

        case 5:
            print("***A LA PROCHAINE***")
            return

        case _:
            print("Cette option n'existe pas")
            time.sleep(5)
            main()


if __name__ == "__main__":
    main()
