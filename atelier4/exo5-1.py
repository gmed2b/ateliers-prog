import random
import time
from exo2 import mix_list
from exo4 import extract_elements_list
from exo5 import graph

default_options = {
    "size_lst": [100, 500, 1000, 5000, 10000],
    "no_exec": 10,
    "extract_num": 10
}


def perf_mix(perso: callable, native: callable, size_lst=None, no_exec: int = default_options["no_exec"], is_extract: bool = False):
    """
    Compare les performances de deux fonctions avec différentes tailles de données
    :param perso: (callable) fonction à tester
    :param native: (callable) fonction de référence
    :param size_lst: (list) liste des tailles de données à tester. Default : [10, 500, 5000, 50000, 100000]
    :param no_exec: (int) nombre d'exécutions pour chaque taille de données. Default : 10
    :param is_extract: (bool) si True, on execute les fonctions avec un paramètre k. Default : False
    :return: (list, list) temps moyen pour la fonction perso, temps moyen pour la fonction native
    """
    if size_lst is None:
        size_lst = list(default_options["size_lst"])

    len_lst = len(size_lst)
    avg_perso = [None] * len_lst
    avg_native = [None] * len_lst

    current_index = 0
    for size in size_lst:
        lst = [i for i in range(size)]
        avg_perso_num, avg_native_num = 0, 0
        for i_exec in range(no_exec):
            # Temps execution pour la fonction perso
            start_pc = time.perf_counter()
            if is_extract:
                perso(lst, lst[-1] // 2)
            else:
                perso(lst)
            end_pc = time.perf_counter()
            avg_perso_num += end_pc - start_pc

            # Temps execution pour la fonction native
            start_pc = time.perf_counter()
            if is_extract:
                native(lst, lst[-1] // 2)
            else:
                native(lst)
            end_pc = time.perf_counter()
            avg_native_num += end_pc - start_pc

        avg_perso[current_index] = avg_perso_num / no_exec
        avg_native[current_index] = avg_native_num / no_exec
        current_index += 1

    return avg_perso, avg_native


def test(is_shuffle: bool = True):
    print("-- Debut du test --")
    print("Test en cours...")

    lst = [ 5000, 7500, 10000, 15000, 20000, 50000, 75000, 100000]
    result = ([], [])
    if is_shuffle:
        result = perf_mix(mix_list, random.shuffle, size_lst=lst, no_exec=100)
    else:
        result = perf_mix(extract_elements_list, random.sample, size_lst=lst, is_extract=True, no_exec=50)

    print("-- Fin du test --")
    print("Resultat du test :")
    print("Temps moyen pour la fonction perso : ", result[0])
    print("Temps moyen pour la fonction native : ", result[1])
    graph([
        {
            "size_lst": lst,
            "avg_lst": result[0],
            "label": "Perso",
            "color": 'bo-'
        },
        {
            "size_lst": lst,
            "avg_lst": result[1],
            "label": "Native",
            "color": 'ro-'
        }
    ])


# test()
test(False)
