## 🎮 Pierre–Feuille–Ciseaux en Python

Un jeu terminal interactif où le joueur affronte l’ordinateur avec :
- 🎬 Animation des mains (elles bougent avant de révéler le choix)
- ✋🤚 Affichage ASCII des mains face à face
- 📊 Score graphique et historique des manches
- 🔄 Possibilité de rejouer plusieurs manches
- ❌ Gestion des entrées invalides (l’utilisateur doit bien écrire pierre, feuille ou ciseaux)

## ⚡ Fonctionnalités
- Choix du joueur : Pierre, Feuille ou Ciseaux
- Choix de l’ordinateur généré aléatoirement
- Animation “Pierre… Feuille… Ciseaux !!!” avant l’affichage final
- Résultat en ASCII avec les mains affichées côte à côte
- Historique de toutes les manches jouées
- Score mis à jour sous forme de barres #
- Possibilité de rejouer tant que le joueur le souhaite

## 🛠️ Installation
- Cloner le dépôt
git clone <URL_DU_DEPOT>
cd nom_du_projet
- Créer un environnement virtuel
python -m venv .venv


Activer l’environnement
# Windows
.\.venv\Scripts\Activate   

# Linux/Mac
source .venv/bin/activate
Installer la dépendance
pip install colorama

Lancer le jeu
python main.py

## 📄 Explication complète du code
1. Imports et initialisation
- import random
- import time
- from colorama import init, Fore
- random → génère le choix aléatoire de l’ordinateur
- time → permet de mettre des pauses (sleep) pour créer des animations
- colorama → ajoute des couleurs dans le terminal (Fore.RED, Fore.GREEN, etc.)
- init(autoreset=True) → évite de devoir remettre les couleurs par défaut après chaque print

2. ASCII ARTS des mains
- arts_gauche = {...}   # Mains côté joueur
- arts_droite = {...}   # Mains côté ordinateur (inversées)
- arts_gauche → dessins ASCII représentant pierre, feuille, ciseaux pour le joueur (main gauche).
- arts_droite → versions inversées (miroir) pour que les deux mains soient face à face.
- Sans cette inversion, les deux mains pointeraient dans la même direction.

3. Frames pour l’animation
frames_sync = [
    ("pierre", "pierre"),
    ("feuille", "feuille"),
    ("ciseaux", "ciseaux")
]
- Définit les étapes d’animation avant le vrai choix.
- Permet de “faire bouger” les deux mains de façon synchronisée.
- Cela imite le geste qu’on fait en vrai quand on dit : “Pierre, feuille, ciseaux !”

4. Fonctions principales
a) Choix de l’ordinateur
def choix_ordinateur():
    return random.choice(["pierre", "feuille", "ciseaux"])
- Retourne un choix aléatoire dans la liste.

b) Vérification du gagnant
def verifier_gagnant(joueur, ordinateur):
    ...
- Compare les choix du joueur et de l’ordinateur.
- Retourne "joueur", "ordinateur" ou "egalite".

Exemple :
Pierre bat Ciseaux
Feuille bat Pierre
Ciseaux bat Feuille

c) Demande du choix du joueur
def demander_choix():
    ...
- Demande à l’utilisateur d’écrire son choix.
- Boucle while True : tant que l’entrée est invalide → redemande.
- Évite les erreurs si l’utilisateur tape autre chose.

d) Animation des mains
def animation_mains():
    ...
- Affiche les deux mains face à face avec un effet de mouvement.
- Utilise :
- time.sleep(0.3) → pause entre chaque image
- print("\033[H\033[J") → efface l’écran (donne l’impression que les mains bougent)

Termine par le message :
Pierre... Feuille... Ciseaux !!!

e) Affichage face à face final
def afficher_face_a_face(joueur, ordinateur):
    ...
- Affiche les vrais choix du joueur et de l’ordinateur en ASCII.
- Écrit en dessous des mains quel signe a été choisi (pierre, feuille ou ciseaux).

f) Affichage du score
def afficher_barres(score_joueur, score_ordi):
    ...
- Transforme le score en une barre graphique avec des #.

Exemple :
Vous      : ### (3)
Ordinateur: ##  (2)

g) Une manche complète
def jouer_manche():
    ...
Étapes :
- Demande le choix du joueur
- Génère le choix de l’ordinateur
- Lance l’animation
- Affiche les mains réelles
- Détermine et affiche le gagnant

5. Boucle principale main()
def main():
    ...
- Initialise : score joueur, score ordinateur, numéro de manche, historique.

À chaque manche :
- Joue une partie avec jouer_manche()
- Met à jour les scores et l’historique
- Affiche le score avec des barres #
- Demande si le joueur veut rejouer.

## 👉 Si le joueur dit non :
- Affiche le résultat final
- Montre l’historique des manches
- Déclare le gagnant global 🎉

## 🎯 Choix techniques
- Colorama → couleurs claires pour rendre le jeu plus lisible et amusant.
- ASCII art → interface visuelle simple dans un terminal texte.
- Animation avec time.sleep + effacement de l’écran → rend le jeu vivant.
- Historique + barres de score → suivi clair et visuel de la progression.
- Validation des entrées → empêche les bugs liés aux fautes de frappe.