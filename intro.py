from colorama import Fore
import time

# ===================== FONCTIONS =====================

def intro_jeu():
    """Affiche une intro avec deux mains décoratives"""
    main_gauche = """
       /')    ./')             
      /' /.--''./'')           
 :--''  ;    ''./'')          
 :     '     ''./')             
 :           ''./'             
 :--''-..--''''                   
    """

    main_droite = """
       ('\\.    ('\\
      (''\\.''--.\\ '\\
     (''\\.''    ;  ''-- 
      ('\\.''     '        :
         '\\.''            :
           ''''--..-''-- 
    """

    print(Fore.CYAN + "\n🎮 Pierre ? Feuille ? Ciseaux ? 🎮\n")
    time.sleep(1)
    
    print(Fore.YELLOW + main_gauche)
    print(Fore.YELLOW + main_droite)
    time.sleep(2)
