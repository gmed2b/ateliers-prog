import numpy as np
from copy import deepcopy


def my_searchsorted(tab: object, elem: int, low: int, high: int) -> int:
    if high < low:
        return -1
    mid = low + (high - low) // 2
    # Check if elem is present at mid
    if tab[mid] == elem:
        return mid
    # search right half
    elif tab[mid] < elem:
        return my_searchsorted(tab, elem, mid + 1, high)
    # search left half
    else:
        return my_searchsorted(tab, elem, low, mid - 1)


def my_where(tab, elem: int) -> tuple:
    result = ([], [])
    row = 0
    col = 0
    for i in tab:
        if tab.ndim > 1:
            for j in i:
                if j == elem:
                    result[0].append(row)
                    result[1].append(col)
                col += 1
        else:
            if i == elem:
                result[0].append(row)
                result[1].append(col)
        row += 1
        col = 0
    return result


def my_add(tab1: np.ndarray, tab2: np.ndarray) -> np.ndarray:
    """
    Additionne deux matrices de même taille
    :param tab1: matrice 1
    :param tab2: matrice 2
    :return: matrice résultat
    """
    if tab1.shape != tab2.shape:
        raise ValueError("Les deux tableaux doivent avoir la même taille")
    result = np.zeros(tab1.shape, dtype=int)
    for row in range(tab1.shape[0]):
        for col in range(tab1.shape[1]):
            result[row][col] = tab1[row][col] + tab2[row][col]
    return result


def test():
    a = np.array([
        [3, 1, 5],
        [6, 4, 2]
    ])
    # print(np.where(a == 2))
    b = np.array([
        [3, 1, 5],
        [6, 4, 2]
    ])
    # print(my_where(b, 2))
    print(my_add(a, b))


test()
