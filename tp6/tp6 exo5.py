import unicodedata

def nettoyer_texte(texte):
    texte = ''.join(c for c in texte if c.isalnum() or c.isspace())
    return texte

def supprimer_accents(texte):
    return ''.join(char for char in unicodedata.normalize('NFD', texte) if unicodedata.category(char) != 'Mn')

def est_palindrome(texte):
    texte = nettoyer_texte(texte.lower())
    texte = supprimer_accents(texte)
    return texte == texte[::-1]

mot_phrase = input("Entrez un mot ou une phrase : ")

if est_palindrome(mot_phrase):
    print("C'est un palindrome!")
else:
    print("Ce n'est pas un palindrome.")
