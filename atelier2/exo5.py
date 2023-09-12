def vitrines(nb_max: int, objets: list) -> (list, list):
    """Retourne le couple de listes (vitrine1, vitrine2) tel que
    chaque vitrine ne peut contenir deux objets identiques
    :arg nb_max: nombre d'emplacements dans chaque vitrine
    :arg objets: liste des objets à placer dans les vitrines
    :return: couple de listes (vitrine1, vitrine2)
    """
    len_objets = len(objets)
    if nb_max <= len_objets // 2:
        raise ValueError("STOOOOPP! Le nombre d'objets est trop grand pour le nombre d'emplacements")

    vitrine1 = []
    nb_vitrine1 = 0
    vitrine2 = []
    nb_vitrine2 = 0
    for i in range(len_objets):
        if objets[i] not in vitrine1 and nb_vitrine1 < nb_vitrine2:
            vitrine1.append(objets[i])
            nb_vitrine1 += 1
        else:
            vitrine2.append(objets[i])
            nb_vitrine2 += 1
    return vitrine1, vitrine2


def test():
    L = [1, 2, 2, 3, 4, 5, 5]
    emplacement = 4
    print(vitrines(emplacement, L))


test()