import random

NO_MAX_ERROR = 5

LISTE_MOTS = ['python', 'java', 'c++', 'javascript',
              'php', 'ruby', 'perl', 'c#', 'go', 'swift',
              'r', 'matlab', 'sql']

HANGMANPICS = ['''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def places_lettre(ch: str, mot: str) -> list:
    """
    Retourne la liste des positions de la lettre ch dans le mot
    :param ch: (str) caractère à chercher
    :param mot: (str) mot dans lequel chercher
    :return: (list) liste des positions de ch dans le mot
    """
    return [i for i, c in enumerate(mot) if c == ch]


def output_str(mot: str, lpos: list) -> str:
    """
    Retourne une chaine de caractères comprenant
    le mot caché avec des tirets et les lettres trouvées
    :param mot: (str) mot à afficher
    :param lpos: (list) liste des positions des lettres trouvées
    :return: (str) chaine de caractères à afficher
    """
    return ''.join([c if i in lpos else '-' for i, c in enumerate(mot)])


def run_game():
    """
    Fonction principale du jeu
    :return: (None)
    """
    random_mot = random.choice(LISTE_MOTS)
    error = 0
    indices_lettre_trouves = []
    while error < NO_MAX_ERROR and len(indices_lettre_trouves) < len(random_mot):
        print(output_str(random_mot, indices_lettre_trouves))
        lettre = input("Tirer une lettre: ")
        liste_pos = places_lettre(lettre, random_mot)
        if not liste_pos:
            error += 1
            print(HANGMANPICS[error])
            print(f"Il vous reste {NO_MAX_ERROR - error} essais")
        else:
            if liste_pos not in indices_lettre_trouves:
                indices_lettre_trouves += liste_pos

    if error < NO_MAX_ERROR:
        print(f"Le mot est {output_str(random_mot, indices_lettre_trouves)} !")
        print("Vous avez gagné !")
    else:
        print("Vous avez perdu !")


run_game()
