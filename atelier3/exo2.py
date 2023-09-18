def mots_Nlettres(lst: list, n: int) -> list:
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
    return mots_Nlettres(finissent_par(commencent_par(lst, prefixe), suffixe), n)


def dictionnaire(file: str):
    f = open(file, "r")
    return f.readlines()

# Tests

def test_mots_Nlettres():
    assert mots_Nlettres(["chat", "chien", "oiseau", "cheval"], 5) == ["chien"]
    assert mots_Nlettres(["chat", "chien", "oiseau", "cheval"], 6) == ["oiseau", "cheval"]
    assert mots_Nlettres(["chat", "chien", "oiseau", "cheval"], 4) == ["chat"]
    assert mots_Nlettres(["chat", "chien", "oiseau", "cheval"], 7) == []
    print("test_mots_Nlettres passed")


def test_commence_par():
    assert commence_par("python", "py") == True
    assert commence_par("python", "pY") == False
    assert commence_par("python", "python3") == False
    assert commence_par("python", "thon") == False
    assert commence_par("python", "python") == True
    print("test_commence_par passed")


def test_finit_par():
    assert finit_par("python", "on") == True
    assert finit_par("python", "oN") == False
    assert finit_par("python", "python3") == False
    assert finit_par("python", "py") == False
    assert finit_par("python", "python") == True
    print("test_finit_par passed")


def test_finissent_par():
    assert finissent_par(["chat", "chien", "oiseau", "cheval"], "en") == ["chien"]
    assert finissent_par(["chat", "chien", "oiseau", "cheval"], "al") == ["cheval"]
    assert finissent_par(["chat", "chien", "oiseau", "cheval"], "au") == ["oiseau"]
    assert finissent_par(["chat", "chien", "oiseau", "cheval"], "at") == ["chat"]
    assert finissent_par(["chat", "chien", "oiseau", "cheval"], "ot") == []
    print("test_finissent_par passed")


def test_commencent_par():
    assert commencent_par(["chat", "chien", "oiseau", "cheval"], "ch") == ["chat", "chien", "cheval"]
    assert commencent_par(["chat", "chien", "oiseau", "cheval"], "oi") == ["oiseau"]
    assert commencent_par(["chat", "chien", "oiseau", "cheval"], "che") == ["cheval"]
    assert commencent_par(["chat", "chien", "oiseau", "cheval"], "ca") == []
    assert commencent_par(["chat", "chien", "oiseau", "cheval"], "chi") == ["chien"]
    print("test_commencent_par passed")


def test_liste_mots():
    words_list = ["chat", "chien", "oiseau", "cheval", "chiennerie"]
    assert liste_mots(words_list, "ch", "en", 5) == ["chien"]
    assert liste_mots(words_list, "ch", "al", 6) == ["cheval"]
    assert liste_mots(words_list, "oi", "eau", 6) == ["oiseau"]
    assert liste_mots(words_list, "ch", "erie", 10) == ["chiennerie"]
    assert liste_mots(words_list, "ch", "at", 4) == ["chat"]
    print("test_liste_mots passed")


# Exécutez toutes les fonctions de test
test_mots_Nlettres()
test_commence_par()
test_finit_par()
test_finissent_par()
test_commencent_par()
test_liste_mots()
