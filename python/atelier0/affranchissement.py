# Ce programme permet de calculer le tarif d'affranchissement
# d'une lettre en fonction de son poids et de son type d'envoi

### FUNCTIONS
def get_affranchissement(poids_lettre: int, type_lettre: str) -> float:
    """Renvoie le tarif d'affranchissement d'une lettre en fonction de son poids et de son type d'envoi"""
    for poids, tarif in AFFRANCHISSEMENT[type_lettre].items():
        if poids_lettre <= poids:
            return tarif
    return 0

### CONSTANTS
AFFRANCHISSEMENT = {
    # Lettre verte
    'V': {
        20: 1.16,
        100: 2.32,
        250: 4,
        500: 6,
        1000: 7.5,
        3000: 10.5
    },
    # Lettre prioritaire
    'P': {
        20: 1.43,
        100: 2.86,
        250: 5.26,
        500: 7.89,
        3000: 11.44
    },
    # Ecopli
    'E': {
        20: 1.14,
        100: 2.28,
        250: 3.92
    }
}

### MAIN

try:
    poids_lettre = int(input("Poids de la lettre en gramme (ex: 120) ? "))
except ValueError:
    print("Le poids de la lettre doit être un nombre entier")
    exit()

type_lettre = ""
# On vérifie que le type d'envoi est valide
while type_lettre not in AFFRANCHISSEMENT:
    type_lettre = input("Type d'envoi: [V]erte, [P]rioritaire ou [E]copli (ex: V) ? ").upper().strip()

montant = get_affranchissement(poids_lettre, type_lettre)
if montant == 0:
    print("Le poids de la lettre est trop élevé pour le type d'envoi choisi")
else:
    print("Le tarif est de", montant, "€")
