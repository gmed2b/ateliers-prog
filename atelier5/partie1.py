def somme_recursive(lst: list) -> int:
    """
    Retourne la somme de tous les éléments.
    :param lst: (list) liste d'entiers
    :return: (int) la somme des entiers
    """
    if not lst:
        return 0
    else:
        return lst[0] + somme_recursive(lst[1:])


def factorielle_recursive(num: int) -> int:
    """
    Retourne la factorielle d'un nombre.
    :param num: (int) nombre
    :return: (int) factorielle
    """
    if num == 0:
        return 1
    else:
        return num * factorielle_recursive(num - 1)


def list_pairs(lst: list) -> list:
    """
    Retourne une liste contenant les nombres pairs.
    :param lst: (list) liste d'entiers
    :return: (list) liste des nombres pairs
    """
    if len(lst) == 0:
        return []
    else:
        if lst[0] % 2 == 0:
            return [lst[0]] + list_pairs(lst[1:])
        else:
            return list_pairs(lst[1:])


def longueur(lst: list) -> int:
    """
    Retourne la longueur d'une liste.
    :param lst: (list) liste
    :return: (int) longueur de la liste
    """
    if not lst:
        return 0
    else:
        return 1 + longueur(lst[1:])


def find_min(lst: list) -> int:
    """
    Retourne le minimum d'une liste
    :param lst: (list) liste d'entiers
    :return: (int) le minimum
    """
    if not lst:
        raise ValueError("Can't get empty list")
    elif not lst[1:]:
        return lst[0]
    else:
        if lst[0] < lst[1]:
            return find_min([lst[0]] + lst[2:])
        else:
            return find_min(lst[1:])


def concat_list(lst: list) -> list:
    """
    Retourne une liste plate
    :param lst: (list) liste de listes
    :return: (list) liste plate
    """
    if not lst:
        return []
    else:
        return lst[0] + concat_list(lst[1:])


def concat_list_v2(lst: list, acc = []) -> list:
    """
    Retourne une liste plate
    :param lst: (list) liste de listes
    :return: (list) liste plate
    """
    if not lst:
        return acc
    else:
        acc += lst[0]
    return concat_list_v2(lst[1:], acc)


print(concat_list([[1, 3], [2], [5, 4]]))
