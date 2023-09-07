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
    """Affiche l'interprétation de l'IMC en
        fonction de sa valeur"""
    if imc <= 0:
        return "IMC invalide"
    for i in range(len(IMC)):
        if imc < IMC[i][0]:
            return IMC[i][1]
    return IMC[len(IMC) - 1][1]


# def message_imc_while(imc: float) -> str:
#     result = IMC[-1][1]
#     i = 0
#     while imc > IMC[i][0] and imc < IMC[i+1][0]:
#         result = IMC[i][1]
#         i += 1
#     return result


def test(x: int) -> None:
    """Test l'execution de la fonction message_imc avec des valeurs différentes"""
    for i in range(x):
        imc = round(uniform(15, 45), 2)
        msg = message_imc(imc)
        print(f"IMC = {imc} -> {msg}")


# get the start time
st = time.time()

test(10)

# get the end time
et = time.time()

# get the execution time
res = et - st
final_res = res * 1000
print('Execution time:', round(final_res, 3), 'ms')