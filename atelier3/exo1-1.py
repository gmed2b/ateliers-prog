BORNE_A_MAJ = 65
BORNE_Z_MAJ = 90
BORNE_A_MIN = 97
BORNE_Z_MIN = 122


def to_upper(ascii_caractere: int) -> str:
    return chr(ascii_caractere - 32) if ascii_caractere - 32 >= 0 else chr(ascii_caractere)


def to_lower(ascii_caractere: int) -> str:
    return chr(ascii_caractere + 32) if ascii_caractere + 32 <= 0x10ffff else chr(ascii_caractere)


def is_maj(c: int) -> bool:
    return BORNE_A_MAJ <= c <= BORNE_Z_MAJ


def is_min(c: int) -> bool:
    return BORNE_A_MIN <= c <= BORNE_Z_MIN


def full_name(str_arg: str) -> str:
    """
    Retourne le nom et prenom d'une personne avec le nom en majuscule et le
    prenom avec la première lettre seulement
    :arg str_arg: (str) le nom d'une personne au format 'nom prenom'
    """
    len_str = len(str_arg)
    i = 0
    nom_majuscule = ""
    # On traite le nom tant qu'on croise pas l'espace
    while i < len_str and str_arg[i] != ' ':
        caractere = ord(str_arg[i])
        nom_majuscule += to_upper(caractere) if is_min(caractere) else str_arg[i]
        i += 1
    # On a fini le nom, on considere le reste comme des prenoms
    # Seulement s'il reste des caracteres a parcourir
    if i < len_str:
        # On ajoute l'espace entre le nom et prenom
        first_letter = True
        while i < len_str:
            if str_arg[i] != ' ':
                caractere = ord(str_arg[i])
                if first_letter:
                    nom_majuscule += to_upper(caractere) if is_min(caractere) else str_arg[i]
                    first_letter = False
                else:
                    nom_majuscule += to_lower(caractere) if is_maj(caractere) else str_arg[i]
            else:
                nom_majuscule += ' '
                first_letter = True
            i += 1

    return nom_majuscule


def test():
    print(full_name(""))
    print(full_name("agag"))
    print(full_name("fig eva"))
    print(full_name("Fig evA"))
    print(full_name("sMenghI AntO pIerRE PhILIppE"))
    print(full_name("AEGAEG Aaegag"))
    print(full_name("Aeag AEGJEGIP"))


test()
