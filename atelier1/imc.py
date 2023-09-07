# Ce programme permet de retourner l'interprétation
# de l'IMC d'une personne

import time
from random import uniform

IMC = [
    (16.5, "dénutrition ou famine"),
    (18.5, "maigreur"),
    (25, "corpulence normale"),
    (30, "surpoids"),
    (35, "obésité modérée"),
    (40, "obésité sévère"),
    (130, "obésité morbide")
]


def message_imc(imc: float) -> str:
    '''Affiche l'interpretation de l'IMC d'une personne
    en fonction de sa valeur.
    :arg imc: (float) L'IMC d'une personne
    :return (str) L'interpretation de l'IMC d'une personne
   '''
    if imc <= 0:
        return "IMC invalide"
    for i in range(len(IMC)):
        if imc < IMC[i][0]:
            return IMC[i][1]
    return IMC[len(IMC) - 1][1]


def test(x: int) -> None:
    '''Test l'execution de la fonction message_imc
    avec des valeurs différentes.
    :arg x: (int) Le nombre de test à effectuer
    :return: None
    '''
    for i in range(x):
        imc = round(uniform(15, 45), 2)
        msg = message_imc(imc)
        print(f"IMC = {imc} -> {msg}")


test(10)
