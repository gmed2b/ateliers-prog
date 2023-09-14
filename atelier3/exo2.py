def mots_n_lettres(lst: list, n: int) -> list:
    """Retourne la liste des mots contenant exactement n caractères
    :param lst: (list) liste de mots
    :param n: (int) nombre de caractères
    :return: (list) liste des mots filtrés
    """
    return list(filter(lambda word: len(word) == n, lst))


def commence_par(mot: str, prefixe: str) -> bool:
    """Retourne True si le mot commence par le prefix, False sinon
    :param mot: (str) mot à verifier
    :param prefixe: (str) préfix à verifier
    :return: (bool) si mot commence par prefix
    """
    result = True
    len_prefix = len(prefixe)
    if len_prefix > len(mot):
        result = False
    else:
        i = 0
        while i < len_prefix and result:
            if mot[i] != prefixe[i]:
                result = False
            i += 1
    return result


def finit_par(mot: str, suffixe: str) -> bool:
    """Retourne True si le mot finit par le suffixe, False sinon
    :param mot: (str) mot à verifier
    :param suffixe: (str) suffixe à verifier
    :return: (bool) si mot finit par le suffixe
    """
    return mot == mot[:len(mot) - len(suffixe)] + suffixe


def finissent_par(lst: list, suffixe: str) -> list:
    """Retourne la liste des mots finissant par suffixe
    :param lst: (list) liste de mots
    :param suffixe: (str) suffixe à verifier
    :return: (list) liste finissant par suffixe
    """
    return [mot for mot in lst if finit_par(mot, suffixe)]


def commencent_par(lst: list, prefixe: str) -> list:
    """Retourne la liste des mots commencant par prefixe
    :param lst: (list) liste de mots
    :param prefixe: (str) prefixe à verifier
    :return: (list) liste commencant par prefixe
    """
    return [mot for mot in lst if commence_par(mot, prefixe)]


def liste_mots(lst: list, prefixe: str, suffixe: str, n: int):
    """Retourne la liste des mots commencant par prefixe, finissant par suffixe et contenant exactement n caractères
    :param lst: (list) liste de mots
    :param prefixe: (str) prefixe à verifier
    :param suffixe: (str) suffixe à verifier
    :param n: (int) nombre de caractères
    :return: (list) liste des mots commencant par prefixe, finissant par suffixe et contenant exactement n caractères
    """
    return mots_n_lettres(finissent_par(commencent_par(lst, prefixe), suffixe), n)
