import random

# ----- Fonctions -----

def choix_ordinateur():
    """Retourne un choix aléatoire parmi pierre, feuille, ciseaux"""
    return random.choice(["pierre", "feuille", "ciseaux"])

def verifier_gagnant(joueur, ordinateur):
    """Détermine le gagnant d'une manche"""
    if joueur == ordinateur:
        return "egalite"
    elif (joueur == "pierre" and ordinateur == "ciseaux") or \
         (joueur == "feuille" and ordinateur == "pierre") or \
         (joueur == "ciseaux" and ordinateur == "feuille"):
        return "joueur"
    else:
        return "ordinateur"

def demander_choix():
    """Demande à l'utilisateur son choix et gère les entrées invalides"""
    while True:
        choix = input("Choisissez pierre, feuille ou ciseaux : ").lower()
        if choix in ["pierre", "feuille", "ciseaux"]:
            return choix
        print("Entrée invalide, veuillez réessayer.")

def jouer_manche():
    """Joue une manche et retourne le résultat"""
    joueur = demander_choix()
    ordinateur = choix_ordinateur()
    print(f"L'ordinateur a choisi : {ordinateur}")
    gagnant = verifier_gagnant(joueur, ordinateur)
    
    if gagnant == "egalite":
        print("Égalité !")
    elif gagnant == "joueur":
        print("Vous gagnez cette manche !")
    else:
        print("L'ordinateur gagne cette manche !")
    return gagnant

# ----- Boucle principale -----

def main():
    score_joueur = 0
    score_ordi = 0
    manche = 1
    
    while True:
        print(f"\n--- Manche {manche} ---")
        resultat = jouer_manche()
        
        if resultat == "joueur":
            score_joueur += 1
        elif resultat == "ordinateur":
            score_ordi += 1
        
        print(f"Score : Vous {score_joueur} - {score_ordi} Ordinateur")
        
        rejouer = input("Voulez-vous rejouer ? (oui/non) : ").lower()
        if rejouer != "oui":
            print("\n--- Résultat final ---")
            print(f"Vous {score_joueur} - {score_ordi} Ordinateur")
            if score_joueur > score_ordi:
                print("Bravo, vous avez gagné !")
            elif score_joueur < score_ordi:
                print("L'ordinateur a gagné !")
            else:
                print("Égalité finale !")
            break
        manche += 1

if __name__ == "__main__":
    main()
