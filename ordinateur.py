import random

# ===================== FONCTIONS =====================

def choix_ordinateur():
    """Retourne un choix aléatoire pour l'ordinateur"""
    # random.choice → choisit un élément au hasard dans la liste
    return random.choice(["pierre", "feuille", "ciseaux"])