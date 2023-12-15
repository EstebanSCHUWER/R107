import time

n = int(input("Entrez un nombre entier positif : "))

print(f"\nCompte à rebours (while) :")
while n >= 0:
    print(n)
    n -= 1
    time.sleep(1)
