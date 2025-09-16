import random   # Sert à choisir au hasard le coup de l’ordinateur (pierre, feuille ou ciseaux)
import time     # Sert à gérer le temps (pause, animation) → utilisé avec time.sleep()
from colorama import init, Fore  # Colorama permet d’afficher du texte en couleur dans le terminal

# Initialisation de colorama
# autoreset=True → remet la couleur par défaut après chaque print
init(autoreset=True)

# ===================== ASCII ARTS =====================

# ASCII art pour le joueur (à gauche)
arts_gauche = {
    "pierre": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "feuille": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "ciseaux": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

# ASCII art pour l’ordinateur (à droite, miroir des gauches pour qu’elles soient face à face)
arts_droite = {
    "pierre": """
       _______
  (____   '---
 (_____)
 (_____)
  (____)
   (___)__.---
""",
    "feuille": """
       _______
  (____    '---
 (______
(_______
 (_______
   (__________.---
""",
    "ciseaux": """
       _______
  (____   '---
 (______
(__________
     (____)
      (___)__.---
"""
}

# Frames pour l’animation → permet de montrer les mains qui bougent avant de révéler le vrai choix
frames_sync = [
    ("pierre", "pierre"),
    ("feuille", "feuille"),
    ("ciseaux", "ciseaux")
]

# ===================== FONCTIONS =====================

def choix_ordinateur():
    """Retourne un choix aléatoire pour l'ordinateur"""
    # random.choice → choisit un élément au hasard dans la liste
    return random.choice(["pierre", "feuille", "ciseaux"])


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


def demander_choix():
    """Demande à l'utilisateur de choisir pierre, feuille ou ciseaux"""
    while True:  # boucle infinie qui continue jusqu’à une entrée valide
        choix = input(Fore.CYAN + "Choisissez pierre, feuille ou ciseaux : ").lower()
        if choix in ["pierre", "feuille", "ciseaux"]:
            return choix
        # Fore.RED → texte rouge
        print(Fore.RED + "Entrée invalide, veuillez réessayer.")


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


def jouer_manche():
    """Joue une manche complète"""
    joueur = demander_choix()
    ordinateur = choix_ordinateur()

    print(Fore.MAGENTA + "\nPréparez-vous...")
    time.sleep(1)
    animation_mains()

    afficher_face_a_face(joueur, ordinateur)

    gagnant = verifier_gagnant(joueur, ordinateur)

    if gagnant == "egalite":
        print(Fore.BLUE + "\nÉgalité !")
    elif gagnant == "joueur":
        print(Fore.GREEN + "\nVous gagnez cette manche !")
    else:
        print(Fore.RED + "\nL'ordinateur gagne cette manche !")

    return gagnant, joueur, ordinateur


# ===================== BOUCLE PRINCIPALE =====================

def main():
    score_joueur = 0
    score_ordi = 0
    manche = 1
    historique = []  # garde la liste de toutes les manches jouées

    while True:  # boucle principale du jeu
        print(Fore.CYAN + f"\n--- Manche {manche} ---")
        resultat, choix_joueur, choix_ordi = jouer_manche()

        historique.append((choix_joueur, choix_ordi, resultat))  # garde en mémoire

        # Mise à jour du score
        if resultat == "joueur":
            score_joueur += 1
        elif resultat == "ordinateur":
            score_ordi += 1

        print(Fore.CYAN + f"\nScore après manche {manche} :")
        afficher_barres(score_joueur, score_ordi)

        # Demande si on continue ou si on arrête
        rejouer = input(Fore.CYAN + "Voulez-vous rejouer ? (oui/non) : ").lower()
        if rejouer != "oui":
            # Résumé final
            print(Fore.MAGENTA + "\n--- Résultat final ---")
            afficher_barres(score_joueur, score_ordi)

            print(Fore.CYAN + "\nHistorique des manches :")
            for i, (j, o, r) in enumerate(historique, start=1):
                print(f"Manche {i}: Vous ({j}) vs Ordi ({o}) → {r}")

            if score_joueur > score_ordi:
                print(Fore.GREEN + "\nBravo, vous avez gagné la partie ! 🎉")
            elif score_joueur < score_ordi:
                print(Fore.RED + "\nL'ordinateur a gagné la partie ! 🤖")
            else:
                print(Fore.BLUE + "\nÉgalité parfaite ! ⚖️")
            break

        manche += 1


# ===================== LANCEMENT DU JEU =====================
# if __name__ == "__main__": permet de lancer main() uniquement
# si le fichier est exécuté directement, pas si on l’importe.
if __name__ == "__main__":
    main()
