import random

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
    random_mot = random.choice(LISTE_MOTS)
    error = 0
    lettre_trouves = []
    while error < 5:
        print(output_str(random_mot, lettre_trouves))
        lettre = input("Tirer une lettre: ")
        liste_pos = places_lettre(lettre, random_mot)
        if not liste_pos:
            error += 1
            print(HANGMANPICS[error])
            print(f"Il vous reste {5 - error} essais")
        else:
            lettre_trouves += liste_pos
    print("Vous avez perdu !")


run_game()