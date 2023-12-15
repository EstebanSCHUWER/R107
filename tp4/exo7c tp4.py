binome = ('login1', 'login2')

message_initial = f"L'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}"
print(message_initial)

try:
    del binome[1]
except TypeError as e:
    print(f"Erreur : {e}")

message_apres_suppression = f"L'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}"
print(message_apres_suppression)
