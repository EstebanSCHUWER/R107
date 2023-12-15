import time

n = int(input("Entrez un nombre entier positif : "))

print(f"\nCompte à rebours (for) :")
for i in range(n, -1, -1):
    print(i)
    time.sleep(1)
