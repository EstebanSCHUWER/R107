dic1 = {"name": "Schuwer", "firstname": "Esteban", "promo": 2023, "group": 112}

dic2 = {"name": "Boulayoune", "firstname": "Yasser", "promo": 2023, "group": 112}

print("Les clés du premier dictionnaire sont :")
for key in dic1.keys():
    print(f"-{key}")

print("\nLes valeurs du premier dictionnaire sont :")
for value in dic1.values():
    print(f"-{value}")

print("\nLes tuplets du premier dictionnaire sont :")
for item in dic1.items():
    print(f"-{item}")

print("\n" + "="*30 + "\n")

print("Les clés du deuxième dictionnaire sont :")
for key in dic2.keys():
    print(f"-{key}")

print("\nLes valeurs du deuxième dictionnaire sont :")
for value in dic2.values():
    print(f"-{value}")

print("\nLes tuplets du deuxième dictionnaire sont :")
for item in dic2.items():
    print(f"-{item}")
