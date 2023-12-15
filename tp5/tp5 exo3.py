def est_palindrome(phrase):
    phrase_epuree = ''.join(c.lower() for c in phrase if c.isalpha())

    return phrase_epuree == phrase_epuree[::-1]

entree = input("Entrez un mot ou une phrase : ")

if est_palindrome(entree):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
