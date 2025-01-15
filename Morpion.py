from modules import remplissage_tab
from modules import affichage_tab
from modules import reste_place
from modules import case_vide
from modules import saisir_entier_borne
from modules import afficher_menu_minijeux
from modules import clear_terminal
from modules import menu_bot_joueur
from modules import menu_niveau_bot
import random
import GestionScores

def regle_morpion():
    """
    Prodedure qui permet d'afficher les regles du jeu du morpion
    entree : rien
    sortie : rien
    """
    print(r"""        ____  ____  ___  __    ____  ___        
 ___   (  _ \( ___)/ __)(  )  ( ___)/ __)   ___ 
(___)   )   / )__)( (_-. )(__  )__) \__ \  (___)
       (_)\_)(____)\___/(____)(____)(___/       """)
    
    print("Chaque joueur pose sa marque à tour de rôle dans les cases d'une grille de 3*3.")
    print("Le premier qui aligne (verctial, horizontal, diagonal) 3 marques a gagne")
    input("Appuyez sur entree pour retourner au menu : ")

def choix_menu_morpion(joueur1 :str, joueur2 :str, Scores_Jeux : list[GestionScores.Scores]):
    """
    Fonction qui permet aux joueurs de choisir une des options du sous-menu du morpion.
    Les joueurs peuvent alors lancer une partie, afficher les regles, changer leur symbole ou retourner au menu principal

    Entrée:
        joueur1 (str) : pseudo du joueur 1
        joueur2 (str) : pseudo du joueur 2
        Scores_Jeux (list[GestionScores.Scores]) : Scores des joueurs pour chaque mini jeux 
    """
    choix : int
    choix = 0
    symbole_j1 : str
    symbole_j1 = "O"
    symbole_j2 :str
    symbole_j2 = "X"

    while choix != 4:
        print(r""" __  __  _____  ____  ____  ____  _____  _  _ 
(  \/  )(  _  )(  _ \(  _ \(_  _)(  _  )( \( )
 )    (  )(_)(  )   / )___/ _)(_  )(_)(  )  ( 
(_/\/\_)(_____)(_)\_)(__)  (____)(_____)(_)\_)""")
        afficher_menu_minijeux()
        choix = int(input("Veuillez saisir votre choix : "))
        clear_terminal()
        while choix<1 or choix>5:
            print("Choix non disponible")
            choix = int(input("Veuillez saisir votre choix : "))
        if choix == 1:
            morpion(joueur1,joueur2,symbole_j1,symbole_j2,Scores_Jeux,0)
        elif choix == 2:
            regle_morpion()
        elif choix == 3:
            print(r"""        ____   __    ____    __    __  __  ____  ____  ____  ____  ___        
 ___   (  _ \ /__\  (  _ \  /__\  (  \/  )( ___)(_  _)(  _ \( ___)/ __)   ___ 
(___)   )___//(__)\  )   / /(__)\  )    (  )__)   )(   )   / )__) \__ \  (___)
       (__) (__)(__)(_)\_)(__)(__)(_/\/\_)(____) (__) (_)\_)(____)(___/       """)
                
            symbole_j1 = input(f"{joueur1}, entrez votre nouveau symbole : ")
            symbole_j2 = input(f"{joueur2}, entrez votre nouveau symbole : ")

    GestionScores.sauvegarde_scores(Scores_Jeux)




def ajout_symbole(joueur : str, tab : list[list[str]], symbole :str) -> list[list[str]]:
    """
    Fonction qui permet au joueur de selectionner une colonne et une ligne et d'ajouter son symbole si la case choisi est libre

    Entree :
        joueur (str) : pseudo du joueur qui va ajouter son symbole
        tab (list[lsit[str]]) : Tableau de chaines de caracteres utilise pendant la partie en cours qui est donc rempli pour etre utilisable dans les jeux du morpion et de puissance 4
        symbole (str) : symbole du joueur
    Sortie :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres avec le symbole qui vient d'être ajoute
    """
    case_libre : bool
    case_libre = False
    colonne : int
    ligne : int
    while case_libre==False:
        colonne = saisir_entier_borne(f"{joueur} entrez la colonne : ",1,3,"Veuillez entrer un nombre entre 1 et 3")
        colonne = colonne + (colonne-1)
        ligne = saisir_entier_borne(f"{joueur} entrez la ligne : ",1,3,"Veuillez entrer un nombre entre 1 et 3")
        ligne = ligne - 1
        if case_vide(tab,colonne,ligne):
            case_libre = True
            tab[ligne][colonne]=symbole
        else:
            print("Veuillez choisir une autre case ")
    return tab

def ajout_symbole_bot(tab : list[list[str]], symbole :str, niveau : int, symbole_adv : str) -> list[list[str]]:
    """
    Fonction qui permet a l'ordinateur de placer son symbole sur une des cases. L'ordinateur choisit la case ou ajouter son symbole en fonction de son niveau (de 1 à 3)

    Entrée :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres utilise pendant la partie en cours qui est donc rempli pour etre utilisable dans les jeux du morpion et de puissance 4
        symbole (str) : symbole de l'ordinateur
        niveau (int) : niveau de l'ordinateur
        symbole_adv (str) : symbole de l'adversaire contre qui l'ordinateur joue
    Sortie :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres avec le symbole qui vient d'être ajouté
    """
    case_libre : bool
    case_libre = False
    colonne : int
    ligne : int
    colonne = 0
    ligne = 0
    if niveau == 1:
        while case_libre == False:
            colonne = random.randint(1,3)
            ligne = random.randint(1,3)
            colonne = colonne + (colonne-1)
            ligne = ligne - 1
            if case_vide(tab,colonne,ligne):
                case_libre = True
                tab[ligne][colonne]=symbole
    elif niveau == 2:
        ajout_n2(tab,symbole)
    elif niveau == 3:
        ajout_n3(tab,symbole,symbole_adv)
    return tab

def ajout_n3 (tab : list[list[str]], symbole : str, symbole_adv : str) -> list[list[str]]:
    """
    Fonction qui permet d'ajouter le symbole de l'ordinateur a une case proche d'un de ses symboles deja present sur le plateau de jeu ou 
        a une case pour empecher l'adversaire de gagner la partie.
    Par exemple si l'adversaire n'a plus qu'un seul symbole a placer pour gagner (horizontalement, verticalement ou en diagonale), 
        la case choisit sera celle qui aurait permis à l'adversaire de gagner.
    Cette fonction represente le niveau 3 de l'ordinateur

    Entree :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres utilise pendant la partie en cours qui est donc rempli pour etre utilisable 
            dans les jeux du morpion et de puissance 4
        symbole (str) : symbole de l'ordinateur
        symbole_adv (str) : symbole de l'adversaire contre qui l'ordinateur joue
    Sortie :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres avec le symbole qui vient d'etre ajoute
    """
    cptr : int
    cptr = 0
    ligne : int
    col : int
    for ligne in range(0,3):
        cptr = 0
        for col in range(1,7,2):
            if tab[ligne][col]==symbole_adv:
                cptr = cptr + 1
            if cptr == 2:
                for col2 in range(1,7,2):
                    if case_vide(tab,col2,ligne):
                        tab[ligne][col2]=symbole
                        return tab
    for col in range(1,7,2):
        cptr = 0
        for ligne in range(0,3):
            if tab[ligne][col]==symbole_adv:
                cptr = cptr + 1
            if cptr == 2:
                for ligne2 in range(0,3):
                    if case_vide(tab,col,ligne2):
                        tab[ligne2][col]=symbole
                        return tab
    cptr = 0
    ligne = 0
    col = 0
    for i in range(0,3):
        if tab[i][2*i+1]==symbole_adv:
            cptr = cptr + 1
        else:
            ligne = i
            col = 2*i+1
    if cptr == 2 and case_vide(tab,col,ligne):
        tab[ligne][col]=symbole
        return tab
    cptr = 0
    for j in range(0,3):
        if tab[j][-2*j+5]==symbole_adv:
            cptr = cptr + 1
        else:
            ligne = j
            col = -2*j+5
    if cptr == 2 and case_vide(tab,col,ligne):
        tab[ligne][col]=symbole
        return tab

    ajout_n2(tab,symbole)
    return tab   

def ajout_n2(tab : list[list[str]], symbole : str) -> list[list[str]]:
    """
    Fonction qui permet d'ajouter le symbole de l'ordinateur a une case proche d'un de ses symboles deja présent sur le plateau de jeu.
    Cette fonction represente le niveau 2 de l'ordinateur

    Entrée :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres utilise pendant la partie en cours qui est donc rempli pour etre utilisable dans les jeux du morpion et de puissance 4
        symbole (str) : symbole de l'ordinateur
    Sortie :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres avec le symbole qui vient d'être ajoute
    """
    positions_libres : list[tuple[int, int]]
    positions_libres = []
    ligne : int
    colonne : int
    for i in range(0,3):
        for j in range(1,7,2):
            if tab[i][j] == symbole:
                if i > 0 and tab[i-1][j] == "-":
                    positions_libres.append((i-1,j))
                if i < len(tab) - 1 and tab[i+1][j] == "-":
                    positions_libres.append((i+1,j))
                if j > 1 and tab[i][j-2] == "-":
                    positions_libres.append((i,j-2))
                if j < len(tab[i]) - 2 and tab[i][j +2] == "-":
                    positions_libres.append((i,j+2))
                if i > 0 and j > 1 and tab[i-1][j-2] == "-":
                    positions_libres.append((i-1,j-2))
                if i > 0 and j < len(tab[i]) - 2 and tab[i-1][j+2] == "-":
                    positions_libres.append((i-1,j+2))
                if i < len(tab) - 1 and j > 1 and tab[i+1][j-2] == "-":
                    positions_libres.append((i+1,j-2))
                if i < len(tab) - 1 and j < len(tab[i]) - 2 and tab[i+1][j+2] == "-":
                    positions_libres.append((i+1,j+2))
    if positions_libres == []:
        ajout_symbole_bot(tab,symbole,1,"-")
    else:
        ligne, colonne = random.choice(positions_libres)
        tab[ligne][colonne]=symbole
    return tab

def check_ligne(tab : list[list[str]],symbole_joueur : str) -> bool:
    """
    Fonction qui permet de savoir si un joueur a gagne en alignant 3 pions horizontalement sur une ligne
    Entree :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres utilise pendant la partie en cours qui est donc rempli pour etre utilisable dans les jeux du morpion et de puissance 4
        symbole_joueur (str) : symbole du joueur 
    Sortie :
        victoire (bool) : Boolden qui retourne "True" si le joueur a gagne et "False" sinon
    """
    victoire_ligne : bool
    victoire_ligne = False
    for i in range(0,2):
        if tab[i][1]==symbole_joueur and tab[i][3]==symbole_joueur and tab[i][5]==symbole_joueur:
            victoire_ligne = True
            return victoire_ligne
    return victoire_ligne         

def check_colonne(tab : list[list[str]], symbole_joueur : str) -> bool:
    """
    Fonction qui permet de savoir si un joueur a gagné en alignant 3 pions verticalement sur une colonne

    Entree :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres utilisé pendant la partie en cours qui est donc rempli pour etre utilisable dans les jeux du morpion et de puissance 4
        symbole_joueur (str) : symbole du joueur 
    Sortie :
        victoire (bool) : Booleen qui retourne "True" si le joueur a gagne et "False" sinon
    """
    victoire_colonne : bool
    victoire_colonne = False
    for i in range(1,7,2):
        if tab[0][i]==symbole_joueur and tab[1][i]==symbole_joueur and tab[2][i]==symbole_joueur:
            victoire_colonne = True
            return victoire_colonne
    return victoire_colonne   

def check_diagonale(tab : list[list[str]], symbole_joueur : str) -> bool:
    """
    Fonction qui permet de savoir si un joueur a gagne en alignant 3 pions en diagonal

    Entree :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres utilise pendant la partie en cours qui est donc rempli pour etre utilisable dans les jeux du morpion et de puissance 4
        symbole_joueur (str) : symbole du joueur 
    Sortie :
        victoire (bool) : Booleen qui retourne "True" si le joueur a gagne et "False" sinon
    """
    victoire_diagonal : bool
    victoire_diagonal = False
    if tab[0][1]==symbole_joueur and tab[1][3]==symbole_joueur and tab[2][5]==symbole_joueur:
        victoire_diagonal = True
        return victoire_diagonal
    elif tab[2][1]==symbole_joueur and tab[1][3]==symbole_joueur and tab[0][5]==symbole_joueur:
        victoire_diagonal = True
        return victoire_diagonal
    return victoire_diagonal


def gagnant(tab : list[list[str]], symbole_joueur : str) -> bool:
    """
    Fonction permettant de vérifier sur une des conditions de victoire (alignement horizontal, vertical, en diagonal) est vraie

    Entree :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres utilisé pendant la partie en cours qui est donc rempli pour etre utilisable dans les jeux du morpion et de puissance 4
        symbole_joueur (str) : symbole du joueur
    Sortie : 
        est_gagnant (bool) : Booleen qui retourne "True" si une des conditions de victoire est vrai et "False" sinon
    """
    est_gagnant : bool
    est_gagnant = False
    if check_colonne(tab,symbole_joueur) or check_ligne(tab,symbole_joueur) or check_diagonale(tab, symbole_joueur):
        est_gagnant = True
        return est_gagnant
    return est_gagnant
           

def morpion(joueur1 : str, joueur2 : str, symbolej1 : str, symbolej2 :str, Scores_Jeux : list[GestionScores.Scores], mode_jeu : int):
    """
    Fonction qui permet de demarrer le mini jeux du morpion.
    Les joueurs jouent chacun leur tour jusqu'à ce qu'il n'y est plus de place ou qu'un joueur est rempli une condition de victoire.
    A la fin de la partie le joueur a la possibilité de rejouer une partie contre le même joueur

    Entree :
        joueur1 (str) : pseudo du joueur 1
        joueur2 (str) : pseudo du joueur 2
        symbolej1 (str) : symbole du joueur 1
        symbolej2 (str) : symbole du joueur 2
        Scores_Jeux (list[GestionScores.Scores]) : Scores des joueurs pour chaque mini jeux 
        mode_jeu (int) : mode de jeu pour lequel le jeu sera lancé (1 pour joueur contre joueur, 2 pour joueur contre ordinateur, 3 pour ordinateur contre ordinateur, 0 pour laisser le joueur choisir)
    """
    tab : list[list[str]]
    tab = list([])
    j_gagnant : str
    j_perdant : str
    j_perdant = ""
    j_gagnant = ""
    existe_gagnant : bool
    existe_gagnant = False
    niveau_bot : int
    niveau_bot = 1
    if mode_jeu == 0:
        mode_jeu = menu_bot_joueur()
    if mode_jeu != 1:
        niveau_bot = menu_niveau_bot()

    tab = remplissage_tab(tab,7,3)
    affichage_tab(tab)
    while existe_gagnant==False and reste_place(tab):
        if mode_jeu == 1 or mode_jeu == 2: 
            tab=ajout_symbole(joueur1,tab,symbolej1)
            j_gagnant = joueur1
            if mode_jeu == 2:
                j_perdant = "bot2"
            else:
                j_perdant = joueur2
        else:
            tab = ajout_symbole_bot(tab,symbolej1,niveau_bot,symbolej2)
            j_gagnant = "bot1"
            j_perdant = "bot2"
        clear_terminal()
        affichage_tab(tab)
        existe_gagnant = gagnant(tab,symbolej1)
        if existe_gagnant==False and reste_place(tab):
            if mode_jeu == 1:
                tab = ajout_symbole(joueur2,tab,symbolej2)
                j_gagnant = joueur2
                j_perdant = joueur1
            else:
                tab = ajout_symbole_bot(tab,symbolej2,niveau_bot,symbolej1)
                j_gagnant = "bot2"
                if mode_jeu==2:
                    j_perdant = joueur1
                else:
                    j_perdant = "bot1"
            clear_terminal()
            affichage_tab(tab)
            existe_gagnant = gagnant(tab,symbolej2)

    if reste_place(tab)==False and existe_gagnant==False:
        print("Egalite")
    else:
        print(f"{j_gagnant} a gagne!")
        if mode_jeu == 1 or (mode_jeu == 2 and j_gagnant == joueur1):
            Scores_Jeux = GestionScores.ajout_score(Scores_Jeux,"morpion",j_gagnant,1)
    

    choix = input("Voulez vous rejouer contre le meme joueur ? O/N : ") 
    while choix!="O" and choix!="N" and choix=="":
        print("Veuillez choisir O ou N")
        choix = input("Voulez vous rejouer contre le meme joueur ? O/N : ")
    if choix=="O":
        clear_terminal()
        morpion(joueur1,joueur2,symbolej1,symbolej2,Scores_Jeux,mode_jeu)
    else:
        clear_terminal()
    GestionScores.sauvegarde_scores(Scores_Jeux)
