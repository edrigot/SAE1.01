import random
from modules import saisir_entier_borne
from modules import afficher_menu_minijeux
from modules import clear_terminal
from modules import menu_bot_joueur
from modules import menu_niveau_bot
import GestionScores

def Allumettes(joueur1 : str, joueur2 : str, nb_allumettes_depart : int, Scores_Jeux : list[GestionScores.Scores], mode_jeu : int):
    """
    Fonction qui permet de démarrer le mini jeux des allumettes.
    Les joueurs jouent chacun leur tour jusqu'à ce qu'il n'y est plus d'allumettes.
    A la fin de la partie le joueur a la possibilité de rejouer une partie contre le même joueur

    Entrée :
        joueur1 (str) : pseudo du joueur 1
        joueur2 (str) : pseudo du joueur 2
        nb_allumettes_depart (int) : nombre d'allumettes disponible lorsque la partie commence
        Scores_Jeux (list[GestionScores.Scores]) : Scores des joueurs pour chaque mini jeux 
        mode_jeu (int) : mode de jeu pour lequel le jeu sera lancé (1 pour joueur contre joueur, 2 pour joueur contre ordinateur, 3 pour ordinateur contre ordinateur, 0 pour laisser le joueur choisir)
    """

    nb_allumettes : int
    nb_allumettes = nb_allumettes_depart
    choix : str
    perdant : str
    perdant = ''
    gagnant : str
    gagnant = ''
    niveau_bot : int
    niveau_bot = 1
    if mode_jeu == 0:
        mode_jeu = menu_bot_joueur()
    if mode_jeu != 1:
        niveau_bot = menu_niveau_bot()
        joueur2 = "bot2"

    while nb_allumettes > 0:

        clear_terminal() 
        
        afficher_allumettes(nb_allumettes)

        if mode_jeu == 1 or mode_jeu == 2:
            nb_allumettes = choix_allumettes(nb_allumettes, joueur1)
            gagnant = joueur1
            if mode_jeu == 2:
                perdant = "bot2"
            else: 
                perdant = joueur2
        else:
            nb_allumettes = choix_allumettes_bot(nb_allumettes,niveau_bot)
            perdant = "bot2"
            gagnant = "bot1"

        clear_terminal() 
        
        afficher_allumettes(nb_allumettes)

        if nb_allumettes > 0:
            if mode_jeu == 1:
                nb_allumettes = choix_allumettes(nb_allumettes, joueur1)
                gagnant = joueur2
                perdant = joueur1
            else:
                nb_allumettes = choix_allumettes_bot(nb_allumettes,niveau_bot)
                gagnant = "bot2"
                if mode_jeu == 2:
                    perdant = joueur1
                else:
                    perdant = "bot1"
            clear_terminal()
            print(f"Tour de {joueur2} fini")

    print(f"{perdant} a perdu, dommage")
    print(f"{gagnant} a gagné, bravo")
    Scores_Jeux = GestionScores.ajout_score(Scores_Jeux,"allumettes",gagnant,1)
    choix = input("Voulez vous rejouer contre le même joueur ? O/N : ")
    while choix!="O" and choix!="N" and choix=="":
        print("Veuillez choisir O ou N")
        choix = input("Voulez vous rejouer contre le même joueur ? O/N : ")
    if choix=="O":
        nb_allumettes = nb_allumettes_depart
        clear_terminal()
        Allumettes(joueur1, joueur2, nb_allumettes_depart,Scores_Jeux,mode_jeu)
    else:
        clear_terminal()

def choix_allumettes_bot(nb_allumettes : int, niveau : int) -> int:
    """
    Fonction permettant à l'ordinateur de jouer et de choisir un nombre d'allumettes à retirer. Ce choix se fait en fonction du niveau de l'ordinateur.
    Les niveaux 2 et 3 sont identiques.

    Entrée :
        nb_allumettes (int) : nombre d'allumettes restant pour la partie en cours
        niveau (int) : niveau de l'ordinateur
    Sortie :
        reste_allumettes (int) : Nombre d'allumettes restant pour la partie en cours après avoir retirer le choix de l'ordinateur
    """
    choix : int
    reste_allumettes : int
    reste_allumettes = nb_allumettes
    if niveau == 1:
        choix = random.randint(1,3)
        while choix > reste_allumettes:
            choix = random.randint(1,3)
    else:
        if reste_allumettes > reste_allumettes / 2:
            choix = random.randint(2,3)

        else:
            choix = random.randint(1,2)

    
    reste_allumettes = reste_allumettes - choix
    return reste_allumettes


def choix_allumettes(nb_allumettes : int, joueur : str) -> int:
    """
    Fonction permettant au joueur de choisir le nombre d'allumettes à retirer (entre 1 et 3).

    Entrée:
        nb_allumettes (int) : nombre d'allumettes encore disponible pour la partie
        joueur (str) : pseudo du joueur
    Sortie :
        reste_allumettes (int) : nombre d'allumettes restant après avoir appliquer le choix du joueur
    """
    reste_allumettes : int
    reste_allumettes = nb_allumettes

    choix : int
    choix = 0
    
    choix = saisir_entier_borne(f"{joueur}, entrez le nombre d'allumettes : ",1,3,"Veuillez choisir un nombre compris entre 1 et 3")

    while choix > reste_allumettes:
        print("Vous ne pouvez pas prendre plus d'allumettes qu'il n'en reste")
        choix = saisir_entier_borne(f"{joueur}, entrez le nombre d'allumettes : ",1,3,"Veuillez choisir un nombre compris entre 1 et 3")

    reste_allumettes = reste_allumettes - choix

    return reste_allumettes

def afficher_regles_allumettes(nb_allumettes_depart : int):
    """
    Fonction qui permet d'afficher les règles du jeu des allumettes
    """
    print(f"On dispose d'un tas de {nb_allumettes_depart} d'allumettes.")
    print("Chaque joueur à tour de rôle peut en prélever 1,2 ou 3.")
    print("Le perdant est celui qui prend la dernière allumette.")
    input("Appuyez sur entrée pour retourner au menu : ")

def afficher_allumettes(nb_allumettes : int):
    """
    procédure qui permet dd'afficher le nombre d'allumettes restantes
    """
    compteur_j:int

    for compteur_j in range (nb_allumettes):
        print("\x1b[38;5;196m.",end=" ")
    print("")

    for compteur_j in range (nb_allumettes):
        print("\x1b[38;5;190m|",end=" ")
    print("")
    
    for compteur_j in range (nb_allumettes):
        print("\x1b[38;5;7m",end=" ")
    print("")
        
    print(f"Il reste {nb_allumettes} allumettes")

def choix_menu_allumettes(joueur1 : str, joueur2 : str, nb_allumettes_depart : int, Scores_Jeux : list[GestionScores.Scores]):
    """
    Fonction qui permet aux joueurs de choisir une des options du sous-menu des allumettes.
    Les joueurs peuvent alors lancer une partie, afficher les règles, changer leur symbole ou retourner au menu principal

    Entrée:
        joueur1 (str) : pseudo du joueur 1
        joueur2 (str) : pseudo du joueur 2
        nb_allumettes_depart (int) : nombre d'allumettes disponible lorsque la partie commence
        Scores_Jeux (list[GestionScores.Scores]) : Scores des joueurs pour chaque mini jeux 
    """

    choix : int
    choix = 0
    
    while choix!=4:
        clear_terminal()
            
        print(r"""   __    __    __    __  __  __  __  ____  ____  ____  ____  ___ 
  /__\  (  )  (  )  (  )(  )(  \/  )( ___)(_  _)(_  _)( ___)/ __)
 /(__)\  )(__  )(__  )(__)(  )    (  )__)   )(    )(   )__) \__ \
(__)(__)(____)(____)(______)(_/\/\_)(____) (__)  (__) (____)(___/
""")
        afficher_menu_minijeux()
        choix = saisir_entier_borne("Veuillez saisir votre choix : ",1,4,"Choix indisponible")
        clear_terminal()
        if choix == 1:
            Allumettes(joueur1,joueur2,nb_allumettes_depart,Scores_Jeux,0)
        elif choix == 2:
            afficher_regles_allumettes(nb_allumettes_depart)
        elif choix == 3:
            nb_allumettes_depart = changement_settings_allumettes()    
    
    GestionScores.sauvegarde_scores(Scores_Jeux)

def changement_settings_allumettes() -> int:
    """
    Fonction qui permet de changer le nombre d'alllumettes de départ d'une partie du jeu des allumettes

    Sortie :
        nouvelle_valeur (int) : Le nouveau nombre d'allumettes de départ
    """
    nouvelle_valeur : int
    nouvelle_valeur = saisir_entier_borne("Entrez le nouveau nombre d'allumettes de départ (compris entre 0 et 50) : ",0,50,"Le nombre doit etre entre 0 et 50")
    clear_terminal()
    
    return nouvelle_valeur
   

