from save import save
import time


def markedTask(taches, numero, retour):
    if numero > 0 and numero <= len(taches):
        tache = taches[numero - 1]
        tache["finie"] = True
        print("\nModification effectuée!")
        print("***Nouvelle Liste de Tache***")
        for i in range(len(taches)):
            print(f"Tache {i+1}: {taches[i]}")

        save(taches)
        time.sleep(5)
    else:
        print("\nNumero de tache invalide")
        time.sleep(5)
    retour()
