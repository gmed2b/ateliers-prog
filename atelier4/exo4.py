from exo3 import choose_element_list


def extract_elements_list(list_in_which_to_choose: list, int_nbr_of_element_to_extract: int = 10) -> list:
    len_list = len(list_in_which_to_choose)
    if int_nbr_of_element_to_extract > len_list:
        int_nbr_of_element_to_extract = len_list
    new_list = [None] * int_nbr_of_element_to_extract
    for i in range(int_nbr_of_element_to_extract):
        new_list[i] = choose_element_list(list_in_which_to_choose)
    return new_list


def test():
    # Test de votre code
    lst_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('Liste de départ', lst_sorted)
    sublist = extract_elements_list(lst_sorted, 3)
    print('La sous liste extraite est', sublist)
    print('Liste de départ après appel de la fonction est', lst_sorted)


# test()
