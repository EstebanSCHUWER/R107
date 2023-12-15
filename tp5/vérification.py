import os.path
from datetime import datetime

def afficher_info_fichier(fichier):
    if os.path.isfile(fichier):
        taille = os.path.getsize(fichier)

        date_modification_timestamp = os.path.getmtime(fichier)
        date_modification = datetime.fromtimestamp(date_modification_timestamp)

        print(f"Le fichier {fichier} existe.")
        print(f"Taille du fichier : {taille} octets.")
        print(f"Dernière modification : {date_modification}")
    else:
        print(f"Le fichier {fichier} n'existe pas.")

fichier1 = input("Entrez le nom du premier fichier : ")
fichier2 = input("Entrez le nom du deuxième fichier : ")

afficher_info_fichier(fichier1)
print()
afficher_info_fichier(fichier2)
