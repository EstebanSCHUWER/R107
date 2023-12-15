def calcul_factorielle_for(n):
    factorielle = 1
    for i in range(1, n + 1):
        factorielle *= i
        print(f"Étape {i}: {factorielle}")
    return factorielle

def calcul_factorielle_while(n):
    factorielle = 1
    i = 1
    while i <= n:
        factorielle *= i
        print(f"Étape {i}: {factorielle}")
        i += 1
    return factorielle

n = int(input("Entrez un entier pour calculer sa factorielle : "))

choix_boucle = input("Choisissez la boucle (for/while) : ")

if choix_boucle.lower() == 'for':
    resultat = calcul_factorielle_for(n)
elif choix_boucle.lower() == 'while':
    resultat = calcul_factorielle_while(n)
else:
    print("Choix de boucle non valide.")

print(f"\nLa factorielle de {n} est : {resultat}")
