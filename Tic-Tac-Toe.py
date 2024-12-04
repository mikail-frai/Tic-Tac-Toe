def initialiser_tableau():
    """Crée un tableau de jeu vide (9 cases)"""
    return [" " for _ in range(9)]  


def verifier_victoire(tableau, joueur):
    """Vérifie si un joueur a gagné"""
    combinaisons_gagnantes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]
    ]
    for combi in combinaisons_gagnantes:
        if tableau[combi[0]] == tableau[combi[1]] == tableau[combi[2]] == joueur:
            return True  
    return False  


def verifier_match_nul(tableau):
    """Vérifie si la partie est un match nul"""
    return " " not in tableau  


def afficher_plateau(tableau):
    """Affiche le plateau de jeu"""
    print("\n")
    for i in range(3):
        print(" | ".join(tableau[i*3:(i+1)*3]))
        if i < 2:
            print("-" * 9)
    print("\n")


def jouer_coup(tableau, joueur, position):
    """Permet au joueur de jouer un coup à la position indiquée"""
    if tableau[position] == " ":
        tableau[position] = joueur
        return True
    else:
        print("Cette case est déjà occupée, essayez une autre.")
        return False


def make_move(tableau, joueur):
    """Demande un coup au joueur et le valide"""
    while True:
        try:
            position = int(input(f"Joueur {joueur}, entrez une position (1-9) : ")) - 1
            if position < 0 or position > 8:
                print("Position invalide, veuillez choisir un nombre entre 1 et 9.")
            elif tableau[position] == " ":
                tableau[position] = joueur
                break
            else:
                print("Case déjà prise. Choisissez-en une autre.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entre 1 et 9.")


def switch_player(joueur):
    """Change le joueur actuel"""
    return "O" if joueur == "X" else "X"


def play_game():
    """Boucle principale du jeu"""
    tableau = initialiser_tableau()
    joueur = "X"

    while True:
        afficher_plateau(tableau)
        make_move(tableau, joueur)
        
        if verifier_victoire(tableau, joueur):
            afficher_plateau(tableau)
            print(f"Le joueur {joueur} a gagné!")
            break
        elif verifier_match_nul(tableau):
            afficher_plateau(tableau)
            print("Match nul!")
            break
        
        joueur = switch_player(joueur)


# Lancer le jeu avec une option de rejouer
while True:
    play_game()
    replay = input("Voulez-vous rejouer ? (o/n) : ").lower()
    if replay != 'o':
        break