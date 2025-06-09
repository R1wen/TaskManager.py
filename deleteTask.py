from save import save
import time


def deleteTask(taches, numero, retour):
    if numero > 0 and numero <= len(taches):
        del taches[numero - 1]
        print("\nTache supprimée avec succès")
        print("***Nouvelle Liste de Tache***")
        for i in range(len(taches)):
            print(f"Tache {i+1}: {taches[i]}")

        save(taches)
        time.sleep(5)
    else:
        print("\nNumero de tache invalide")
        time.sleep(5)
    retour()
