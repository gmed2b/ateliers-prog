import copy

import numpy as np


def matrice_carre(n):
    """
    Retourne une matrice carre de n*n
    :param n: (int) taille de la matrice
    :return: (ndarray) matrice
    """
    return np.arange(1, (n * n) + 1).reshape(n, n)


def matrice_add(mat: np.ndarray, n: int) -> np.ndarray:
    """
    Ajoute n à chaque element de la liste
    :param mat: (ndarray) matrice
    :param n: (int) element à additionner
    :return: (ndarray) matrice
    """
    new_mat = copy.deepcopy(mat)
    nb_row, nb_col = mat.shape
    for row in range(nb_row):
        for col in range(nb_col):
            new_mat[row][col] += n
    return new_mat


def matrice_double(mat: np.ndarray) -> np.ndarray:
    """
    Multiplie chaque element de la liste par 2
    :param mat:(ndarray) matrice
    :return: (ndarray) matrice double
    """
    new_mat = copy.deepcopy(mat)
    nb_row, nb_col = mat.shape
    for row in range(nb_row):
        for col in range(nb_col):
            new_mat[row][col] *= 2
    return new_mat


def affiche_ligne_mat(mat: np.ndarray, n: int):
    """
    Affiche la n eme ligne de la matrice
    :param n: (int) numero ligne
    :param mat: (ndarray) matrice
    """
    row = n - 1
    if 0 <= row <= mat.shape[0]:
        print(mat[row])
    else:
        raise ValueError("Le numéro de ligne doit être compris entre 1 et le nombre de ligne de la matrice")


def affiche_col_mat(mat: np.ndarray, n: int):
    """
    Affiche la n eme colonne de la matrice
    :param n: (int) numero colonne
    :param mat: (ndarray) matrice
    """
    selected_col = n - 1
    nb_row, nb_col = mat.shape
    if 0 <= selected_col <= nb_col:
        print(np.array(
            [mat[row][selected_col] for row in range(nb_row) for col in range(nb_col) if col == selected_col]))
    else:
        raise ValueError("Le numéro de colonne doit être compris entre 1 et le nombre de colonne de la matrice")


def extract_mat(mat: np.ndarray, n: int) -> np.ndarray:
    """
    Extraire une sous matrice n*n du coin sup gauche de la matrice
    :param mat: (ndarray) matrice
    :param n: (int) taille sous matrice
    :return: (ndarray) sous matrice
    """
    nb_row, nb_col = mat.shape
    if n >= nb_row:
        raise ValueError("La taille de la sous matrice doit être inférieur au nombre de ligne de la matrice")
    else:
        return mat[:n, :n]


def test():
    mat = matrice_carre(4)
    print(mat)
    mat_4 = matrice_add(mat, 4)
    print(mat_4)
    mat_d = matrice_double(mat_4)
    print(mat_d)
    affiche_ligne_mat(mat_d, 2)
    affiche_col_mat(mat_d, 3)
    sous_mat = extract_mat(mat_d, 2)
    print(sous_mat)


test()
