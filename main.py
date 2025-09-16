from colorama import init
from intro import intro_jeu
from joueur import demander_choix
from ordinateur import choix_ordinateur
from game import verifier_gagnant, animation_mains, afficher_face_a_face, afficher_barres
import time     # Sert à gérer le temps (pause, animation) → utilisé avec time.sleep()
from colorama import init, Fore  # Colorama permet d’afficher du texte en couleur dans le terminal

# Initialisation de colorama
# autoreset=True → remet la couleur par défaut après chaque print
init(autoreset=True)

# ===================== FONCTIONS =====================

def jouer_manche():
    """Joue une manche complète"""
    joueur = demander_choix()
    ordinateur = choix_ordinateur()

    print(Fore.MAGENTA + "\nPréparez-vous...")
    # \n = saut de ligne (retour à la ligne avant le texte).
    time.sleep(1)
    animation_mains()

    afficher_face_a_face(joueur, ordinateur)

    gagnant = verifier_gagnant(joueur, ordinateur)

    if gagnant == "egalite":
        print(Fore.BLUE + "\nÉgalité !")
    elif gagnant == "joueur":
    # elif = contraction de else if → “sinon si”
        print(Fore.GREEN + "\nVous gagnez cette manche !")
    else:
    # else en Python veut dire “dans tous les autres cas”
        print(Fore.RED + "\nL'ordinateur gagne cette manche !")

    return gagnant, joueur, ordinateur
    # return sert à renvoyer une valeur


# ===================== BOUCLE PRINCIPALE =====================

def main():
    score_joueur = 0
    score_ordi = 0
    manche = 1
    historique = []  # garde la liste de toutes les manches jouées

    # Intro du jeu
    intro_jeu()  # <-- Appelle la fonction pour montrer pierre vs feuille

    while True:  # boucle principale du jeu
    # while est une boucle qui répète des instructions tant qu’une condition est vraie.
        print(Fore.CYAN + f"\n--- Manche {manche} ---")
        resultat, choix_joueur, choix_ordi = jouer_manche()

        historique.append((choix_joueur, choix_ordi, resultat))  # garde en mémoire
        # append = C’est une méthode des listes en Python.

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