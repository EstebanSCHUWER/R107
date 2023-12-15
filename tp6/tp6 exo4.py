import random

def generer(nbr, vmin, vmax):
    return [random.randint(vmin, vmax) for _ in range(nbr)]

def combienInferieur(table, vseuil):
    return sum(1 for valeur in table if valeur < vseuil)

def programme_interactif():
    nb = int(input("Entrez le nombre de valeurs à générer : "))

    vmin = int(input("Entrez la valeur minimale : "))
    vmax = int(input("Entrez la valeur maximale : "))

    tab = generer(nb, vmin, vmax)
    tab.sort()

    print("Tableau généré :", tab)

    choix_seuil = input("Voulez-vous préciser le seuil ? (Oui/O, Non/N) : ").lower()

    if choix_seuil == 'oui' or choix_seuil == 'o':
        seuil = int(input("Entrez le seuil : "))
    else:
        seuil = 30

    total = combienInferieur(tab, seuil)
    print(f"Il y en a {total} inférieurs à {seuil}")

programme_interactif()
