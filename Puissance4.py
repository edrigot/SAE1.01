from modules import afficher_menu_minijeux
from modules import saisir_entier_borne
from modules import remplissage_tab
from modules import affichage_tab
from modules import reste_place
from modules import case_vide
from modules import clear_terminal
from modules import menu_niveau_bot
from modules import menu_bot_joueur
import time
import GestionScores
import random


def ajout_symbole_col(tab : list[list[str]], symbole : str, colonne : int) -> list[list[str]]:
    """
    Fonction qui permet d'ajouter le symbole du joueur à la ligne la plus basse de la colonne

    Entrée :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres utilise pendant la partie en cours qui est donc rempli pour etre utilisable dans les jeux du morpion et de puissance 4
        symbole (str) : symbole du joueur
        colonne (int) : colonne dans laquelle le symbole sera ajoute 
    Sortie :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres avec le symbole qui vient d'être ajoute
    """
    ligne : int
    ligne = 0
    if case_vide(tab,colonne,ligne):
            while case_vide(tab,colonne,ligne+1):
                ligne = ligne + 1
                clear_terminal()
                tab[ligne][colonne]=symbole
                tab[ligne-1][colonne]="-"
                affichage_tab(tab)
                time.sleep(0.1)
                if ligne == 5:
                    break
            clear_terminal()
            tab[ligne][colonne]=symbole
    return tab

def ajout_symbole_p4(joueur : str, tab : list[list[str]], symbole : str) -> list[list[str]]:
    """
    Fonction qui permet au joueur de selectionner une colonne et d'ajouter son symbole si ou moins une case dans la colonne choisi est libre.
    Le symbole est ajouté dans la ligne la plus basse libre.

    Entrée :
        joueur (str) : pseudo du joueur qui va ajouter son symbole
        tab (list[lsit[str]]) : Tableau de chaines de caracteres utilise pendant la partie en cours qui est donc rempli pour etre utilisable dans les jeux du morpion et de puissance 4
        symbole (str) : symbole du joueur
    Sortie :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres avec le symbole qui vient d'être ajoute
    """
    case_libre : bool
    case_libre = False
    colonne : int
    while case_libre == False:
        colonne = saisir_entier_borne(f"{joueur} entrez la colonne : ",1,7,"Veuillez entrer un nombre entre 1 et 7")
        colonne = colonne + (colonne-1)
        tab = ajout_symbole_col(tab,symbole,colonne)
        affichage_tab(tab)
        case_libre = True
        if case_libre==False:
            print("Veuillez choisir une autre colonne ")
    return tab       

def ajout_symbole_bot_p4(tab : list[list[str]], symbole :str, niveau : int, symbole_adv : str) -> list[list[str]]:
    """
    Fonction qui permet à l'ordinateur de placer son symbole sur une des colonnes. L'ordinateur choisit la colonne ou ajouter son symbole en fonction de son niveau (de 1 à 3)

    Entree :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres utilise pendant la partie en cours qui est donc rempli pour etre utilisable dans les jeux du morpion et de puissance 4
        symbole (str) : symbole de l'ordinateur
        niveau (int) : niveau de l'ordinateur
        symbole_adv (str) : symbole de l'adversaire contre qui l'ordinateur joue
    Sortie :
        tab (list[list[str]]) : Tableau de chaines de caracteres avec le symbole qui vient d'être ajouté
    """
    case_libre : bool
    case_libre = False
    colonne : int
    colonne = 0
    if niveau == 1:
        colonne = random.randint(1,7)
        colonne = colonne + (colonne - 1)
        while case_libre == False:
            tab = ajout_symbole_col(tab,symbole,colonne)
            affichage_tab(tab)
            case_libre = True

    elif niveau == 2:
        ajout_n2_p4(tab,symbole)
    elif niveau == 3:
        ajout_n3_p4(tab,symbole,symbole_adv)

    return tab

def ajout_n2_p4(tab : list[list[str]], symbole : str) -> list[list[str]]:
    """
    Fonction qui permet d'ajouter le symbole de l'ordinateur a une colonne proche d'un de ses symboles deja present sur le plateau de jeu.
    Au premier tour, la colonne est choisie aleatoirement en utilisant le niveau 1 de l'ordinateur
    Cette fonction represente le niveau 2 de l'ordinateur

    Entrée :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres utilise pendant la partie en cours qui est donc rempli pour etre utilisable dans les jeux du morpion et de puissance 4
        symbole (str) : symbole de l'ordinateur
    Sortie :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres avec le symbole qui vient d'être ajoute
    """
    col_libres : list[int]
    col_libres = []
    colonne : int
    for i in range(0,6):
        for j in range(1,15,2):
            if tab[i][j] == symbole:
                if i > 0 and tab[i-1][j] == "-":
                    col_libres.append((j))
                if i < len(tab) - 1 and tab[i+1][j] == "-":
                    col_libres.append((j))
                if j > 1 and tab[i][j-2] == "-":
                    col_libres.append((j-2))
                if j < len(tab[i]) - 2 and tab[i][j +2] == "-":
                    col_libres.append((j+2))
                if i > 0 and j > 1 and tab[i-1][j-2] == "-":
                    col_libres.append((j-2))
                if i > 0 and j < len(tab[i]) - 2 and tab[i-1][j+2] == "-":
                    col_libres.append((j+2))
                if i < len(tab) - 1 and j > 1 and tab[i+1][j-2] == "-":
                    col_libres.append((j-2))
                if i < len(tab) - 1 and j < len(tab[i]) - 2 and tab[i+1][j+2] == "-":
                    col_libres.append((j+2))
    if col_libres == []:
        ajout_symbole_bot_p4(tab,symbole,1,"-")
    else:
        colonne = random.choice(col_libres)
        tab = ajout_symbole_col(tab,symbole,colonne)
        affichage_tab(tab)
        return tab
    return tab

def ajout_n3_p4(tab : list[list[str]], symbole : str, symbole_adv : str) -> list[list[str]]:
    """
    Fonction qui permet d'ajouter le symbole de l'ordinateur à une colonne proche d'un de ses symboles deja presents sur le plateau de jeu ou 
        à une colonne pour empecher l'adversaire de gagner la partie.
    Par exemple, si l'adversaire n'a plus qu'un seul symbole à placer pour gagner (horizontalement, verticalement ou en diagonal), 
        la colonne choisie sera celle qui aurait permis à l'adversaire de gagner.
    Cette fonction represente le niveau 3 de l'ordinateur

    Entree :
        tab (list[list[str]]) : Tableau de chaines de caracteres utilise pendant la partie en cours qui est donc rempli pour etre utilisable 
            dans les jeux du morpion et de puissance 4
        symbole (str) : symbole de l'ordinateur
        symbole_adv (str) : symbole de l'adversaire contre qui l'ordinateur joue
    Sortie :
        tab (list[list[str]]) : Tableau de chaines de caracteres avec le symbole qui vient d'être ajoute
    """
    cptr : int
    cptr = 0
    ligne : int
    col : int
    for ligne in range(0,6):
        cptr = 0
        for col in range(1,15,2):
            if tab[ligne][col]==symbole_adv:
                cptr = cptr + 1
            else:
                cptr = 0
            if cptr == 3 and col<=11 and case_vide(tab,col+2,ligne):
                for col2 in range (col,15,2):
                    if case_vide(tab,col2,ligne):
                        tab = ajout_symbole_col(tab,symbole,col2)
                        affichage_tab(tab)
                        return tab
        cptr=0
        for col in range(13,-1,-2):
            if tab[ligne][col]==symbole_adv:
                cptr = cptr + 1
            else:
                cptr = 0
            if cptr == 3 and col>1 and case_vide(tab,col-2,ligne):
                    tab = ajout_symbole_col(tab,symbole,col-2)
                    affichage_tab(tab)
                    return tab       
    for col in range(1,15,2):
        cptr = 0
        for ligne in range(5,-1,-1):
            if tab[ligne][col]==symbole_adv:
                cptr = cptr + 1
            else:
                cptr = 0
            if cptr == 3 and case_vide(tab,col,ligne-1) and ligne>0:
                for ligne2 in range(0,6):
                    if case_vide(tab,col,ligne2):
                        tab = ajout_symbole_col(tab,symbole,col)
                        affichage_tab(tab)
                        return tab
    cptr = 0
    ligne = 0
    col = 0

    for k in range(1,9,2): #diagonale de bas vers haut droite
        for j in range(5,2,-1):
            if tab[j][k]==symbole_adv and tab[j-1][k+2]==symbole_adv and tab[j-2][k+4]==symbole_adv:
                if case_vide(tab,k+6,j-3) and case_vide(tab,k+6,j-2)==False:
                    tab = ajout_symbole_col(tab,symbole,k+6)
                    affichage_tab(tab)
                    return tab
    for k in range(13,5,-2): #diagonale de haut vers bas gauche
        for j in range(0,3):
            if tab[j][k]==symbole_adv and tab[j+1][k-2]==symbole_adv and tab[j+2][k-4]==symbole_adv:
                if j<2 and case_vide(tab,k-6,j-3) and case_vide(tab,k-6,j-4)==False:
                    tab = ajout_symbole_col(tab,symbole,k-6)
                    affichage_tab(tab)
                    return tab
                elif case_vide(tab,k-6,j-3):
                    tab = ajout_symbole_col(tab,symbole,k-6)
                    affichage_tab(tab)
                    return tab
    for k in range(13,5,-2): #diagonale de bas vers haut gauche
        for j in range(5,2,-1):
            if tab[j][k]==symbole_adv and tab[j-1][k-2]==symbole_adv and tab[j-2][k-4]==symbole_adv:
                if case_vide(tab,k-6,j-3) and case_vide(tab,k-6,j-2)==False:
                    tab = ajout_symbole_col(tab,symbole,k-6)
                    affichage_tab(tab)
                    return tab
    for k in range(1,9,2): #diagonale de haut vers bas droite
        for j in range(0,3):
            if tab[j][k]==symbole_adv and tab[j+1][k+2]==symbole_adv and tab[j+2][k+4]==symbole_adv:
                if j<2 and case_vide(tab,k+6,j+3) and case_vide(tab,k+6,j+4)==False:
                    tab = ajout_symbole_col(tab,symbole,k+6)
                    affichage_tab(tab)
                    return tab
                elif case_vide(tab,k+6,j+3):
                    tab = ajout_symbole_col(tab,symbole,k+6)
                    affichage_tab(tab)
                    return tab
                
    ajout_n2_p4(tab,symbole)
    return tab   

def check_colonne_p4(tab : list[list[str]], symbole_joueur : str) -> bool:
    """
    Fonction qui permet de savoir si un joueur a gagne en alignant 4 pions verticalement sur une colonne

    Entree :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres utilise pendant la partie en cours qui est donc rempli pour etre utilisable dans les jeux du morpion et de puissance 4
        symbole_joueur (str) : symbole du joueur 
    Sortie :
        victoire (bool) : Booléen qui retourne "True" si le joueur a gagne et "False" sinon
    """
    victoire : bool
    victoire = False
    cptr : int

    for j in range(1,15,2):
        cptr = 0
        for i in range(5,-1,-1):
            if tab[i][j]==symbole_joueur:
                cptr = cptr + 1
                if cptr == 4:
                    victoire = True
                    return victoire
            else: 
                cptr = 0
    return victoire

def check_ligne_p4(tab : list[list[str]], symbole_joueur : str) -> bool:
    """
    Fonction qui permet de savoir si un joueur a gagne en alignant 4 pions horizontalement sur une ligne

    Entree :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres utilise pendant la partie en cours qui est donc rempli pour etre utilisable dans les jeux du morpion et de puissance 4
        symbole_joueur (str) : symbole du joueur 
    Sortie :
        victoire (bool) : Booleen qui retourne "True" si le joueur a gagne et "False" sinon
    """
    victoire : bool
    victoire = False
    cptr : int

    for j in range(5,-1,-1):
        cptr = 0
        for i in range(1,15,2):
            if tab[j][i]==symbole_joueur:
                cptr = cptr + 1
                if cptr == 4:
                    victoire = True
                    return victoire
            else:
                cptr = 0
    return victoire

def check_diagonale_p4(tab : list[list[str]], symbole_joueur : str) -> bool:
    """
    Fonction qui permet de savoir si un joueur a gagne en alignant 4 pions en diagonal

    Entree :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres utilise pendant la partie en cours qui est donc rempli pour etre utilisable dans les jeux du morpion et de puissance 4
        symbole_joueur (str) : symbole du joueur 
    Sortie :
        victoire (bool) : Booléen qui retourne "True" si le joueur a gagne et "False" sinon
    """
    victoire : bool
    victoire = False
    for i in range(5,4,-1):
        for j in range(1,9,2):
            if tab[i][j]==symbole_joueur and tab[i-1][j+2]==symbole_joueur and tab[i-2][j+4]==symbole_joueur and tab[i-3][j+6]==symbole_joueur:
                victoire = True
                return victoire
        for k in range(7,15,2):
            if tab[i][k]==symbole_joueur and tab[i-1][k-2]==symbole_joueur and tab[i-2][k-4]==symbole_joueur and tab[i-3][k-6]==symbole_joueur:
                victoire = True
                return victoire
    for m in range(0,3,1):
        for n in range(1,9,2):
            if tab[m][n]==symbole_joueur and tab[m+1][n+2]==symbole_joueur and tab[m+2][n+4]==symbole_joueur and tab[m+3][n-6]==symbole_joueur:
                victoire = True
                return victoire
        for o in range(7,15,2):
            if tab[m][o]==symbole_joueur and tab[m+1][o-2]==symbole_joueur and tab[m+2][o-4]==symbole_joueur and tab[m+3][o-6]==symbole_joueur:
                victoire = True
                return victoire
    return victoire
            


def gagnant_p4(tab : list[list[str]], symbole_joueur : str) -> bool:
    """
    Fonction permettant de verifier sur une des conditions de victoire (alignement horizontal, vertical, en diagonal) est vraie

    Entrée :
        tab (list[lsit[str]]) : Tableau de chaines de caracteres utilise pendant la partie en cours qui est donc rempli pour etre utilisable dans les jeux du morpion et de puissance 4
        symbole_joueur (str) : symbole du joueur
    Sortie : 
        est_gagnant (bool) : Booleen qui retourne "True" si une des conditions de victoire est vrai et "False" sinon
    """
    est_gagnant : bool
    est_gagnant = False
    if check_colonne_p4(tab,symbole_joueur) or check_ligne_p4(tab,symbole_joueur) or check_diagonale_p4(tab,symbole_joueur):
        est_gagnant = True
        return est_gagnant
    return est_gagnant

def afficher_regles_p4():
    """
    Fonction qui affiche les regles du puissance 4
    entrée : rien
    sortie : rien
    """
    print(r"""        ____  ____  ___  __    ____  ___        
 ___   (  _ \( ___)/ __)(  )  ( ___)/ __)   ___ 
(___)   )   / )__)( (_-. )(__  )__) \__ \  (___)
       (_)\_)(____)\___/(____)(____)(___/       """)
    
    print("Le but du jeu est d'aligner une suite de 4 pions de meme symbole sur une grille de 6*7")
    print("Tour à tour les joueurs placent un pion dans la colonne de leur choix, le pion coulisse alors jusqu'à la position la plus basse possible")
    print("Le vainqueur est le joueur qui realise le premier un alignement (horizontal, vertical, diagonal) d'au moins 4 pions")
    input("Appuyez sur entree pour retourner au menu : ")

def puissance4(joueur1 : str, joueur2 : str, symbolej1 : str, symbolej2 : str, Scores_Jeux : list[GestionScores.Scores], mode_jeu : int ):
    """
    Procedure qui permet de demarrer le puissance 4, les joueurs jouent chacun leur tour jusqu'à ce que le tableau du jeu soit rempli ou lorsqu'un des joueurs gagne

    Entrée :
        joueur1 (str) : pseudo du joueur 1
        joueur2 (str) : pseudo du joueur 2
        symbolej1 (str) : symbole que le joueur 1 place dans le tableau du jeu
        symbolej2 (str) : symbole que le joueur 2 place dans le tableau du jeu
        Scores_Jeux (list[GestionScores.Scores]) : Scores des joueurs pour chaque mini jeux 
        mode_jeu (int) : mode de jeu pour lequel le jeu sera lancé 
        (1 pour joueur contre joueur, 2 pour joueur contre ordinateur, 3 pour ordinateur contre ordinateur, 0 pour laisser le joueur choisir)
    Sortie : rien
    """
    tab : list[list[str]]
    tab = list([])
    choix : str
    gagnant : str
    gagnant = ""
    perdant = ""
    perdant : str
    existe_gagnant : bool
    existe_gagnant = False
    niveau_bot : int
    niveau_bot = 1

    if mode_jeu == 0:
        mode_jeu = menu_bot_joueur()
    if mode_jeu != 1:
        niveau_bot = menu_niveau_bot()

    tab = remplissage_tab(tab,15,6)
    affichage_tab(tab)
    while existe_gagnant==False and reste_place(tab):
        
        if mode_jeu == 1 or mode_jeu == 2:
            tab = ajout_symbole_p4(joueur1,tab,symbolej1)
            gagnant = joueur1
            if mode_jeu == 2:
                perdant = "bot2"
            else: 
                perdant = joueur2
        if mode_jeu==3:
            tab = ajout_symbole_bot_p4(tab,symbolej1,niveau_bot,symbolej2)
            gagnant = "bot1"
            perdant = "bot2"
        existe_gagnant = gagnant_p4(tab,symbolej1)
        if existe_gagnant==False and reste_place(tab):
            if mode_jeu == 1:
                tab = ajout_symbole_p4(joueur2,tab,symbolej2)
                gagnant = joueur2
                perdant = joueur1
            else : 
                tab = ajout_symbole_bot_p4(tab,symbolej2,niveau_bot,symbolej1)
                gagnant = "bot2"
                if mode_jeu == 2:
                    perdant = joueur1
                else:
                    perdant = "bot1"
            existe_gagnant = gagnant_p4(tab,symbolej2)
        
    if reste_place(tab)==False and existe_gagnant==False:
        print("Egalité")
    else:
        print(f"Le vainqueur est {gagnant} et le perdant est {perdant}")
        if mode_jeu == 1 or (mode_jeu == 2 and gagnant == joueur1):
            Scores_Jeux = GestionScores.ajout_score(Scores_Jeux,"puissance4",gagnant,1)

    choix = input("Voulez vous rejouer contre le même joueur ? O/N : ")
    while choix!="O" and choix!="N" and choix=="":
        print("Veuillez choisir O ou N")
        choix = input("Voulez vous rejouer contre le même joueur ? O/N : ")
    if choix=="O":
        clear_terminal()
        puissance4(joueur1,joueur2,symbolej1,symbolej2,Scores_Jeux,mode_jeu)
    else:
        clear_terminal()
    GestionScores.sauvegarde_scores(Scores_Jeux)

def choix_menu_p4(joueur1 : str, joueur2 : str, Scores_Jeux : list[GestionScores.Scores]):
    """
    Fonction qui permet aux joueurs de choisir une des options du sous-menu du puissance 4.
    Les joueurs peuvent alors lancer une partie, afficher les règles, changer leur symbole ou retourner au menu principal

    Entrée : 
        joueur1 (str) : pseudo du joueur 1
        joueur2 (str) : pseudo du joueur 2
        Scores_Jeux (list[GestionScores.Scores]) : Scores des joueurs pour chaque mini jeux 
    """
    choix : int
    choix = 0
    symbole_j1 : str
    symbole_j1 = "O"
    symbole_j2 : str
    symbole_j2 = "X"
    
    while choix!=4:
        clear_terminal()
        print(r""" ____  __  __  ____  ___  ___    __    _  _  ___  ____     __  
(  _ \(  )(  )(_  _)/ __)/ __)  /__\  ( \( )/ __)( ___)   /. | 
 )___/ )(__)(  _)(_ \__ \\__ \ /(__)\  )  (( (__  )__)   (_  _)
(__)  (______)(____)(___/(___/(__)(__)(_)\_)\___)(____)    (_) """)
        afficher_menu_minijeux()
        choix = saisir_entier_borne("Veuillez saisir votre choix : ",1,4,"Choix indisponible")
        clear_terminal()
        if choix == 1:
            puissance4(joueur1,joueur2,symbole_j1,symbole_j2,Scores_Jeux,0)
        elif choix == 2:
            afficher_regles_p4()
        elif choix == 3:
            print(r"""        ____   __    ____    __    __  __  ____  ____  ____  ____  ___        
 ___   (  _ \ /__\  (  _ \  /__\  (  \/  )( ___)(_  _)(  _ \( ___)/ __)   ___ 
(___)   )___//(__)\  )   / /(__)\  )    (  )__)   )(   )   / )__) \__ \  (___)
       (__) (__)(__)(_)\_)(__)(__)(_/\/\_)(____) (__) (_)\_)(____)(___/       """)
            symbole_j1 = input(f"{joueur1}, entrez votre nouveau symbole : ")
            symbole_j2 = input(f"{joueur2}, entrez votre nouveau symbole : ")
            if symbole_j1 == symbole_j2:
                print("Les symboles doivent être differents")
                symbole_j1 = "O"
                symbole_j2 = "X"
                time.sleep(2)

    GestionScores.sauvegarde_scores(Scores_Jeux)