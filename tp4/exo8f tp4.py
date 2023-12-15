binome = {
    "id1": {"name": "Schuwer", "firstname": "Esteban", "group": 112},
    "id2": {"name": "Boulayoune", "firstname": "Yasser", "group": 112}
}

print("Les étudiants formant le binôme sont :")
for student_id, student_info in binome.items():
    print(f"- L'étudiant {student_info['name']} {student_info['firstname']} du groupe {student_info['group']}")
