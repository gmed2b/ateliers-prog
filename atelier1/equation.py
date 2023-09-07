from math import sqrt

def discriminant(a: float, b: float, c: float) -> float:
    """Renvoie le discriminant de l'équation ax^2 + bx + c = 0"""
    return b ** 2 - 4 * a * c


def racine_unique(a: float, b: float) -> float:
    """Renvoie la racine unique de l'équation ax + b = 0"""
    if a == 0:
        raise ValueError("/!\\ Division par zéro /!\\")
    return -b / 2 * a


def racine_double(a: float, b: float, delta: float, num: int) -> float:
    """Renvoie la racine double de l'équation ax^2 + bx + c = 0"""
    if num == 1:
        return (-b + sqrt(delta)) / (2 * a)
    else:
        return (-b - sqrt(delta)) / (2 * a)


def str_equation(a: float, b: float, c: float) -> str:
    """Renvoie l'équation ax^2 + bx + c = 0 sous forme de chaîne de caractères"""
    return f"{a}x^2 + {b}x + {c} = 0"


def solution_equation(a: float, b: float, c: float) -> str:
    """Renvoie la solution de l'équation ax^2 + bx + c = 0"""
    print(f"Solution de l'équation {str_equation(a, b, c)} :")
    delta = discriminant(a, b, c)
    if delta < 0:
        return "Pas de racine réelle"
    elif delta == 0:
        return f"Racine unique : x = {racine_unique(a, b)}"
    else:
        return f"Deux racines :\nx1 = {racine_double(a, b, delta, 1)}\nx2 = {racine_double(a, b, delta, 2)}"


def equation(a: float, b: float, c: float) -> None:
    """Affiche la solution de l'équation ax^2 + bx + c = 0"""
    print(solution_equation(a, b, c), "\n")


def test():
    """Fonction de text réalisant plusieurs appels à la fonction equation avec des données pertinentes"""
    test_data = [
        (1, -5, 6),
        (1, -4, 4),
        (1, 2, 5),
        (0, 2, 1)
    ]
    # Bouclez sur la liste de données pour effectuer les tests
    for data in test_data:
        a, b, c = data
        if a == 0:
            print("a = 0, l'équation n'est pas du second degré")
        else:
            equation(a, b, c)


test()
