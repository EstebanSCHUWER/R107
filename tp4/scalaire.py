n_max = 5

n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {n_max}] ? "))

while n < 1 or n > n_max:
    print(f"La taille des vecteurs doit être entre 1 et {n_max}.")
    n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 3] ? "))

v1 = []
v2 = []

print("Saisie du premier vecteur :")
for i in range(n):
    composante = int(input(f"v1[{i}] = "))
    v1.append(composante)

print("Saisie du second vecteur :")
for i in range(n):
    composante = int(input(f"v2[{i}] = "))
    v2.append(composante)

produit_scalaire = sum(x * y for x, y in zip(v1, v2))

print(f"Le produit scalaire des vecteurs v1 et v2 est : {produit_scalaire}")
