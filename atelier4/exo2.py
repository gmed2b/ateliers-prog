import random
from copy import deepcopy


def mix_list_v1(list_to_mix: list) -> list:
    """
    Retourne la liste list_to_mix mélangée.
    :param list_to_mix: (list) Liste à mélanger
    :return: (list) Liste mélangée
    """
    len_list = len(list_to_mix)
    new_list = [None] * len_list
    for item in list_to_mix:
        picked = False
        while not picked:
            rand_int = random.randint(0, len_list - 1)
            if new_list[rand_int] is None:
                new_list[rand_int] = item
                picked = True
    return new_list


def mix_list(list_to_mix: list) -> list:
    """
    Retourne la liste list_to_mix mélangée.
    :param list_to_mix: (list) Liste à mélanger
    :return: (list) Liste mélangée
    """
    lst = deepcopy(list_to_mix)
    len_lst = len(lst)
    for i in range(len_lst):
        random_idx = random.randint(0, len_lst - 1)
        lst[i], lst[random_idx] = lst[random_idx], lst[i]
    return lst


def test():
    # Test de votre code
    lst_sorted = [i for i in range(1, 11)]
    print(lst_sorted)
    print('Liste triée de départ', lst_sorted)
    mixed_list = mix_list(lst_sorted)
    print('Liste mélangée obtenue', mixed_list)
    print('Liste triée de départ après appel à mixList, elle doit être inchangée', lst_sorted)
    # assert (cf. doc en ligne) permet de vérifier qu’une condition
    # est vérifiée en mode debug (désactivable)
    assert lst_sorted != mixed_list, "Les deux listes doivent être différente après l'appel à mixList..."


test()
