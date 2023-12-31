from random import randint

play_with_comp = ""

# Ask to play against computer or real player
gamemode = True
while gamemode:
    play_with_comp = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? ").upper()
    if play_with_comp == 'O' or play_with_comp == 'N':
        gamemode = False
    else:
        print("Je n'ai pas compris votre réponse")

# Ask name of player 1
player1 = input("Quel est votre nom ? ")
print("Bienvenue ", player1, " nous allons jouer ensemble \n")
player2 = 'Machine'

# Ask name of player 2
if play_with_comp == 'N':
    player2 = input("Quel est le nom du deuxième joueur ? ")
    print("Bienvenue ", player2, " nous allons jouer ensemble \n")

is_playing = True
no_round = 0
score_player1 = 0
score_player2 = 0

while is_playing:
    no_round += 1

    # Validate player1 move
    choice_player1 = ""
    valid_choice = False
    while not valid_choice:
        choice_player1 = input(f"{player1} faîtes votre choix parmi (pierre, papier, ciseaux): ").lower()
        if choice_player1 == 'pierre' or choice_player1 == 'papier' or choice_player1 == 'ciseaux':
            valid_choice = True
        print("Je n'ai pas compris votre réponse")

    # Validate player2 move
    if play_with_comp == 'O':
        choice_player2 = ['pierre', 'papier', 'ciseaux'][randint(0, 2)]
    else:
        choice_player2 = ""
        valid_choice = False
        while not valid_choice:
            choice_player2 = input(f"{player2} faîtes votre choix parmi (pierre, papier, ciseaux): ").lower()
            if choice_player2 == 'pierre' or choice_player2 == 'papier' or choice_player2 == 'ciseaux':
                valid_choice = True
            print("Je n'ai pas compris votre réponse")

    # On affiche les choix de chacun
    print(f"Si on récapitule : {player1} joue {choice_player1} et {player2} joue {choice_player2} \n")

    # On regarde qui a gagné cette manche on calcule les points et on affiche le résultat
    if choice_player1 == choice_player2:
        print("le gagnant est aucun de vous, vous etes a ex æquo")
        print(
            f"Les scores à l'issue de cette manche sont donc {player1}({score_player1}) et {player2}({score_player2}) \n")

    winner = ""
    if ((choice_player1 == 'pierre' and choice_player2 == 'ciseaux')
            or (choice_player1 == 'papier' and choice_player2 == 'pierre')
            or (choice_player1 == 'ciseaux' and choice_player2 == 'papier')):
        score_player1 += 1
        winner = player1
    else:
        score_player2 += 1
        winner = player2

    print("le gagnant est", winner)
    print(f"Les scores à l'issue de cette manche sont donc {player1}({score_player1}) et {player2}({score_player2}) \n")

    # Five round played, the game is over
    if no_round == 5:
        is_playing = False
    else:
        # On propose de continuer ou de s'arrêter
        keep_playing = input(f"Souhaitez vous refaire une partie {player1} contre {player2} ? (O/N) ").upper()
        if keep_playing == 'N':
            is_playing = False
        print("Vous ne répondez pas à la question, on continue ")

print("Merci d'avoir joué ! A bientôt")
