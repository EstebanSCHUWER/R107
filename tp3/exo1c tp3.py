valeurs_inf_10 = 0
valeurs_10_15 = 0
valeurs_sup_15 = 0

for _ in range(10):
    valeur = float(input("Entrez une valeur réelle entre 0 et 20 : "))

    while valeur < 0 or valeur > 20:
        valeur = float(input("Valeur incorrecte. Entrez une valeur réelle entre 0 et 20 : "))

    if valeur < 10:
        valeurs_inf_10 += 1
    elif valeur < 15:
        valeurs_10_15 += 1
    else:
        valeurs_sup_15 += 1

print("Nombre de valeurs inférieur strictement à 10 :", valeurs_inf_10)
print("Nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15 :", valeurs_10_15)
print("Nombre de valeurs supérieur ou égale à 15 :", valeurs_sup_15)
