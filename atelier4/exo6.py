from copy import deepcopy


def sort_list(lst_param: list):
    """
    Retourne une nouvelle liste triée par ordre croissant.
    :param lst: (list) liste d'éléments
    :return: (list) liste triée
    """
    lst = list(lst_param)
    len_lst = len(lst)
    if len_lst > 1:
        for k in range(len_lst):
            min = k
            for i in range(k + 1, len_lst):
                if lst[i] < lst[min]:
                    min = i
            lst[k], lst[min] = lst[min], lst[k]
    return lst


# print(sort_list([4, 6, 5, 3, 7, 9, 1, 2]))
