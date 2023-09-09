
def position_for(lst: list, elt: int) -> int:
    """Retourne l'indice de l'entier elt si présent dans lst, -1 autrement
    :arg lst: (list) liste d'entiers
    :arg elt: (int) entier à chercher
    :return: (int) indice de l'entier elt
    """
    idx = -1
    length = len(lst)
    for i in range(length):
        if lst[i] == elt:
            idx = i
    return idx


def position_while(lst: list, elt: int) -> int:
    """Retourne l'indice de l'entier elt si présent dans lst, -1 autrement
    :arg lst: (list) liste d'entiers
    :arg elt: (int) entier à chercher
    :return: (int) indice de l'entier elt
    """
    length = len(lst)
    i = 0
    while lst[i] != elt and i < length:
        i += 1
    return i if i < length-1 else -1


def nb_occurrences(lst: list, e: int) -> int:
    """Retourne le nombre d'occurrences de l'entier e dans la list lst
    :arg lst: (list) liste d'entiers
    :arg e: (int) entier à chercher
    :return: (int) nombre d'occurrences de l'entier e
    """
    occurrences = 0
    for num in lst:
        if e == num:
            occurrences += 1
    return occurrences


def est_triee_for(lst: list) -> bool:
    """Retourne un booléen si la liste lst est triée par ordre croissant
    :arg lst: (list) liste d'entiers
    :return: (bool) True si la liste est triée, False autrement
    """
    result = True
    prev = lst[0]
    for current in lst:
        if current < prev:
            result = False
    return result


def est_triee_while(lst: list) -> bool:
    """Retourne un booléen si la liste lst est triée par ordre croissant
    :arg lst: (list) liste d'entiers
    :return: (bool) True si la liste est triée, False autrement
    """
    length = len(lst)
    result = True
    i = 0
    while lst[i] <= lst[i+1] and i < length:
        i += 1
    return result if i == length-1 else False


def dichotomie(lst: list, e: int, low: int, high: int) -> int:
    """Retourne l'indice de l'entier e si présent dans lst
    par recherche dichotomique, -1 autrement
    :arg lst: (list) liste d'entiers
    :arg e: (int) entier à chercher
    :arg low: (int) borne inferieur
    :arg high: (int) borne superieur
    :return: (int) indice de l'entier e
    """
    if high >= low:
        mid = round((low + high) / 2)
        if e == lst[mid]:
            return mid
        elif e < lst[mid]:
            return dichotomie(lst, e, low, mid - 1)
        elif e > lst[mid]:
            return dichotomie(lst, e, mid + 1, high)
    else:
        return -1

def position_tri(lst: list, e: int) -> int:
    """Retourne l'indice de l'entier e si présent dans lst
    par recherche dichotomique, -1 autrement
    :arg lst: (list) liste d'entiers
    :arg elt: (int) entier à chercher
    :return: (int) indice de l'entier elt
    """
    borne_inf = 0
    borne_sup = len(lst) - 1
    return dichotomie(lst, e, borne_inf, borne_sup)

