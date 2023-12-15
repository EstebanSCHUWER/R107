def table_multiplication(nombre, n):
    resultat_table = []

    for i in range(10):
        resultat = nombre * i
        resultat_arrondi = round(resultat, n)
        resultat_table.append((nombre, i, resultat_arrondi))

    return resultat_table


def afficher_table(table):
    print(f"Vous cherchez la table de multiplication de quel nombre ?")

    for nombre, i, resultat_arrondi in table:
        print(f"{nombre} * {i} = {resultat_arrondi}")

    print("Vous allez vous apercevoir qu’avec Python, {:.1f} * 3 donne {:.1f} !".format(table[0][0], table[3][2]))
    print(
        "C’est complètement normal étant donné que les fractions sont représentées d’une manière approchée par les ordinateurs.")
    print(
        "Pour afficher plutôt {:.1f}, vous pouvez utiliser la fonction round(x, n) qui prend un nombre x en entrée et l’arrondit à n décimales.")


# Utilisation du script avec le nombre 1.2 arrondi à une décimale
nombre_reel = 1.2
nombre_decimales = 1
table = table_multiplication(nombre_reel, nombre_decimales)
afficher_table(table)
