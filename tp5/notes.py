def calculer_moyenne(notes, coefficients):
    somme_notes_ponderees = sum(note * coef for note, coef in zip(notes, coefficients))
    somme_coefficients = sum(coefficients)
    moyenne = somme_notes_ponderees / somme_coefficients
    return moyenne

def est_admis(moyenne, notes):
    return moyenne > 10 and all(note >= 8 for note in notes)

notes = []
coefficients = []

for i in range(5):
    try:
        entree = input(
            f"Veuillez entrer la note du module {i + 1} et le coefficient correspondant (séparés par un espace) : ")
        valeurs = entree.split()
        note = float(valeurs[0])
        coefficient = int(valeurs[1])

        notes.append(note)
        coefficients.append(coefficient)
    except (ValueError, IndexError):
        print("Erreur de saisie. Veuillez entrer des valeurs valides.")

moyenne_generale = calculer_moyenne(notes, coefficients)

print(f"\nMoyenne générale : {moyenne_generale:.2f}")

if est_admis(moyenne_generale, notes):
    print("L'étudiant est admis.")
else:
    print("L'étudiant n'est pas admis.")
