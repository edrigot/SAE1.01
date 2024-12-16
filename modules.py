import os

def saisir_entier_borne(message : str, borneinf : int, bornesup : int, message_erreur : str) -> int:
    """
    Fonction qui permet de saisir un entier compris entre deux valeurs. 
    On affiche un message pour informer l'utilisateur de la valeur à entrer et un message lorsque la valeur n'est pas dans l'intervalle

    Entrée : 
        message (str) : Message pour informer l'utilisateur de ce qu'il doit entrer
        borneinf (int) : Valeur minimum que l'utilisateur peut entrer
        bornesup (int) : Valeur maximum que l'utilisateur peut entrer
        message_erreur (str) : Message lorsque la valeur n'est pas entre les deux bornes
    Sortie :
        val (int) : La valeur qu'a entré l'utilisateur 
    """
    val : int
    val = int(input(message))
    while (val<borneinf) or (val>bornesup):
        print(message_erreur)
        val = int(input(message))
    return val



def afficher_menu_minijeux():
    """
    Procedure permettant d'afficher le sous-menu des mini-jeux
    entree: rien
    sortie: rien
    """
    print("----------------------")
    print("|1 -- Jouer          |")
    print("|2 -- Regles du jeu  |")
    print("|3 -- Parametres     |")
    print("|4 -- Menu principal |")
    print("----------------------")


def remplissage_tab(tab : list[list[str]], nb_colonnes : int, nb_lignes : int) -> list[list[str]]:
    """
    Fonction permettant de préparer un tableau pour les jeux du morpion et du puissance 4
    Le tableau est de taille variable et est sous la forme (pour un tableau de 3 lignes et 3 colones) :
    |-|-|-|
    |-|-|-|
    |-|-|-|
    Entrée : 
        tab (list[list[str]]) : Tableau de chaines de caracteres qui doit être deja declare et initalise avant l'utilisation de la fonction
        nb_colonnes (int) : Le nombre de colonnes du tableau (doit prefarablement etre un nombre impair sinon il ne sera pas "ferme")
        nb_lignes (int) : Le nombre de lignes du tableau 
    Sortie:
        tab (list[lsit[str]]) : Tableau de chaines de caracteres qui est rempli pour etre utilisable dans les jeux du morpion et de puissance 4
    """
    
    for i in range(0,nb_lignes): #pour chaque ligne dans le tableau on ajoute une ligne de "-" et de "|" correspondant à la ligne du tableau
        ligne:list[str]
        ligne=[]
        for j in range(0,nb_colonnes):
            if j==0:
                ligne.append("|")
            else:
                if ligne[j-1]=="|":
                    ligne.append("-")
                else:
                    ligne.append("|")
        tab.append(ligne)
    return tab



def affichage_tab(tab : list[list[str]]):
    """
    Procedure qui permet d'afficher un tableau en revenant à la ligne a chaque fois que les colones d'une lignes sont affiches

    Entrée :
        tab (list[list[str]]) : Tableau de chaines de caracteres qui doit être deja declare et initalise avant l'utilsation de la fonction
    Sortie :
        rien
    """
    for i in range(0,len(tab)):
        for j in range(0,len(tab[i])):
            print(tab[i][j],end=" ")
        print()



def reste_place(tab : list[list[str]]) -> bool:
    """
    Fonction qui permet de savoir s'il reste au moins une case de libre dans un tableau deja rempli pour une utilisation pour le morpion ou le puissance 4
    Une est libre lorsqu'elle contient la chaine de caractere : "-"

    Entrée :
        tab (list[list[str]]) : Tableau de chaines de caracteres qui doit être deja declare et initalise avant l'utilsation de la fonction. 
                                Il doit etre deja rempli pour une utilisation pour le morpion ou le puissance 4 
    Sortie :
        reste_place (bool) : Booleen qui renvoi "True" si au moins une case est vide et "False" sinon 
    """
    reste_place : bool
    reste_place = False
    for i in range(0,len(tab)):
        for j in range(0,len(tab[i])):
            if tab[i][j]=="-":
                reste_place = True
                return reste_place
    return reste_place



def case_vide(tab : list[list[str]], colonne : int, ligne : int) -> bool:
    """
    Fonction permettant de savoir si une case est libre et donc si l'on peut jouer sur cette case

    Entrée :
        tab (list[list[str]]) : Tableau de chaines de caracteres qui doit etre deja declare et initalisz avant l'utilsation de la fonction. 
                                Il doit etre deja rempli pour une utilisation pour le morpion ou le puissance 4 
        colonne (int) : numero de la colonne ou se trouve la case
        ligne (int) : numero de la ligne ou se trouve la case
    Sortie :
        est_vide (bool) : Booleen qui renvoi "True" si la case est vide et "False" sinon 
    """
    est_vide : bool
    est_vide = True
    if tab[ligne][colonne]=="-":
            return est_vide
    else:
        est_vide = False
    return est_vide



def clear_terminal():
    """
    Procédure qu permet de determiner le systeme d'exploitation et d'effectuer la commande approprie pour effacer le terminal
    entrée: rien*
    sortie: rien
    """
    if os.name=='nt':
        os.system("cls")
    else:
        os.system("clear")



def menu_bot_joueur() -> int:
    """
    Fonction qui permet d'afficher le menu pour choisir le mode de jeu pour les jeux contre l'ordinateur
    Entrée : rien
    Sortie : entier correspondant au choix de l'utilisateur
    """
    choix : int
    print(r""" __  __  _____  ____  ____ 
(  \/  )(  _  )(  _ \( ___)
 )    (  )(_)(  )(_) ))__) 
(_/\/\_)(_____)(____/(____)""")
    print("-------------------------------------")
    print("|1 -- Joueur 1 contre joueur 2      |")
    print("|2 -- Joueur 1 contre ordinateur    |")
    print("|3 -- Ordinateur contre ordinateur  |")
    print("-------------------------------------")

    choix = saisir_entier_borne("Entrez votre choix : ",1,3,"Erreur, choix indisponible")
    clear_terminal()
    return choix



def menu_niveau_bot() -> int:
    """
    Fonction qui permet d'afficher le menu pour choisir le niveau de difficulte pour les jeux contre l'ordinateur
    Entrée : rien
    Sortie : entier correspondant au choix de l'utilisateur
    """
    choix : int
    print(r""" ____  ____  ____  ____  ____  ___  __  __  __   ____  ____ 
(  _ \(_  _)( ___)( ___)(_  _)/ __)(  )(  )(  ) (_  _)( ___)
 )(_) )_)(_  )__)  )__)  _)(_( (__  )(__)(  )(__  )(   )__) 
(____/(____)(__)  (__)  (____)\___)(______)(____)(__) (____)""")
    print("-----------------")
    print("|1 -- Facile    |")
    print("|2 -- Moyen     |")
    print("|3 -- Difficile |")
    print("-----------------")

    choix = saisir_entier_borne("Veuillez choisir la difficulte : ",1,3,"Erreur, choix indisponible")
    clear_terminal()
    return choix



def menu_niveau_bot_allumettes() -> int:
    """
    Fonction qui permet d'afficher le menu pour choisir le niveau de difficulte pour le jeu des allumettes contre l'ordinateur
    Entrée : rien
    Sortie : entier correspondant au choix de l'utilisateur
    """
    choix : int
    print(r""" ____  ____  ____  ____  ____  ___  __  __  __   ____  ____ 
(  _ \(_  _)( ___)( ___)(_  _)/ __)(  )(  )(  ) (_  _)( ___)
 )(_) )_)(_  )__)  )__)  _)(_( (__  )(__)(  )(__  )(   )__) 
(____/(____)(__)  (__)  (____)\___)(______)(____)(__) (____)""")
    print("-----------------")
    print("|1 -- Facile     |")
    print("|2 -- Moyen      |")
    print("|3 -- Difficile  |")
    print("|4 -- Impossible |")
    print("-----------------")

    choix = saisir_entier_borne("Veuillez choisir la difficulte : ",1,4,"Erreur, choix indisponible")
    clear_terminal()
    return choix