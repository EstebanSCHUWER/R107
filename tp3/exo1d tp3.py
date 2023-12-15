X = float(input("Entrez un nombre X supérieur à 1 : "))
N = 0
somme = 0

while somme <= X:
    N += 1
    somme += N

print("Le plus grand nombre N tel que la somme de 0 à N est inférieure ou égale à", X, "est :", N - 1)
