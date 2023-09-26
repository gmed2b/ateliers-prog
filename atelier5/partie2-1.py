import numpy as np


def matrice(n):
    return np.arange(1, (n * n) + 1).reshape(n, n)


print(matrice(2))
print(matrice(3))
print(matrice(5))
print(matrice(6))
