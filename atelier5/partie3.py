import numpy as np


def matrice_adjacence(sommets: list, arcs: list[tuple[int, int]]):
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


def matrice_adjacence_pond(sommets: list, arcs: list[tuple[int, int, int]]):
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


def lire_matrice(nom_fichier: str):
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
            no_col = len(line)
            for col in range(no_col):
                matrice[row][col] = line[col]
    return matrice


def test():
    sommets = [0, 1, 2, 3, 4]
    arcs = [(0, 1, 38), (0, 2, 120), (1, 2, 12), (1, 4, 49), (2, 3, 42), (3, 4, 69), (4, 2, 43)]
    print(matrice_adjacence_pond(sommets, arcs))


# test()
print(lire_matrice("graph0.txt"))
