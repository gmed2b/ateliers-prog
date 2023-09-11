def closetozero(lst: list) -> float:
    """
    Renvoie la valeur la plus proche de zero
    :param lst:
    :return:
    """
    numclosetozero = lst[0]
    for num in lst:
        # recherche du plus petit nombre
        if (num < numclosetozero):
            numclosetozero = num
    if numclosetozero < 0:
        for num in lst:
            # recherche du plus grand nombre netant pas superieur a 0
            if (num > numclosetozero and num < 0):
                numclosetozero = num

    return numclosetozero


# TEST

lst = [7, -10, 13, 8, 5, -7.2, -12, -3.7, 3.5, -1.7, 2, 1]
print(closetozero(lst))
