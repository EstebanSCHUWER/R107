def formater_nom_prenom(nom, prenom):
    nom_formate = nom.upper()
    prenom_formate = prenom.capitalize()
    return f"{prenom_formate} {nom_formate}"

nom1 = input("Entrez le nom de la première personne : ")
prenom1 = input("Entrez le prénom de la première personne : ")

nom2 = input("Entrez le nom de la deuxième personne : ")
prenom2 = input("Entrez le prénom de la deuxième personne : ")

personne1 = formater_nom_prenom(nom1, prenom1)
personne2 = formater_nom_prenom(nom2, prenom2)

if personne1 < personne2:
    print(personne1)
    print(personne2)
else:
    print(personne2)
    print(personne1)
