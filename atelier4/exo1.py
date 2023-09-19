import random


def gen_list_random_int(num: int = 10, inf: int = 0, sup: int = 10) -> list:
    """
    Génère une liste de num nombres entiers aléatoires compris entre inf et sup
    :param num: (int) nombre d'éléments de la liste
    :param inf: (int) borne inférieure (incluse)
    :param sup: (int) borne supérieure (exclus)
    :return: (list) liste de num nombres entiers aléatoires compris entre inf et sup
    """
    return [random.randint(inf, sup-1) for _ in range(num)]


def test():
    print(gen_list_random_int())
    print(gen_list_random_int(5))
    print(gen_list_random_int(5, 1, 6))


# test()