import numpy as np


def matrice_adjacence(sommets: list, arcs: list[tuple[int, int]]) -> np.ndarray:
    """
    Retourne la matrice d'adjacence associée au graphe défini par S et A
    :param sommets: (list) liste des sommets
    :param arcs: (tuple) liste des arcs
    :return: (array) matrice d'adjacence
    """
    if len(sommets) > 1 and len(arcs) > 1:
        result = np.zeros((len(sommets), len(sommets)), dtype=int)
        for row, col in arcs:
            result[row][col] = 1
    else:
        raise ValueError("La liste des sommets et/ou des arcs est vide")
    return result


def matrice_adjacence_pond(sommets: list, arcs: list[tuple[int, int, int]]) -> np.ndarray:
    """
    Retourne la matrice d'adjacence associée au graphe défini par S et A
    :param sommets: (list) liste des sommets
    :param arcs: (tuple) liste des arcs
    :return: (array) matrice d'adjacence
    """
    if len(sommets) > 1 and len(arcs) > 1:
        result = np.zeros((len(sommets), len(sommets)), dtype=int)
        for row, col, poids in arcs:
            result[row][col] = poids
    else:
        raise ValueError("La liste des sommets et/ou des arcs est vide")
    return result


def lire_matrice(nom_fichier: str) -> np.ndarray:
    """
    Lit une matrice carrée dans un fichier texte et retourne la matrice
    :param nom_fichier: (str) nom du fichier
    :return: (array) matrice
    """
    with open(nom_fichier, "r") as file:
        lines = file.readlines()
        no_lines = len(lines)
        matrice = np.zeros((no_lines, no_lines), dtype=int)
        for row in range(no_lines):
            line = lines[row].split()
            for col in range(len(line)):
                matrice[row][col] = line[col]
    return matrice


def liste_sommets(matrice: np.ndarray) -> list:
    """
    Retourne la liste des sommets du graphe associé à la matrice d'adjacence
    :param matrice: (array) matrice d'adjacence
    :return: (list) liste des sommets
    """
    return [i for i in range(matrice.shape[0])]


def liste_arcs(matrice: np.ndarray) -> list[tuple[int, int]]:
    """
    Retourne la liste des arcs associés à la matrice d'adjacence
    :param matrice:
    :return:
    """
    nb_row, nb_col = matrice.shape
    return [(row, col) for row in range(nb_row) for col in range(nb_col) if matrice[row][col] > 0]


def matrice_incidence(matrice: np.ndarray) -> np.ndarray:
    nb_row, nb_col = matrice.shape
    arcs = liste_arcs(matrice)
    len_arcs = len(arcs)
    mat_incidence = np.zeros((nb_row, len_arcs), dtype=int)
    for col in range(len_arcs):
        arc = arcs[col]
        mat_incidence[arc[0]][col] = 1
        mat_incidence[arc[1]][col] = -1
    return mat_incidence


def test():
    # sommets = [0, 1, 2, 3, 4]
    # arcs = [(0, 1, 38), (0, 2, 120), (1, 2, 12), (1, 4, 49), (2, 3, 42), (3, 4, 69), (4, 2, 43)]
    # print(matrice_adjacence_pond(sommets, arcs))

    # Q.4
    mat = lire_matrice("graph0.txt")
    print(mat)
    sommets = liste_sommets(mat)
    print(sommets)
    arcs = liste_arcs(mat)
    print(arcs)

    # Q.6
    print("\nMatrice d'incidence")
    print(matrice_incidence(mat))


test()
