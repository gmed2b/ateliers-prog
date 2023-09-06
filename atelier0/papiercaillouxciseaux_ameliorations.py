import random

# Ask to play against computer or real player
while 1:
    play_with_comp = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? ").upper()
    if play_with_comp != 'O' and play_with_comp != 'N':
        print("Je n'ai pas compris votre réponse")
    else:
        break

# Ask name of each player
if play_with_comp == 'O':
    player2 = 'Machine'
    player1 = input("Quel est votre nom ? ")
    print("Bienvenu ", player1, " nous allons jouer ensemble \n")
else:
    player1 = input("Quel est le nom du premier joueur ? ")
    print("Bienvenu ", player1, " nous allons jouer ensemble")
    player2 = input("Quel est le nom du deuxième joueur ? ")
    print("Bienvenu ", player2, " nous allons jouer ensemble \n")


is_playing = True
no_round = 0
score_player1 = 0
score_player2 = 0

while is_playing:
    no_round += 1

    # Validate player1 move
    valid_move = False
    while valid_move == False:
        move_player1 = input(f"{player1} faîtes votre choix parmi (pierre, papier, ciseaux): ").lower()
        if move_player1 == 'pierre' or move_player1 == 'papier' or move_player1 == 'ciseaux':
            valid_move = True
        print("Je n'ai pas compris votre réponse")

    # Validate player2 move
    if play_with_comp == 'O':
        move_player2 = ['pierre', 'papier', 'ciseaux'][random.randint(0, 2)]
    else:
        valid_move = False
        while valid_move == False:
            move_player2 = input(f"{player2} faîtes votre choix parmi (pierre, papier, ciseaux): ").lower()
            if move_player2 == 'pierre' or move_player2 == 'papier' or move_player2 == 'ciseaux':
                valid_move = True
            print("Je n'ai pas compris votre réponse")

    # On affiche les choix de chacun
    print(f"Si on récapitule : {player1} joue {move_player1} et {player2} joue {move_player2} \n")

    # On regarde qui a gagné cette manche on calcule les points et on affiche le résultat
    if move_player1 == move_player2:
        print("le gagnant est aucun de vous, vous etes a ex æquo")
        print(f"Les scores à l'issue de cette manche sont donc {player1}({score_player1}) et {player2}({score_player2}) \n")

    if move_player1 == 'pierre' and move_player2 == 'papier':
        score_player2 += 1
        print("le gagnant est", player2)
        print(f"Les scores à l'issue de cette manche sont donc {player1}({score_player1}) et {player2}({score_player2}) \n")

    if move_player1 == 'pierre' and move_player2 == 'ciseaux':
        score_player1 += 1
        print("le gagnant est", player1)
        print(f"Les scores à l'issue de cette manche sont donc {player1}({score_player1}) et {player2}({score_player2}) \n")

    if move_player1 == 'papier' and move_player2 == 'ciseaux':
        score_player2 += 1
        print("le gagnant est", player2)
        print(f"Les scores à l'issue de cette manche sont donc {player1}({score_player1}) et {player2}({score_player2}) \n")

    if move_player1 == 'papier' and move_player2 == 'pierre':
        score_player1 += 1
        print("le gagnant est", player1)
        print(f"Les scores à l'issue de cette manche sont donc {player1}({score_player1}) et {player2}({score_player2}) \n")

    if move_player1 == 'ciseaux' and move_player2 == 'pierre':
        score_player2 += 1
        print("le gagnant est", player2)
        print(f"Les scores à l'issue de cette manche sont donc {player1}({score_player1}) et {player2}({score_player2}) \n")

    if move_player1 == 'ciseaux' and move_player2 == 'papier':
        score_player1 += 1
        print("le gagnant est", player1)
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
