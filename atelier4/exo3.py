import random


def choose_element_list(list_in_which_to_choose: list) -> any:
    """
    Retourne un élément de la liste au hasard.
    :param list_in_which_to_choose: (list) Liste dans laquelle on veut choisir un élément.
    :return: (list) Un élément de la liste.
    """
    return list_in_which_to_choose[random.randint(0, len(list_in_which_to_choose) - 1)]


def test():
    lst_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Test de votre code
    print('Liste triée de départ', lst_sorted)
    e1 = choose_element_list(lst_sorted)
    print('A la première exécution', e1, 'a été sélectionné')
    e2 = e1
    different = False
    while not different:
        e2 = choose_element_list(lst_sorted)
        if e1 != e2:
            different = True
    print('A la deuxième exécution', e2, 'a été sélectionné')
    assert e1 != e2, "Attention vérifiez votre code, pour deux sélections de suite l'élément sélectionné est le même !"


# test()