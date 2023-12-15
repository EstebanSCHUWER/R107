import random

resultat_lancer = random.randint(0, 100)

if resultat_lancer < 50:
    print("Pile !")
else:
    print("Face !")
