import Allumettes
import Morpion
import devinette
import Puissance4
from modules import saisir_entier_borne
from modules import clear_terminal
from GestionScores import Scores
from GestionScores import afficher_scores
from GestionScores import lecture_Scores
from GestionScores import sauvegarde_scores

#choix présent sur le menu
menu_options = {
    1:'Changement de pseudo',
    2:'Allumettes',
    3:'Devinettes',
    4:'Morpion',
    5:'Puissance 4',
    6:'Scores',
    7:'Quitter'
}

#imprimer le menu
def afficher_menu():
    """
    Procédure qui permet d'afficher le menu des mini jeux
    Entrée : rien
    Sortie : rien
    """
    print(r""" ____  __      __    _  _  ____  ____ 
(  _ \(  )    /__\  ( \( )( ___)(_  _)
 )___/ )(__  /(__)\  )  (  )__)   )(  
(__)  (____)(__)(__)(_)\_)(____) (__) 
""")
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )


def choix_pseudo(j1 : str, j2 : str) -> str: 
    """
    Fonction permettant aux joueurs de choisir lequel des deux souhaite changer son pseudo

    Entrée: 
        j1 (str) : pseudo du joueur 1
        j2 (str) : pseudo du joueur 2 
        str : retourne le pseudo du joueur qui veut le changer ou "Erreur" si il y a un probleme dans l'execution
    """
    choix_joueur :str
    choix_joueur = input(f"Quel joueur veut changer son pseudo {j1} ou {j2} ?  : ")
    while choix_joueur!=j1 and choix_joueur!=j2:
        print("Erreur de saisie")
        choix_joueur = input(f"Quel joueur veut changer son pseudo {j1} ou  {j2} ?  : ")
    if choix_joueur==j1:
        return j1
    elif choix_joueur==j2:
        return j2
    return "Erreur"

if __name__=="__main__":
    joueur1:str
    joueur2:str
    nb_allumettes_depart : int
    nb_allumettes_depart = 20
    nbtour : int
    nbtour = 20
    choix_menu : int
    choix_menu = 0
    Scores_Jeux : list[Scores]
    Scores_Jeux = []

    Scores_Jeux = lecture_Scores(Scores_Jeux)
    sauvegarde_scores(Scores_Jeux)
    clear_terminal()
    joueur1=input("Joueur 1-Quel est votre pseudo? : ")
    while joueur1=="":
        print("Veuillez entrer un pseudo")
        joueur1=input("Joueur 1-Quel est votre pseudo?: ")
    joueur2=input("Joueur 2-Quel est votre pseudo? : ")
    while joueur2=="" or joueur2==joueur1:
        print("Veuillez entrer un pseudo different du joueur 1")
        joueur2=input("Joueur 2-Quel est votre pseudo? : ")

    while choix_menu != 7:
        clear_terminal()
        afficher_menu() #affiche le menu et permet de faire choisir une option à l'utilisateur
        choix_menu = saisir_entier_borne("Veuillez saisir votre choix : ",1,7,"Choix indisponible")
        clear_terminal()

        #selon les choix de l'utilisateur, on lance le jeu/l'option correspondant

        if choix_menu == 1: 
            if choix_pseudo(joueur1, joueur2)==joueur1: #change le pseudo du joueur1
                joueur1=input(f"{joueur1}, quel sera ton nouveau pseudo ? : ")
                print("Changement enregistre !")
            else: #change le pseudo du joueur2
                joueur2=input(f"{joueur2}, quel sera ton nouveau pseudo ? : ")
                print("Changement enregistre !")
        elif choix_menu == 2: 
            Allumettes.choix_menu_allumettes(joueur1,joueur2,nb_allumettes_depart,Scores_Jeux)
        elif choix_menu == 3:
            clear_terminal()
            devinette.menudevinette(nbtour,joueur1,joueur2,Scores_Jeux)
        elif choix_menu == 4:
            Morpion.choix_menu_morpion(joueur1,joueur2,Scores_Jeux)
        elif choix_menu == 5:
            Puissance4.choix_menu_p4(joueur1,joueur2,Scores_Jeux)
        elif choix_menu == 6:
            afficher_scores(Scores_Jeux)
        
    sauvegarde_scores(Scores_Jeux)


    

