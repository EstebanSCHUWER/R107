def ajouter_elt(lst=[0, 1, 2], elt=3):
    lst.append(elt)
    return lst

for _ in range(3):
    print(ajouter_elt(), "ID de lst :", id(ajouter_elt.__defaults__[0]))

def ajouter_carac(ch="abc", elt="d"):
    return ch + elt

for _ in range(3):
    print(ajouter_carac(), "ID de ch :", id(ajouter_carac.__defaults__[0]))
