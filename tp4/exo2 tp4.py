nombre_etudiants = int(input("Donnez le nombre d'étudiants : "))
moyenne = 0.0

notes = []

for i in range(nombre_etudiants):
    note = float(input(f"Note de l'étudiant {i} : "))

    while note < 0 or note > 20:
        print("La note doit être comprise entre 0 et 20.")
        note = float(input(f"Note de l'étudiant {i} : "))

    notes.append(note)
    moyenne += note

moyenne /= nombre_etudiants

print(f"\nMoyenne de classe : {moyenne:.2f}\n")

print("Numéro de l'Étudiant | Note | Écart à la moyenne")
for i, note in enumerate(notes):
    ecart = note - moyenne
    print(f"{i} | {note} | {ecart:.2f}")
