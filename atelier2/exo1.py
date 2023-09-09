def somme_for_i(l: list) -> int:
    """Retourne la somme des éléments d'une liste l
    :arg l: (list) liste d'entiers
    :return: (int) somme des éléments de l
    """
    somme = 0
    for i in range(len(l)):
        somme += l[i]
    return somme


def somme_for_e(l: list) -> int:
    """Retourne la somme des éléments d'une liste l
    :arg l: (list) liste d'entiers
    :return: (int) somme des éléments de l
    """
    somme = 0
    for e in l:
        somme += e
    return somme


def somme_while(l: list) -> int:
    """Retourne la somme des éléments d'une liste l
    :arg l: (list) liste d'entiers
    :return: (int) somme des éléments de l
    """
    somme = 0
    i = 0
    while i < len(l):
        somme += l[i]
        i += 1
    return somme


def moyenne(l: list) -> float:
    """Retourne la moyenne des éléments d'une liste l
    :arg l: (list) liste d'entiers
    :return: (float) moyenne des éléments de l
    """
    length = len(l)
    if length == 0:
        return 0
    return round(somme_for_i(l) / length, 2)


def nb_sup_for_i(l: list, e: int) -> int:
    """Retourne le nombre de valeurs strictement supérieures à e
    :arg l: (list) liste d'entiers
    :arg e: (int) entier à comparer
    :return: (int) nombre de valeurs strictement supérieures à e
    """
    nb = 0
    for i in range(len(l)):
        if l[i] > e:
            nb += 1
    return nb


def nb_sup_for_e(l: list, e: int) -> int:
    """Retourne le nombre de valeurs strictement supérieures à e
    :arg l: (list) liste d'entiers
    :arg e: (int) entier à comparer
    :return: (int) nombre de valeurs strictement supérieures à e
    """
    nb = 0
    for num in l:
        if num > e:
            nb += 1
    return nb


def moyenne_sup(l: list, e: int) -> float:
    """Retourne la moyenne des valeurs de la liste l
    strictement supérieures à e
    :arg l: (list) liste d'entiers
    :arg e: (int) entier à comparer
    :return: (float) moyenne des valeurs de l strictement supérieures à e
    """
    nb_sup = []
    for num in l:
        if num > e:
            nb_sup.append(num)
    return round(moyenne(nb_sup), 2)


def moyenne_sup_v2(l: list, e: int) -> float:
    """Retourne la moyenne des valeurs de la liste l
    strictement supérieures à e
    :arg l: (list) liste d'entiers
    :arg e: (int) entier à comparer
    :return: (float) moyenne des valeurs de l strictement supérieures à e
    """
    somme = 0
    for num in l:
        if num > e:
            somme += num
    return somme / nb_sup_for_e(l, e)


def val_max(l: list) -> int:
    """Retourne la valeur maximal d'une liste l
    :arg l: (list) liste d'entiers
    :return: (int) max de la liste l
    """
    max = l[0]
    for num in l:
        if num > max:
            max = num
    return max


def ind_max(l: list) -> int:
    """Retourne l'indice de la valeur maximal d'une liste l
    :arg l: (list) liste d'entiers
    :return: (int) indice de la valeur max
    """
    idx = None
    max = l[0]
    for i in range(len(l)):
        if l[i] > max:
            max = l[i]
            idx = i
    return idx


def test_exercice1():
    """Fonction de test des fonctions de l'exercice 1"""
    l = [2, 9, 3, 23, 5, 11, 18, 4, 13, 28, 1, 9]
    print("Liste de test: ", l)
    print("Somme avec for i: ", somme_for_i(l))
    print("Somme avec for e: ", somme_for_e(l))
    print("Somme avec while: ", somme_while(l))
    print("Moyenne: ", moyenne(l))
    print("Nombre de valeurs strictement supérieures à 5 avec for i: ", nb_sup_for_i(l, 5))
    print("Nombre de valeurs strictement supérieures à 5 avec for e: ", nb_sup_for_e(l, 5))
    print("Moyenne des valeurs strictement supérieures à 5: ", moyenne_sup(l, 5))
    print("Moyenne V2 des valeurs strictement supérieures à 5: ", round(moyenne_sup_v2(l, 5), 2))
    print("Valeur max: ", val_max(l))
    print("Indice de la valeur max: ", ind_max(l))


test_exercice1()
