binome = ('login1', 'login2')

message_initial = f"L'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}"
print(message_initial)

nouveau_login = input("Entrez le nouveau login pour le binôme : ")

binome = (binome[0], nouveau_login)

message_mis_a_jour = f"L'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}"
print(message_mis_a_jour)
