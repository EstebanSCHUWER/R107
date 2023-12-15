def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)


def verifier_date(date):
    if len(date) != 8:
        print("La date n'est pas au bon format. Veuillez saisir une date valide (jjmmaaaa).")
        return

    jour = int(date[0:2])
    mois = int(date[2:4])
    annee = int(date[4:])

    if jour < 1 or jour > 31:
        print("Le jour n'est pas valide. Veuillez saisir un jour entre 01 et 31.")
        return

    if mois < 1 or mois > 12:
        print("Le mois n'est pas valide. Veuillez saisir un mois entre 01 et 12.")
        return

    if annee < 1 or annee > 9999:
        print("L'année n'est pas valide. Veuillez saisir une année entre 0001 et 9999.")
        return

    jours_dans_mois = [31, 28 if not est_bissextile(annee) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if jour > jours_dans_mois[mois - 1]:
        print(f"Le jour {jour} n'est pas valide pour le mois {mois}.")
        return

    print(f"La date {date} est valide.")


verifier_date("3102199")
verifier_date("31041000")
verifier_date("32052020")
verifier_date("30032021")
verifier_date("29022022")
