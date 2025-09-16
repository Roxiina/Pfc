from colorama import Fore
import time
from arts import arts_gauche, arts_droite, frames_sync

# ===================== FONCTIONS =====================

def verifier_gagnant(joueur, ordinateur):
    """Détermine le gagnant de la manche"""
    if joueur == ordinateur:
        return "egalite"
    elif (joueur == "pierre" and ordinateur == "ciseaux") or \
         (joueur == "feuille" and ordinateur == "pierre") or \
         (joueur == "ciseaux" and ordinateur == "feuille"):
        return "joueur"
    else:
        return "ordinateur"


def animation_mains():
    """
    Anime les deux mains qui bougent face à face avant le vrai choix.
    """
    for _ in range(2):  
        # for _ in range(2) → répète l’animation 2 fois
        # Le "_" veut dire qu’on n’a pas besoin de la valeur, juste répéter
        for gauche, droite in frames_sync:
            # zip(lignes_gauche, lignes_droite) → permet de parcourir les deux listes de lignes ASCII en parallèle
            lignes_gauche = arts_gauche[gauche].splitlines()  # splitlines → transforme le dessin ASCII en liste ligne par ligne
            lignes_droite = arts_droite[droite].splitlines()

            print(Fore.GREEN + "VOUS".ljust(45) + Fore.MAGENTA + "ORDINATEUR")
            # ljust(45) → aligne le texte à gauche sur 45 caractères (pour espacer les deux mains)

            for l_j, l_o in zip(lignes_gauche, lignes_droite):
                # l_j = une ligne du dessin du joueur
                # l_o = une ligne du dessin de l’ordi
                print(Fore.YELLOW + l_j.ljust(45) + Fore.YELLOW + l_o)

            time.sleep(0.3)              # petite pause → crée l’effet animé
            print("\033[H\033[J", end="")  # efface l’écran avec un code ANSI pour donner l’impression que ça bouge

    print(Fore.CYAN + "Pierre... Feuille... Ciseaux !!!\n")
    time.sleep(0.5)


def afficher_face_a_face(joueur, ordinateur):
    """
    Affiche les choix du joueur et de l’ordinateur en ASCII,
    avec leur nom écrit en dessous.
    """
    lignes_joueur = arts_gauche[joueur].splitlines()
    lignes_ordi = arts_droite[ordinateur].splitlines()

    print(Fore.GREEN + "VOUS".ljust(45) + Fore.MAGENTA + "ORDINATEUR")

    for l_j, l_o in zip(lignes_joueur, lignes_ordi):
        print(Fore.YELLOW + l_j.ljust(45) + Fore.YELLOW + l_o)

    # Ajoute le nom du signe sous la main
    print(Fore.CYAN + joueur.ljust(45) + Fore.MAGENTA + ordinateur)


def afficher_barres(score_joueur, score_ordi):
    """Affiche un classement visuel avec des barres de # représentant les scores"""
    # "#" * score_joueur → répète le caractère # autant de fois que le score
    joueur_barre = "#" * score_joueur
    ordi_barre = "#" * score_ordi
    print(Fore.GREEN + f"Vous      : {joueur_barre} ({score_joueur})")
    print(Fore.RED + f"Ordinateur: {ordi_barre} ({score_ordi})")
    # f"..." → c’est une f-string en Python (format string). 
    # Ça permet d’intégrer directement des variables dans une chaîne de caractères avec {}.