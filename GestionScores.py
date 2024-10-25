from typing import BinaryIO
import pickle
from modules import clear_terminal

class Scores:
    nom : str
    allumettes : int
    devinette : int
    morpion : int
    puissance4 : int

def lecture_Scores(Scores_Jeux : list[Scores]) -> list[Scores]:
    """
    Fonction qui permet d'importer les données du fichier scores.dat

    Entrée : 
        Scores_Jeux (list[Scores]) : Scores des joueurs pour chaque mini jeux 
    Sortie :
        Scores_Jeux (list[Scores]) : Scores des joueurs pour chaque mini jeux 
    """
    fichier : BinaryIO
    fin : bool
    fin = False
    fichier = open("scores.dat","rb")
    while not fin:
        try:
            Scores_Jeux.append(pickle.load(fichier))
        except EOFError:
            fin = True
    fichier.close()
    return Scores_Jeux    

def sauvegarde_scores(Scores_Jeux : list[Scores]):
    """
    Fonction qui permet de sauvegarder les nouveaux score ajouté durant l'exécution du programme dans le fichier scores.dat

    Entrée:
        Scores_Jeux (list[Scores]) : Scores des joueurs pour chaque mini jeux 
    """
    fichier : BinaryIO
    fichier = open("scores.dat","wb")
    for i in range(0,len(Scores_Jeux)):
        pickle.dump(Scores_Jeux[i],fichier)
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
    for i in range(0,len(Scores_Jeux)):
        if Scores_Jeux[i].nom==joueur:
            return i
    return -1

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
        mini_jeu (str) : le nom du mini jeu dans lequel le score doit être modifié
        joueur (str) : le nom du joueur à qui le score doit être modifié
        score (int) : le score à ajouter
    Sortie :
        Scores_Jeux (list[Scores]) : Scores des joueurs pour chaque mini jeux 
    """
    fichier : BinaryIO
    fichier = open("scores.dat","wb")
    indice_joueur : int
    indice_joueur = recherche_indice_joueur(joueur,Scores_Jeux)

    if indice_joueur==-1:
        Scores_Jeux.append(ajout_joueur(joueur))
    indice_joueur = recherche_indice_joueur(joueur,Scores_Jeux)

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
        mini_jeu (str) : nom du mini jeu pour lequel les scores doivent être triés
    Sortie : 
        Scores_Jeux (list[Scores]) : Scores triés des joueurs pour chaque mini jeux 
    """
    p : int
    p = len(Scores_Jeux)-1
    echange : bool
    echange = True
    tmp : Scores
    while echange and p>0:
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
    Fonction qui permet d'afficher les scores des 5 meilleurs joueurs dans chaque mini jeu
    """

    Scores_Jeux = tri_score(Scores_Jeux,"puissance4")
    print("------ Puissance 4 ------")
    for i in range(0,len(Scores_Jeux[slice(5)])):
        print(f"{Scores_Jeux[i].nom} : {Scores_Jeux[i].puissance4}")
    input("Appuyez sur entrée pour afficher la page suivante : ")
    clear_terminal()

    Scores_Jeux = tri_score(Scores_Jeux,"morpion")
    print("------ Morpion ------")
    for i in range(0,len(Scores_Jeux[slice(5)])):
        print(f"{Scores_Jeux[i].nom} : {Scores_Jeux[i].morpion}")
    input("Appuyez sur entrée pour afficher la page suivante : ")
    clear_terminal()

    Scores_Jeux = tri_score(Scores_Jeux,"devinette")
    print("------ Devinettes ------")
    for i in range(0,len(Scores_Jeux[slice(5)])):
        print(f"{Scores_Jeux[i].nom} : {Scores_Jeux[i].devinette}")
    input("Appuyez sur entrée pour afficher la page suivante : ")
    clear_terminal()

    Scores_Jeux = tri_score(Scores_Jeux,"allumettes")
    print("------ Allumettes ------")
    for i in range(0,len(Scores_Jeux[slice(5)])):
        print(f"{Scores_Jeux[i].nom} : {Scores_Jeux[i].allumettes}")

    input("Appuyez sur entrée pour retourner au menu : ")

    