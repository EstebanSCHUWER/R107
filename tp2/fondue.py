BASE = 4
fromage_base = 800.0
eau_base = 2
ail_base = 2
pain_base = 400

nbConvives = int(input("Entrez le nombre de convives : "))

fromage = fromage_base * nbConvives / BASE
eau = eau_base * nbConvives / BASE
ail = ail_base * nbConvives / BASE
pain = pain_base * nbConvives / BASE

print(f"\nRecette pour {nbConvives} convives :\n")
print(f"Fromage: {fromage} grammes")
print(f"Eau: {eau} décilitres")
print(f"Ail: {ail} gousses")
print(f"Pain: {pain} grammes")
