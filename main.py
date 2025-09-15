import random
import time
from colorama import init, Fore

# Initialisation de colorama pour les couleurs dans le terminal
# (autoreset=True permet de revenir à la couleur par défaut après chaque print)
init(autoreset=True)

# ===================== ASCII ARTS =====================

# Mains du joueur (côté gauche, normales)
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

# Mains de l’ordinateur (côté droit, miroir des gauches pour faire "face à face")
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

# Frames pour l’animation des deux mains avant de révéler les vrais choix
frames_sync = [
    ("pierre", "pierre"),
    ("feuille", "feuille"),
    ("ciseaux", "ciseaux")
]

# ===================== FONCTIONS =====================

def choix_ordinateur():
    """Retourne un choix aléatoire pour l'ordinateur"""
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
    while True:
        choix = input(Fore.CYAN + "Choisissez pierre, feuille ou ciseaux : ").lower()
        if choix in ["pierre", "feuille", "ciseaux"]:
            return choix
        print(Fore.RED + "Entrée invalide, veuillez réessayer.")

def animation_mains():
    """
    Anime les deux mains qui bougent face à face
    (comme si elles se chauffaient avant de jouer).
    """
    for _ in range(2):  # nombre de cycles d'animation
        for gauche, droite in frames_sync:
            # On découpe les ASCII en lignes
            lignes_gauche = arts_gauche[gauche].splitlines()
            lignes_droite = arts_droite[droite].splitlines()

            # Titre au-dessus des mains
            print(Fore.GREEN + "VOUS".ljust(45) + Fore.MAGENTA + "ORDINATEUR")
            
            # Affiche les deux mains côte à côte
            for l_j, l_o in zip(lignes_gauche, lignes_droite):
                print(Fore.YELLOW + l_j.ljust(45) + Fore.YELLOW + l_o)

            time.sleep(0.3)              # petite pause pour donner l’effet animé
            print("\033[H\033[J", end="")  # efface l'écran (ANSI escape code)

    print(Fore.CYAN + "Pierre... Feuille... Ciseaux !!!\n")
    time.sleep(0.5)

def afficher_face_a_face(joueur, ordinateur):
    """
    Affiche les choix du joueur et de l’ordinateur sous forme ASCII,
    avec leur nom écrit juste **en dessous** de la main.
    """
    lignes_joueur = arts_gauche[joueur].splitlines()
    lignes_ordi = arts_droite[ordinateur].splitlines()

    # Titre
    print(Fore.GREEN + "VOUS".ljust(45) + Fore.MAGENTA + "ORDINATEUR")

    # Affichage des mains ASCII
    for l_j, l_o in zip(lignes_joueur, lignes_ordi):
        print(Fore.YELLOW + l_j.ljust(45) + Fore.YELLOW + l_o)

    # Affichage des noms **sous les mains**, une seule fois
    print(Fore.CYAN + joueur.ljust(45) + Fore.MAGENTA + ordinateur)

def afficher_barres(score_joueur, score_ordi):
    """Affiche un classement visuel avec des barres de # représentant les scores"""
    joueur_barre = "#" * score_joueur
    ordi_barre = "#" * score_ordi
    print(Fore.GREEN + f"Vous      : {joueur_barre} ({score_joueur})")
    print(Fore.RED + f"Ordinateur: {ordi_barre} ({score_ordi})")

def jouer_manche():
    """
    Joue une manche complète :
    - demande le choix du joueur
    - génère celui de l’ordinateur
    - lance l’animation
    - affiche les résultats
    """
    joueur = demander_choix()
    ordinateur = choix_ordinateur()

    print(Fore.MAGENTA + "\nPréparez-vous...")
    time.sleep(1)
    animation_mains()  # animation avant révélation

    afficher_face_a_face(joueur, ordinateur)

    gagnant = verifier_gagnant(joueur, ordinateur)

    # Messages selon le résultat
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
    historique = []  # garde en mémoire toutes les manches jouées

    while True:
        print(Fore.CYAN + f"\n--- Manche {manche} ---")
        resultat, choix_joueur, choix_ordi = jouer_manche()

        # Ajoute au suivi de l’historique
        historique.append((choix_joueur, choix_ordi, resultat))

        # Mise à jour des scores
        if resultat == "joueur":
            score_joueur += 1
        elif resultat == "ordinateur":
            score_ordi += 1

        # Affiche le score courant
        print(Fore.CYAN + f"\nScore après manche {manche} :")
        afficher_barres(score_joueur, score_ordi)

        # Demande si le joueur veut continuer
        rejouer = input(Fore.CYAN + "Voulez-vous rejouer ? (oui/non) : ").lower()
        if rejouer != "oui":
            # Résumé final
            print(Fore.MAGENTA + "\n--- Résultat final ---")
            afficher_barres(score_joueur, score_ordi)

            # Historique complet
            print(Fore.CYAN + "\nHistorique des manches :")
            for i, (j, o, r) in enumerate(historique, start=1):
                print(f"Manche {i}: Vous ({j}) vs Ordi ({o}) → {r}")

            # Résultat global
            if score_joueur > score_ordi:
                print(Fore.GREEN + "\nBravo, vous avez gagné la partie ! 🎉")
            elif score_joueur < score_ordi:
                print(Fore.RED + "\nL'ordinateur a gagné la partie ! 🤖")
            else:
                print(Fore.BLUE + "\nÉgalité parfaite ! ⚖️")
            break
        manche += 1
        

# Lancement du jeu
if __name__ == "__main__":
    main()
