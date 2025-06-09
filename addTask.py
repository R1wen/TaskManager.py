from save import save


def addTasks(taches, retour):
    continuer = "y"
    while continuer.lower() == "y":
        titre_tache = input("Entrez la tache à enregistrer: ").strip()
        if titre_tache:
            tache = {"titre": titre_tache, "finie": False}
            taches.append(tache)
            print("Tâche ajoutée !")
            save(taches)
        else:
            print("Le titre de la tâche ne peut pas être vide.")
        continuer = input("Voulez-vous ajouter une autre tâche ? (y/n): ")
    retour()
