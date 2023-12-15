binome = ('login1', 'login2')

message_initial = f"L'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}"
print(message_initial)

binome_avec_troisieme = binome + ('login3',)

message_avec_troisieme = f"L'étudiant {binome_avec_troisieme[0]} est en trinôme avec les étudiants {binome_avec_troisieme[1]} et {binome_avec_troisieme[2]}"
print(message_avec_troisieme)
