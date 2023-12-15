heure_debut = int(input("Entrez l'heure de début de la location (0-24) : "))
heure_fin = int(input("Entrez l'heure de fin de la location (0-24) : "))

if not (0 <= heure_debut <= 24) or not (0 <= heure_fin <= 24):
    print("Les heures doivent être comprises entre 0 et 24 !")
elif heure_debut == heure_fin:
    print("Attention ! L'heure de fin est identique à l'heure de début.")
elif heure_debut > heure_fin:
    print("Attention ! L'heure de début de la location est après l'heure de fin.")
else:
    if (heure_debut >= 0 and heure_fin <= 7) or (heure_debut >= 17 and heure_fin <= 24):
        cout_location = (heure_fin - heure_debut) * 1
    else:
        cout_location = (heure_fin - heure_debut) * 2

    print(f"Le coût de la location est de {cout_location} euros.")
