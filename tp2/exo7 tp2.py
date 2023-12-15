import random

def lancer_truque():
    return random.choice(["Pile", "Face"])

nombre_de_lancers = 1000
pile_count = 0

for _ in range(nombre_de_lancers):
    resultat = lancer_truque()
    if resultat == "Pile":
        pile_count += 1

frequence_pile = pile_count / nombre_de_lancers

print(f"Fréquence de 'Pile' sur {nombre_de_lancers} lancers : {frequence_pile:.2%}")
