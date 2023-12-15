a = int(input("Entrez le premier nombre (a) : "))
b = int(input("Entrez le deuxième nombre (b) : "))
c = int(input("Entrez le troisième nombre (c) : "))

print("Nombres initiaux :")
print(f"a = {a}, b = {b}, c = {c}")

temp = a
a = b
b = c
c = temp

print("\nNombres après permutation :")
print(f"a = {a}, b = {b}, c = {c}")
