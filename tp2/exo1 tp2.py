x = int(input("Entrez la valeur de la variable x : "))
y = int(input("Entrez la valeur de la variable y : "))

print(f"Avant la permutation : x = {x}, y = {y}")

temp = x
x = y
y = temp

print(f"Après la permutation : x = {x}, y = {y}")
