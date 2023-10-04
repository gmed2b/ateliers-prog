def est_bissextile(annee: int) -> bool:
    """Permet de savoir si une année est bissextile ou non
    :arg annee: (int) l'année à tester
    :return: (bool) True si l'année est bissextile, False sinon
    """
    result = False
    if (annee % 400 == 0) or (annee % 4 == 0 and annee % 100 != 0):
        result = True
    return result


def test():
    """Test l'execution de la fonction avec des valeurs différentes"""
    test_cases = [
        (2020, True),  # Valid Leap Year
        (2000, True),  # Valid Leap Year
        (2400, True),  # Valid Leap Year (Century Leap Year)
        (2021, False),  # Non-Leap Year
        (1900, False),  # Non-Leap Year (Century Year, Not Divisible by 400)
        (2000, True),  # Leap Year (Century Year, Divisible by 400)
        (-800, True),  # Leap Year (Negative Year)
        (4008, True),  # Leap Year (Random Large Year)
        (1837, False),  # Non-Leap Year (Random Year)
        (1944, True),  # Leap Year (Random Year)
        (1700, False),  # Non-Leap Year (Year Divisible by 100 but Not by 4)
        (1604, True),  # Valid Leap Year (Year Divisible by 4 and Not by 100)
        (1800, False)  # Non-Leap Year (Year Divisible by 100 and 400, but Not by 4)
    ]
    for i in range(len(test_cases)):
        annee = test_cases[i][0]
        print(f"{annee} est {'' if est_bissextile(annee) else 'non '}bissextile")


test()
