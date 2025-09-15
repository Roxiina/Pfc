# 🎮 Pierre–Feuille–Ciseaux en Python

Un jeu terminal interactif où tu affrontes l’ordinateur avec :
- Animation des mains 🎬  
- Affichage ASCII des mains ✋🤚  
- Score graphique et historique des manches 📊  
- Possibilité de rejouer plusieurs manches 🔄  

---

## ⚡ Fonctionnalités
- Choix du joueur : **Pierre, Feuille, Ciseaux**  
- Choix aléatoire de l’ordinateur  
- Animation “Pierre… Feuille… Ciseaux !!!” avec les deux mains qui bougent  
- Affichage face à face des mains réelles  
- Historique des manches et score mis à jour  
- Gestion des **entrées invalides**  

---

## 🛠️ Installation
1. Cloner le dépôt :  
```bash
git clone <URL_DU_DEPOT>
cd nom_du_projet

Créer et activer l’environnement virtuel :
python -m venv .venv

# Windows
.\.venv\Scripts\Activate   
# Linux/Mac
source .venv/bin/activate

Installer la dépendance :
pip install colorama

Lancer le jeu :
python main.py


## 📄 Explication rapide du code
arts_gauche et arts_droite → dessins ASCII des mains
frames_sync → animation des mains avant le choix final
choix_ordinateur() → choix aléatoire de l’ordinateur
verifier_gagnant() → détermine le gagnant de la manche
demander_choix() → demande et valide le choix du joueur
animation_mains() → anime les deux mains en mouvement
afficher_face_a_face() → montre le résultat final face à fac
afficher_barres() → score visuel avec des #
jouer_manche() → joue une manche complète
main() → boucle principale, gère le score, l’historique et le rejouer

1. Import des modules
import random
import time
from colorama import init, Fore

random → pour choisir aléatoirement la main de l’ordinateur.
time → pour gérer les pauses et les animations.
colorama → pour ajouter des couleurs dans le terminal.

init(autoreset=True) → réinitialise automatiquement les couleurs après chaque print.

2. ASCII ARTS
arts_gauche = {...}
arts_droite = {...}


Contient les dessins ASCII des mains pour le joueur et l’ordinateur.
arts_droite est redessiné pour faire face à face sans déformer les mains.

3. Frames pour animation
frames_sync = [("pierre","pierre"),("feuille","feuille"),("ciseaux","ciseaux")]
Permet de créer une animation des mains qui bougent avant de révéler le vrai choix.

4. Fonctions principales
choix_ordinateur()
Retourne un choix aléatoire parmi ["pierre","feuille","ciseaux"].
verifier_gagnant(joueur, ordinateur)
Compare les choix et retourne : "joueur", "ordinateur" ou "egalite".
demander_choix()
Demande au joueur de saisir son choix.
Gère les entrées invalides avec une boucle while True.
animation_mains()
Anime les deux mains qui bougent face à face.
Utilise time.sleep() pour créer l’effet animé.
Efface l’écran avec print("\033[H\033[J") pour donner l’impression de mouvement.
afficher_face_a_face(joueur, ordinateur)
Affiche les mains réelles après l’animation, avec les titres “VOUS” et “ORDINATEUR”.
afficher_barres(score_joueur, score_ordi)
Affiche une représentation graphique du score avec des #.
Permet de visualiser rapidement qui mène la partie.
jouer_manche()

Gère une manche complète :
Demande le choix du joueur
Choix aléatoire de l’ordinateur
Lance l’animation
Affiche les mains réelles
Détermine le gagnant et retourne le résultat

5. Boucle principale main()
Gère le score total, le nombre de manches, et l’historique.
Affiche le score après chaque manche.
Demande au joueur s’il veut rejouer ou terminer la partie.

À la fin, affiche :
Le résultat final
L’historique des manches
Le gagnant global

Choix techniques
Colorama → pour rendre le jeu plus lisible et attractif.
ASCII art → pour avoir une interface visuelle simple dans le terminal.
Animation → rend le jeu interactif et amusant.
Historique + barres de score → suivi clair de la progression.
Vérification des entrées → empêche les erreurs et rend le jeu robuste.
Améliorations possibles
Ajouter un mode Best of 3/5/7 manches.
Ajouter un compteur de victoires consécutives.
Ajouter un son ou effet sonore à chaque manche.
Créer une interface graphique avec tkinter ou pygame.
Ajouter des animations plus complexes pour les mains.