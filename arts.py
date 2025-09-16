
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
