def calculer_taille(chaine):
    taille = 0
    for caractere in chaine:
        if caractere == '\0':
            break
        taille += 1
    return taille

def calculer_pourcentage_voyelles(chaine):
    voyelles = "aeiouyAEIOUY"
    nombre_voyelles = sum(1 for caractere in chaine if caractere in voyelles)
    taille = calculer_taille(chaine)
    if taille > 0:
        pourcentage = (nombre_voyelles / taille) * 100
        return pourcentage
    else:
        return 0

def est_sous_chaine(chaine, sous_chaine):
    taille_chaine = calculer_taille(chaine)
    taille_sous_chaine = calculer_taille(sous_chaine)

    for i in range(taille_chaine - taille_sous_chaine + 1):
        if chaine[i:i + taille_sous_chaine] == sous_chaine:
            return True, i

    return False, -1

def compter_occurrences(chaine, sous_chaine):
    taille_chaine = calculer_taille(chaine)
    taille_sous_chaine = calculer_taille(sous_chaine)
    occurrences = 0

    for i in range(taille_chaine - taille_sous_chaine + 1):
        if chaine[i:i + taille_sous_chaine] == sous_chaine:
            occurrences += 1

    return occurrences

chaine_a_traiter = input("Entrez une chaîne de caractères : ")

taille_chaine = calculer_taille(chaine_a_traiter)
print(f"La taille de la chaîne est : {taille_chaine} caractères.")

pourcentage_voyelles = calculer_pourcentage_voyelles(chaine_a_traiter)
print(f"Le pourcentage de voyelles dans la chaîne est : {pourcentage_voyelles:.2f}%.")

sous_chaine = 'wagon'
est_sous_chaine, debut_occurrence = est_sous_chaine(chaine_a_traiter, sous_chaine)

if est_sous_chaine:
    print(f"'{sous_chaine}' est une sous-chaîne, et la première occurrence commence à la position {debut_occurrence}.")
    nombre_occurrences = compter_occurrences(chaine_a_traiter, sous_chaine)
    print(f"Il y a {nombre_occurrences} occurrences de '{sous_chaine}' dans la chaîne.")
else:
    print(f"'{sous_chaine}' n'est pas une sous-chaîne dans la chaîne donnée.")
