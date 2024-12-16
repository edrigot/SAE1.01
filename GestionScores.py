from typing import BinaryIO
import pickle
from modules import clear_terminal
import os

class Scores:
    nom : str
    allumettes : int
    devinette : int
    morpion : int
    puissance4 : int

def lecture_Scores(Scores_Jeux : list[Scores]) -> list[Scores]:
    """
    Fonction qui permet d'importer les donnees du fichier scores.dat

    Entrée : 
        Scores_Jeux (list[Scores]) : Scores des joueurs pour chaque mini jeux 
    Sortie :
        Scores_Jeux (list[Scores]) : Scores des joueurs pour chaque mini jeux 
    """
    fichier : BinaryIO
    fin : bool
    if not os.path.exists("scores.dat"):
        with open("scores.dat", "wb") as fichier:
            pickle.dump([], fichier)    
        with open("scores.dat", "wb") as fichier:
            pass
    fin = False
    fichier = open("scores.dat","rb") #on ouvre le fichier en mode lecture binaire
    while not fin:
        try:
            Scores_Jeux.append(pickle.load(fichier))
        except EOFError:
            fin = True
    fichier.close()
    return Scores_Jeux    

def sauvegarde_scores(Scores_Jeux : list[Scores]):
    """
    Fonction qui permet de sauvegarder les nouveaux score ajoute durant l'exécution du programme dans le fichier scores.dat

    Entrée:
        Scores_Jeux (list[Scores]) : Scores des joueurs pour chaque mini jeux 
    Sortie : 
        rien
    """
    fichier : BinaryIO
    fichier = open("scores.dat","wb") #on ouvre le fichier en mode ecriture binaire
    for i in range(0,len(Scores_Jeux)): #on parcourt le tableau des scores pour le sauvegarder
        pickle.dump(Scores_Jeux[i],fichier) #on sauvegarde chaque objet dans le fichier
    fichier.close()

def recherche_indice_joueur(joueur : str, Scores_Jeux : list[Scores]) -> int:
    """
    Fonction permettant de rechercher et de renvoyer la poistion d'un joueur dans le tableau des scores.
    La fonction retourne -1 si le joueur n'existe pas dans le tableau

    Entrée : 
        Scores_Jeux (list[Scores]) : Scores des joueurs pour chaque mini jeux 
    Sortie : 
        int : la position du joueur ou -1 s'il n'existe pas
    """
    for i in range(0,len(Scores_Jeux)): #on parcourt le tableau des scores dans le but de trouver le joueur
        if Scores_Jeux[i].nom==joueur:
            return i #on retourne l'indice du joueur s'il est trouve
    return -1 #on retourne -1 si le joueur n'est pas trouvé

def ajout_joueur(pseudo : str) -> Scores:
    """
    Fonction permettant d'ajouter un joueur avec son pseudo.
    Toutes les valeurs de scores sont mises à 0

    Entrée :
        pseudo (str) : pseudo du nouveau joueur
    Sortie : 
        nouveau_joueur (Scores) : nouveau joueur à ajouter dans le tableau des Scores le programme principal
    """
    nouveau_joueur : Scores
    nouveau_joueur = Scores()
    nouveau_joueur.nom = pseudo
    nouveau_joueur.allumettes = 0
    nouveau_joueur.devinette = 0
    nouveau_joueur.morpion = 0
    nouveau_joueur.puissance4 = 0
    return nouveau_joueur

def ajout_score(Scores_Jeux : list[Scores], mini_jeu : str, joueur : str, score : int) -> list[Scores]:
    """
    Fonction qui permet d'ajouter ou de modifier le score d'un joueur pour un mini jeu en particulier 

    Entrée :
        Scores_Jeux (list[Scores]) : Scores des joueurs pour chaque mini jeux 
        mini_jeu (str) : le nom du mini jeu dans lequel le score doit être modifie
        joueur (str) : le nom du joueur à qui le score doit être modifié
        score (int) : le score à ajouter
    Sortie :
        Scores_Jeux (list[Scores]) : Scores des joueurs pour chaque mini jeux 
    """
    fichier : BinaryIO 
    fichier = open("scores.dat","wb") #on ouvre le fichier en mode écriture binaire
    indice_joueur : int
    indice_joueur = recherche_indice_joueur(joueur,Scores_Jeux) #on cherche l'indice du joueur dans le tableau des scores

    if indice_joueur==-1: #si le joueur n'existe pas on l'ajoute
        Scores_Jeux.append(ajout_joueur(joueur)) 
    indice_joueur = recherche_indice_joueur(joueur,Scores_Jeux) 

    #on ajoute le score en fonction du mini jeu

    if mini_jeu=="allumettes":
        Scores_Jeux[indice_joueur].allumettes += score
    elif mini_jeu=="devinettes":
        Scores_Jeux[indice_joueur].devinette += score
    elif mini_jeu=="morpion":
        Scores_Jeux[indice_joueur].morpion += score
    elif mini_jeu=="puissance4":
        Scores_Jeux[indice_joueur].puissance4 += score

    fichier.close()
    return Scores_Jeux

def tri_score(Scores_Jeux : list[Scores], mini_jeu : str) -> list[Scores]:
    """
    Fonction qui permet de trier les scores du plus grand au plus petit pour un mini jeu en particulier

    Entrée :
        Scores_Jeux (list[Scores]) : Scores des joueurs pour chaque mini jeux 
        mini_jeu (str) : nom du mini jeu pour lequel les scores doivent être tries
    Sortie : 
        Scores_Jeux (list[Scores]) : Scores tries des joueurs pour chaque mini jeux 
    """
    p : int 
    p = len(Scores_Jeux)-1 #on initialise p à la taille du tableau -1
    echange : bool 
    echange = True #on initialise echange à True pour rentrer dans la boucle
    tmp : Scores
    while echange and p>0: #tant qu'il y a eu un échange et que p est supérieur à 0 on continue de trier
        echange = False
        for i in range(0,p):
            if getattr(Scores_Jeux[i], mini_jeu) < getattr(Scores_Jeux[i + 1], mini_jeu):
                tmp = Scores_Jeux[i]
                Scores_Jeux[i] = Scores_Jeux[i+1]
                Scores_Jeux[i+1] = tmp
                echange = True
        p = p-1
    return Scores_Jeux

def afficher_scores(Scores_Jeux : list[Scores]):
    """
    Procedure qui permet d'afficher les scores des 5 meilleurs joueurs dans chaque mini jeu
    Entree : Scores_Jeux (list[Scores]) : Scores des joueurs pour chaque mini jeux 
    Sortie : rien
    """

    Scores_Jeux = tri_score(Scores_Jeux,"puissance4") #on trie les scores pour chaque mini jeu

    print(r"""        ____  __  __  ____  ___  ___    __    _  _  ___  ____     __         
 ___   (  _ \(  )(  )(_  _)/ __)/ __)  /__\  ( \( )/ __)( ___)   /. |    ___ 
(___)   )___/ )(__)(  _)(_ \__ \\__ \ /(__)\  )  (( (__  )__)   (_  _)  (___)
       (__)  (______)(____)(___/(___/(__)(__)(_)\_)\___)(____)    (_)        """)
    for i in range(0,len(Scores_Jeux[slice(5)])): #on affiche les 5 meilleurs scores pour chaque mini jeu
        print(f"{Scores_Jeux[i].nom} : {Scores_Jeux[i].puissance4}") #on affiche le nom du joueur et son score
    input("Appuyez sur entree pour afficher la page suivante : ")
    clear_terminal()

    Scores_Jeux = tri_score(Scores_Jeux,"morpion")
    print(r"""        __  __  _____  ____  ____  ____  _____  _  _        
 ___   (  \/  )(  _  )(  _ \(  _ \(_  _)(  _  )( \( )   ___ 
(___)   )    (  )(_)(  )   / )___/ _)(_  )(_)(  )  (   (___)
       (_/\/\_)(_____)(_)\_)(__)  (____)(_____)(_)\_)       """)
    for i in range(0,len(Scores_Jeux[slice(5)])):
        print(f"{Scores_Jeux[i].nom} : {Scores_Jeux[i].morpion}")
    input("Appuyez sur entree pour afficher la page suivante : ")
    clear_terminal()

    Scores_Jeux = tri_score(Scores_Jeux,"devinette")
    print(r"""        ____  ____  _  _  ____  _  _  ____  ____  ____  ____        
 ___   (  _ \( ___)( \/ )(_  _)( \( )( ___)(_  _)(_  _)( ___)   ___ 
(___)   )(_) ))__)  \  /  _)(_  )  (  )__)   )(    )(   )__)   (___)
       (____/(____)  \/  (____)(_)\_)(____) (__)  (__) (____)       """)
    for i in range(0,len(Scores_Jeux[slice(5)])):
        print(f"{Scores_Jeux[i].nom} : {Scores_Jeux[i].devinette}")
    input("Appuyez sur entree pour afficher la page suivante : ")
    clear_terminal()

    Scores_Jeux = tri_score(Scores_Jeux,"allumettes")
    print(r"""          __    __    __    __  __  __  __  ____  ____  ____  ____  ___        
 ___     /__\  (  )  (  )  (  )(  )(  \/  )( ___)(_  _)(_  _)( ___)/ __)   ___ 
(___)   /(__)\  )(__  )(__  )(__)(  )    (  )__)   )(    )(   )__) \__ \  (___)
       (__)(__)(____)(____)(______)(_/\/\_)(____) (__)  (__) (____)(___/       """)
    for i in range(0,len(Scores_Jeux[slice(5)])):
        print(f"{Scores_Jeux[i].nom} : {Scores_Jeux[i].allumettes}")

    input("Appuyez sur entree pour retourner au menu : ")

    