from colorama import Fore

# ===================== FONCTIONS =====================

def demander_choix():
    """Demande à l'utilisateur de choisir pierre, feuille ou ciseaux"""
    while True:  # boucle infinie qui continue jusqu’à une entrée valide
        choix = input(Fore.CYAN + "Choisissez pierre, feuille ou ciseaux : ").lower()
        if choix in ["pierre", "feuille", "ciseaux"]:
            return choix
        # Fore.RED → texte rouge
        print(Fore.RED + "Entrée invalide, veuillez réessayer.")
