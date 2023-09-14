BORNE_1_MAJ = 65
BORNE_2_MAJ = 90
BORNE_1_MIN = 97
BORNE_2_MIN = 122


def to_upper(ascii_caractere: int) -> str:
    return chr(ascii_caractere - 32)


def to_lower(ascii_caractere: int) -> str:
    return chr(ascii_caractere + 32)


def is_maj(c: int) -> bool:
    return BORNE_1_MAJ <= c <= BORNE_2_MAJ


def is_min(c: int) -> bool:
    return BORNE_1_MIN <= c <= BORNE_2_MIN


def full_name(str_arg: str) -> str:
    """
    Returns the full name of a person
    :arg str_arg: (str) the name of the person in format 'last_name first_name'
    """
    nom_majuscule = ""
    est_nom = True
    est_prenom = False
    for caractere in str_arg:
        ascii_caractere = ord(caractere)
        if caractere == ' ':
            est_nom = False
            est_prenom = True
            nom_majuscule += ' '
        elif est_nom:
            # CAS LETTRE MINUSCULE
            if is_min(ascii_caractere):
                # TRANSFORMER EN MAJUSCULE
                nom_majuscule += to_upper(ascii_caractere)
            else:
                nom_majuscule += caractere
        else:
            if est_prenom:
                if is_min(ascii_caractere):
                    nom_majuscule += to_upper(ascii_caractere)
                else:
                    nom_majuscule += caractere
                est_prenom = False
            else:
                if is_maj(ascii_caractere):
                    nom_majuscule += to_lower(ascii_caractere)
                else:
                    nom_majuscule += caractere
    return nom_majuscule


def test():
    print(full_name(""))
    print(full_name("agag"))
    print(full_name("fig eva"))
    print(full_name("Fig evA"))
    print(full_name("AEGAEG Aaegag"))
    print(full_name("Aeag AEGJEGIP"))


test()