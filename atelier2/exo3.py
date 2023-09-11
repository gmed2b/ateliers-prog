def separer(lst: list) -> list:
    lsep = []
    idx_inf = 0
    for num in lst:
        if num < 0:
            lsep.insert(0, num)
            idx_inf += 1
        elif num > 0:
            lsep.append(num)
        else:
            lsep.insert(idx_inf, num)
    return lsep


# TEST

l = [-3, 5, -2, 3, 0, -1, 0, 4, -9, 6, 0]

print("Liste initiale:", l)
print("Liste séparée:", separer(l))
