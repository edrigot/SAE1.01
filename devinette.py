from modules import saisir_entier_borne
from modules import afficher_menu_minijeux
from modules import clear_terminal
from modules import menu_bot_joueur
from modules import menu_niveau_bot
import random
import GestionScores

def choix_jeu_bot(niveau : int, nombrechoisi : int, reponse : int , valeur_min : int, valeur_max : int, limite : int):

    """
    fonction qui permet de choisir un nombre en fonction du niveau du bot
    entree : 
        niveau (int) : niveau du bot
        nombrechoisi (int) : nombre choisi par le joueur
        reponse (int) : reponse du joueur
        valeur_min (int) : valeur minimale du nombre choisi par le bot
        valeur_max (int) : valeur maximale du nombre choisi par le bot
    sortie :
            int : nombre choisi par le bot
    """
    if valeur_min == 0:
        valeur_min = 1
    if valeur_max == 0:
        valeur_max = limite
    aleatoire : int
    aleatoire = random.randint(1,2)
    if niveau == 1:
        return random.randint(1,limite)
    elif niveau == 2:
        if aleatoire == 1: 
            return random.randint(1, limite)
        elif aleatoire == 2:
            if reponse == 1:
                if valeur_max - nombrechoisi == 1:
                    return nombrechoisi
                return random.randint(nombrechoisi,valeur_max-1)
            elif reponse == 2:
                if nombrechoisi - valeur_min == 1:
                    return nombrechoisi
                return random.randint(valeur_min+1,nombrechoisi)
    elif niveau == 3:
        if reponse == 1:
            if valeur_max - nombrechoisi == 1:
                return nombrechoisi
            return random.randint(nombrechoisi,valeur_max-1)
        elif reponse == 2:
            if nombrechoisi - valeur_min == 1:
                return nombrechoisi
            return random.randint(valeur_min+1,nombrechoisi)
    return random.randint(valeur_min, valeur_max)
    
def afficher_regles_devinette():
    """
    Fonction qui permet d'afficher les regles du jeu des allumettes
    """
    print(r"""        ____  ____  ___  __    ____  ___        
 ___   (  _ \( ___)/ __)(  )  ( ___)/ __)   ___ 
(___)   )   / )__)( (_-. )(__  )__) \__ \  (___)
       (_)\_)(____)\___/(____)(____)(___/       """)
    print("Le joueur 1 choisi un nombre entre 1 et une limite à decider.")
    print("Le joueur 2 doir deviner ce nombre : à chacune de ses propositions, le joueur 1 répond 'trop petit','trop grand' ou 'c'est gagné'")
    input("Appuyez sur entree pour retourner au menu : ")

def menudevinette(nbtour:int,joueur1:str,joueur2:str,Scores_Jeux : list[GestionScores.Scores]):
    """
    Fonction qui permet aux joueurs de choisir une des options du sous-menu du jeu des devinettes.
    Les joueurs peuvent alors lancer une partie, afficher les regles, changer leur symbole ou retourner au menu principal

    Entrée:
        nbtour (int) : nombre de tour maximum pour laquelle la partie peut durer
        joueur1 (str) : pseudo du joueur 1
        joueur2 (str) : pseudo du joueur 2
        nb_allumettes_depart (int) : nombre d'allumettes disponible lorsque la partie commence
        Scores_Jeux (list[GestionScores.Scores]) : Scores des joueurs pour chaque mini jeux 
    """
    choix:int
    choix=0
    while (choix!=4):
        clear_terminal()
        print(r""" ____  ____  _  _  ____  _  _  ____  ____  ____  ____  ___ 
(  _ \( ___)( \/ )(_  _)( \( )( ___)(_  _)(_  _)( ___)/ __)
 )(_) ))__)  \  /  _)(_  )  (  )__)   )(    )(   )__) \__ \
(____/(____)  \/  (____)(_)\_)(____) (__)  (__) (____)(___/""")
        afficher_menu_minijeux()
        choix=saisir_entier_borne("Veuillez saisir votre choix : ",1,4,"Choix indisponible")
        clear_terminal()
        if (choix==1):
            devinette(nbtour,joueur1,joueur2,Scores_Jeux,0)
        elif (choix==2):
            afficher_regles_devinette()
        elif (choix==3):
            print(r"""        ____   __    ____    __    __  __  ____  ____  ____  ____  ___        
 ___   (  _ \ /__\  (  _ \  /__\  (  \/  )( ___)(_  _)(  _ \( ___)/ __)   ___ 
(___)   )___//(__)\  )   / /(__)\  )    (  )__)   )(   )   / )__) \__ \  (___)
       (__) (__)(__)(_)\_)(__)(__)(_/\/\_)(____) (__) (_)\_)(____)(___/       """)
                
            nbtour=int(input("choisissez le nombre de tour maximum pour la partie : "))


def devinette(nbtour:int,joueur1:str,joueur2:str, Scores_Jeux : list[GestionScores.Scores], mode_jeu : int):
    """
    Fonction qui permet de demarrer le jeu des devinettes, le jeu se termine lorsque le joueur 2 trouve la bon nombre ou lorsque le nombre de tour maxium a ete atteint

    Entrée :
        nbtour (int) : nombre de tour maximum pour laquelle la partie peut durer
        joueur1 (str) : pseudo du joueur 1
        joueur2 (str) : pseudo du joueur 2
        Scores_Jeux (list[GestionScores.Scores]) : Scores des joueurs pour chaque mini jeux 
        mode_jeu (int) : mode de jeu pour lequel le jeu sera lancé (1 pour joueur contre joueur, 2 pour joueur contre ordinateur, 3 pour ordinateur contre ordinateur, 0 pour laisser le joueur choisir)
    """
    nombrechoisi:int
    nombrechoisi=0
    limite:int
    limite=1
    nombredevine:int
    reponse:int
    reponse=0
    choix = str
    gagnant : str
    gagnant = ""
    joueur_ment : bool
    touractuel:int
    touractuel = 1
    valeur_min : int
    valeur_min = 0
    valeur_max : int
    niveau_bot : int = 1
    niveau_bot : int


    if mode_jeu == 0:
        mode_jeu = menu_bot_joueur()
    if mode_jeu != 1:
        niveau_bot = menu_niveau_bot()

    clear_terminal()
    if mode_jeu == 1: 
        limite=saisir_entier_borne(f"{joueur2}, choisissez la limite : ",1,1000,"La limite doit etre comprise entre 1 et 1000")
        nombrechoisi=saisir_entier_borne(f"{joueur1},choisissez le nombre que vous souhaitez faire deviner, entre 1 et {limite}, : ",1,limite,"Le nombre n'est pas l'intervalle")
    elif mode_jeu == 2:
        joueur2="bot2"
        if niveau_bot == 1:
            limite=random.randint(1,50)
        elif niveau_bot == 2:
            limite=random.randint(1,500)
        elif niveau_bot == 3:
            limite=random.randint(1,1000)
        valeur_max = limite
        nombrechoisi=saisir_entier_borne(f"{joueur1},choisissez le nombre que vous souhaitez faire deviner, entre 1 et {limite}, : ",1,limite,"Le nombre n'est pas l'intervalle")
    elif mode_jeu == 3:
        joueur1="bot1"
        joueur2="bot2"
        if niveau_bot == 1:
            limite=random.randint(1,50)
        elif niveau_bot == 2:
            limite=random.randint(1,500)
        elif niveau_bot == 3:
            limite=random.randint(1,1000)
        valeur_max = limite
        nombrechoisi=random.randint(1,limite)

    
    clear_terminal()
    while (touractuel<=nbtour and gagnant==""):
        joueur_ment = True
        if touractuel==1:
            print(f"Vous etes au tour {touractuel} sur {nbtour}")
        else:
            print(f"Vous etes au tour {touractuel} sur {nbtour}")
            if reponse == 1:
                print(f"Au tour precedent, {joueur1} a repondu : trop petit")
            elif reponse == 2:
                print(f"Au tour precedent, {joueur1} a repondu : trop grand")

        if mode_jeu==1:
            nombredevine=saisir_entier_borne(f"{joueur2}, saisissez un nombre : ",1,limite,"Le nombre n'est pas l'intervalle")
        elif mode_jeu==2:
            nombredevine=choix_jeu_bot(niveau_bot,nombrechoisi,reponse,valeur_min,valeur_max,limite)
        else: 
            nombredevine=choix_jeu_bot(niveau_bot,nombrechoisi,reponse,valeur_min,valeur_max,limite)
        
        clear_terminal()
        print(f"{joueur1}, veuillez choisir parmi les choix suivant : ")
        print("1 -- trop petit")
        print("2 -- trop grand")
        print("3 -- c'est gagné")


        while joueur_ment:
            if mode_jeu==1 or mode_jeu == 2:
                reponse=saisir_entier_borne(f"{joueur1}, le nombre {nombredevine}, est-il : ",1,3,"Choix indisponible")
            else:
                if nombredevine > nombrechoisi:
                    reponse=2
                elif nombredevine < nombrechoisi:
                    reponse=1
                elif nombredevine == nombrechoisi:
                    reponse = 3

            if (reponse==1 or reponse==2):
                if reponse==1:
                    valeur_min = nombredevine
                elif reponse == 2:
                    valeur_max = nombredevine
                touractuel = touractuel + 1
                joueur_ment = False
                clear_terminal()
            elif reponse==3:
                if nombrechoisi==nombredevine:
                    print("Bravo, tu as trouvé le bon nombre!!!")
                    gagnant = joueur2
                    joueur_ment = False
                    break
                else:
                    print("Vous ne pouvez pas mentir !!")
                    touractuel = touractuel + 1
    if touractuel>=nbtour:
        print("Le nombre de tour maximum a ete atteint")
        print(f"La partie est termine, {joueur1} a gagne ! ")
        gagnant = joueur1
    else:
        print(f"La partie est termine, {joueur2} a gagne ! ")
        gagnant = joueur2
    

    if mode_jeu == 1 or (mode_jeu == 2 and gagnant == joueur1):
        Scores_Jeux = GestionScores.ajout_score(Scores_Jeux,"devinettes",gagnant,1)
    
    choix = input("Voulez vous rejouer contre le meme joueur ? O/N : ")
    while choix!="O" and choix!="N" and choix=="":
        print("Veuillez choisir O ou N")
        choix = input("Voulez vous rejouer contre le meme joueur ? O/N : ")
    if choix=="O":
        clear_terminal()
        devinette(nbtour,joueur1,joueur2,Scores_Jeux,mode_jeu)
    else:
        clear_terminal()
        



     

    









