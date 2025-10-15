def remove_vowels_it(s):
    """Retire les voyelles de la chaÃ®ne de caractÃ¨re passÃ©e en paramÃ¨tre

    Args:
        s (str): chaine de caractÃ¨re Ã  traiter

    Returns:
        str: chaine de caractÃ¨re privÃ©e de ses voyelles

    >>> s = "elephant"
    >>> remove_vowels_it(s)
    'lphnt'
    >>> s = "crocodile"
    >>> remove_vowels_it(s)
    'crcdl'
    >>> s = "girafe"
    >>> remove_vowels_it(s)
    'grf'
    >>> s = "phacochere"
    >>> remove_vowels_it(s)
    'phcchr'
    >>> s = "ornithorynque"
    >>> remove_vowels_it(s)
    'rnthrnq'
    """
    out = ""
    for c in s:
        if c in "aeiouy": continue
        out += c
    return out

def remove_vowels_rec(s):
    """Retire les voyelles de la chaÃ®ne de caractÃ¨re passÃ©e en paramÃ¨tre

    Args:
        s (str): chaine de caractÃ¨re Ã  traiter

    Returns:
        str: chaine de caractÃ¨re privÃ©e de ses voyelles

    >>> s = "elephant"
    >>> remove_vowels_rec(s)
    'lphnt'
    >>> s = "crocodile"
    >>> remove_vowels_rec(s)
    'crcdl'
    >>> s = "girafe"
    >>> remove_vowels_rec(s)
    'grf'
    >>> s = "phacochere"
    >>> remove_vowels_rec(s)
    'phcchr'
    >>> s = "ornithorynque"
    >>> remove_vowels_rec(s)
    'rnthrnq'
    """
    # base case
    if not s:
        return ""
    # recursive call si s starts with a vowel
    if s[0] in "aeiouy":
        return remove_vowels_rec(s[1:])
    # recursive call if s starts with a consonant
    if s[0] not in "aeiouy":
        return s[0] + remove_vowels_rec(s[1:])
    
    return ""

    
def main():
    pass
    s = "phacochere"
    print(remove_vowels_rec(s))

if __name__ == "__main__":
    main()