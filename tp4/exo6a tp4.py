def tri_par_selection(liste):
    n = len(liste)

    for i in range(n):
        indice_min = i
        for j in range(i + 1, n):
            if liste[j] < liste[indice_min]:
                indice_min = j

        liste[i], liste[indice_min] = liste[indice_min], liste[i]

        print(liste)

liste_a_trier = [5, 2, 4, 8, 1, 3]

print("Liste originale:", liste_a_trier)
tri_par_selection(liste_a_trier)
