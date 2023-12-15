def calculer_salaire(heures_travaillees, salaire_horaire):
    heures_normales = min(heures_travaillees, 160)
    heures_majoration_25 = max(0, min(heures_travaillees - 160, 40))
    heures_majoration_50 = max(0, heures_travaillees - 200)

    salaire_total = (heures_normales * salaire_horaire) + \
                    (heures_majoration_25 * salaire_horaire * 1.25) + \
                    (heures_majoration_50 * salaire_horaire * 1.5)

    return salaire_total

heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))

salaire = calculer_salaire(heures_travaillees, salaire_horaire)

print(f"Le salaire total est de {salaire:.2f} euros.")
