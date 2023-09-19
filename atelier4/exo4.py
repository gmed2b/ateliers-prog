from exo3 import choose_element_list
from copy import deepcopy
from random import randint


def extract_elements_list(list_in_which_to_choose: list, int_nbr_of_element_to_extract=10) -> list:
    len_list = len(list_in_which_to_choose)
    new_lst = deepcopy(list_in_which_to_choose)
    # Verifie que le nombre passé en paramètre ne soit pas supérieur à la liste
    if int_nbr_of_element_to_extract > len_list:
        int_nbr_of_element_to_extract = len_list
    return [new_lst.pop(randint(0, len_list - 1 - i)) for i in range(int_nbr_of_element_to_extract)]


def test():
    # Test de votre code
    lst_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('Liste de départ', lst_sorted)
    num = int(input("Combien d'element a retirer ? "))
    sublist = extract_elements_list(lst_sorted, num)
    print('La sous liste extraite est', sublist)
    print('Liste de départ après appel de la fonction est', lst_sorted)


# test()
