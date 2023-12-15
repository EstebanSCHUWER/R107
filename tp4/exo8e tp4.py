dic1 = {"name": "Schuwer", "firstname": "Esteban", "promo": 2023, "group": 112}

dic2 = {"name": "Boulayoune", "firstname": "Yasser", "promo": 2023, "group": 112}

binome = {
    "id1": dic1,
    "id2": dic2
}

print("Les clés du dictionnaire 'binome' sont :", binome.keys())

print("\nLes valeurs du dictionnaire 'binome' sont :")
for value in binome.values():
    print(f"-{value}")
