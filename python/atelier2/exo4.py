import matplotlib.pyplot as plt
import numpy as np


def histo(F: list) -> list:
    """Renvoie une liste d'entier H représentant l'histogramme de F
    :arg F: (list) une liste d'entiers
    :return: (list) une liste d'entiers
    """
    H = []
    len_F = len(F)
    if len_F > 0:
        H = [0] * (max(F) + 1)
        for i in range(len_F):
            H[F[i]] += 1
    return H


def est_injective(F: list) -> bool:
    """Renvoie True si F est injective, False sinon
    :arg F: (list) une liste d'entiers
    :return: (bool)
    """
    result = True
    H = histo(F)
    i = 0
    while i < len(H) and result:
        if H[i] > 1:
            result = False
        i += 1
    return result


def est_surjective(F: list) -> bool:
    """Renvoie True si F est surjective, False sinon
    :arg F: (list) une liste d'entiers
    :return: (bool)
    """
    result = True
    H = histo(F)
    i = 0
    while i < len(H) and result:
        if H[i] < 1:
            result = False
        i += 1
    return result


def est_bijective(F: list) -> bool:
    """Renvoie True si F est bijective, False sinon
    :arg F: (list) une liste d'entiers
    :return: (bool)
    """
    result = True
    H = histo(F)
    i = 0
    while i < len(H) and result:
        if H[i] != 1:
            result = False
        i += 1
    return result


def affiche_histo(F: list) -> None:
    """Affiche une représentation graphique de l'histogramme
    associé à la liste F
    :arg F: (list) une liste d'entiers
    :return: (None)
    """
    H = histo(F)
    length_H = len(H)

    print("TEST HISTOGRAMME")
    print(f"F = {F}")
    print(f"H = {H}")
    print("\nHISTOGRAMME\n")

    if len(H) == 0:
        return None

    MAXOCC = max(H)
    row = MAXOCC
    # Affiche l'histogramme
    while row > -2:
        print("|", end='')
        for col in range(length_H):
            if H[col] >= row > 0:
                print(" # ", end='')
            elif row > 0:
                print("   ", end='')
            elif row == 0:
                print("--|", end='')
            else:
                if col < 10:
                    print(f" {col} ", end='')
                else:
                    print(f"{col} ", end='')
        print("")
        row -= 1


def affiche_histo_plot(F: list) -> None:
    """Affiche une représentation graphique de l'histogramme
    associé à la liste F
    :arg F: (list) une liste d'entiers
    :return: (None)
    """
    plt.hist(F, bins=np.arange(min(F), max(F) + 2) - 0.5, rwidth=0.8)
    plt.show()


def test():
    F = []
    affiche_histo(F)
    print("")
    print(f"est_injective(F) = {est_injective(F)}")
    print(f"est_surjective(F) = {est_surjective(F)}")
    print(f"est_bijective(F) = {est_bijective(F)}")
    # affiche_histo_plot(F)


test()