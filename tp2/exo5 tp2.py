nombre = float(input("Entrez un nombre : "))

if nombre > 0:
    print("Le nombre est positif.")
elif nombre < 0:
    print("Le nombre est négatif.")
else:
    print("Le nombre est égal à zéro.")

if nombre % 2 == 0:
    print("Le nombre est pair.")
else:
    print("Le nombre est impair.")
