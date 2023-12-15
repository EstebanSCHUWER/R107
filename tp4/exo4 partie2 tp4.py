def most_frequent(lst):
    max_element = max(set(lst), key=lst.count)
    max_count = lst.count(max_element)

    return max_element, max_count

liste_exemple = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]
resultat = most_frequent(liste_exemple)

print(f"Le nombre le plus frequent dans la liste est le : {resultat[0]} ({resultat[1]} x)")
