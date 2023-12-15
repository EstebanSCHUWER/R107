import random

nombre_mystere = random.randint(0, 100)

compteur_tours = 0

while True:
    guess = int(input("Devinez la valeur entre 0 et 100 : "))
    compteur_tours += 1

    if guess < nombre_mystere:
        print("La valeur à deviner est plus grande.")
    elif guess > nombre_mystere:
        print("La valeur à deviner est plus petite.")
    else:
        print(f"Bravo ! Vous avez trouvé la valeur mystère {nombre_mystere} en {compteur_tours} tours.")
        break
