#### Fonction secondaire

import string

def ispalindrome(p):
    # Met en minuscules
    p = p.lower()
    # Supprime les espaces
    p = p.replace(" ", "")
    # Supprime la ponctuation
    punct = string.punctuation
    for c in punct:
        p = p.replace(c, "")
    # Supprime les accents
    #dic = {'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'à': 'a', 'â': 'a', 'ù': 'u', 'û': 'u', 'ô': 'o', 'î': 'i', 'ï': 'i', 'ç': 'c'}
    p = p.translate(str.maketrans('éèêëàâùûôîïç', 'eeeeaauuoiic'))

    # Vérifie si le mot est un palindrome
    if p == p[::-1]:
        return True
    return False


#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()