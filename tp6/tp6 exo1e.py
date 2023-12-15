ma_chaine = "machaine"

print("e) Variable de chaîne :")
print("   Type de la variable :", type(ma_chaine))
print("   ID de la variable :", id(ma_chaine))

for i, caractere in enumerate(ma_chaine):
    print(f"   Caractère {i+1} :")
    print(f"      Valeur : {caractere}")
    print(f"      Type : {type(caractere)}")
    print(f"      ID : {id(caractere)}")
