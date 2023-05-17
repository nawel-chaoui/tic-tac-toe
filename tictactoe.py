#  __  __                  _                _____                             _ 
# |  \/  |                (_)              / ____|                           | |
# | \  / | ___  _ __ _ __  _  ___  _ __   | |  __  __ _ _ __ ___   ___  ___  | |
# | |\/| |/ _ \| '__| '_ \| |/ _ \| '_ \  | | |_ |/ _` | '_ ` _ \ / _ \/ __| | |
# | |  | | (_) | |  | |_) | | (_) | | | | | |__| | (_| | | | | | |  __/\__ \ |_|
# |_|  |_|\___/|_|  | .__/|_|\___/|_| |_|  \_____|\__,_|_| |_| |_|\___||___/ (_)
#                   | |                                                         
#                   |_|    

################ Importation des modules ################ 
from tkinter import *
import tkinter.messagebox


################ Définition des variables globales ################ 
cases=[ [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
drapeau = True                              # True pour les croix, False pour les ronds
n = 1                                       # Numéro du tour de jeu


################  Définition des Fonctions ################ 
def afficher(event) :
    """ Entrées : Un événement de la souris
        Sortie : Affiche en temps réel les coordonnées de la case du clic de souris"""
    global drapeau, cases, n
    l = (event.y-2)//100                    # Ligne du clic
    c = (event.x-2)//100                    # Colonne du clic

    if (n < 10) and (cases[l][c] == 0):
        if drapeau:                              # drapeau == True
            dessin.create_line(100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, fill = 'black')
            dessin.create_line(100*c+8, 100*l+96, 100*c+96, 100*l+8, width = 5, fill = 'black')
            cases[l][c] = 1
            message.configure(text='Tour de O',font=('Showcard Gothic',30), fg='#FFFFFF')

        else:
            dessin.create_oval(100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, outline = 'red')
            cases[l][c] = -1
            message.configure(text='Tour de X',font=('Showcard Gothic',30), fg='#000000')
            

        drapeau = not(drapeau)
        if (n >= 5) and (n <= 9):
            somme = verif(cases)
            if somme == 1 or somme == -1:
                n = gagner(somme)
            elif n == 9:
                n = gagner(0)
        n += 1


def verif(tableau):
    sommes = [0,0,0,0,0,0,0,0]             # Il y a 8 sommes à vérifier
    # Les lignes :
    sommes[0] = sum(tableau[0])
    sommes[1] = sum(tableau[1])
    sommes[2] = sum(tableau[2])
    # Les colonnes
    sommes[3] = tableau[0][0]+tableau[1][0]+tableau[2][0]
    sommes[4] = tableau[0][1]+tableau[1][1]+tableau[2][1]
    sommes[5] = tableau[0][2]+tableau[1][2]+tableau[2][2]
    # Les diagonales
    sommes[6] = tableau[0][0]+tableau[1][1]+tableau[2][2]
    sommes[7] = tableau[0][2]+tableau[1][1]+tableau[2][0]

    for i in range(8):                     # Parcours des sommes
        if sommes[i] == 3:
            return 1
        elif sommes[i] == -3:
            return -1
    return 0


def gagner(a):
    if a == 1:
        message.configure(text = 'X GAGNE !', font=('Showcard Gothic',30), fg='#FFFF00', bg='#FF0921')
    elif a == -1:
        message.configure(text = 'O GAGNE !', font=('Showcard Gothic',30), fg='#FFFF00', bg='#FF0921')
    elif a == 0:
        message.configure(text = 'Match nul !', font=('Showcard Gothic',30), fg='#FFFF00', bg='#FF0921')
    return 9


def reinit():
    """Cette fonction ré-initialise les variables globales."""
    global drapeau, cases, n
    cases = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    drapeau = True          # True pour les croix, False pour les ronds
    n = 1

    message.configure(text='Tour de X',font=('Showcard Gothic',30), fg='#000000')
    dessin.delete(ALL)      # Efface toutes les figures
    lignes = []
    for i in range(4):  
      lignes.append(dessin.create_line(0, 100*i+2, 303, 100*i+2, width=3))
      lignes.append(dessin.create_line(100*i+2, 0, 100*i+2, 303, width=3))


def create():
    win = Toplevel(fen)
    win.iconbitmap("tictactoe.ico")
    win.configure(bg='#FF0921')
    win.resizable(width=False, height=False)
    label_title = Label(win, text="Règles du jeu ! ", font=("showcard gothic", 20), bg='#FF0921', fg='black')
    label_title.pack(pady=10)

    label_rules = Label(win, text="Vous devez aligner 3 symboles identiques (X ou O).", font=("impact", 14), bg='#FF0921', fg='white')
    label_rules2 = Label(win, text="En ligne, colonne ou en diagonale. Tour par tour, vous placez un symbole.", font=("impact", 14), bg='#FF0921', fg='white')
    label_rules3 = Label(win, text="Si toutes les cases sont cochées et qu'il n'y a pas de gagnant, ça sera match nul.", font=("impact", 14), bg='#FF0921', fg='white') 
    label_rules.pack(padx=20, pady=10)
    label_rules2.pack(padx=20, pady=10)
    label_rules3.pack(padx=20, pady=10)



def vs_ia():  #pas réussit à implenter
    reinit()
    
    
    

def versus_joueur(): # reset le plateau
    reinit()



################ Création et configuration de la fenêtre ################ 
fen = Tk()
fen.configure(bg='#FF0921')
fen.iconbitmap("tictactoe.ico")
fen.title("Tik..Tak..TOE ! ")
fen.resizable(width=False, height=False)


################ Création des zones de texte ################ 
message=Label(fen, text='Tour de X', font=('Showcard Gothic',30), fg='#000000', bg='#FF0921')
message.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3, sticky = W+E)


################ Création des boutons ################ 
bouton_quitter = Button(fen, text='Quitter', font=('Showcard Gothic',10), fg='#000000', bg='#FF0921', command=fen.destroy)
bouton_quitter.grid(row = 3, column = 1, padx=3, pady=3, sticky = S+W+E)

bouton_ia = Button(fen, text='versus IA', font=('Showcard Gothic',10), fg='#000000', bg='#FF0921', command=vs_ia)
bouton_ia.grid(row = 2, column = 0, padx=3, pady=3, sticky = S+W+E)

bouton_rules = Button(fen, text='règles', font=('Showcard Gothic',10), fg='#000000', bg='#FF0921', command=create)
bouton_rules.grid(row = 2, column = 1, padx=3, pady=3, sticky = S+W+E)

bouton_reload = Button(fen, text='versus joueur', font=('Showcard Gothic',10), fg='#000000', bg='#FF0921', command=versus_joueur)
bouton_reload.grid(row = 3, column = 0, padx=3, pady=3, sticky = S+W+E)


################ Création du canevas ################ 
dessin=Canvas(fen, bg="white", width=301, height=301)
dessin.grid(row = 1, column = 0, columnspan = 2, padx=5, pady=5)


################ La grille ################ 
lignes = []


################ Evenements ################ 
dessin.bind('<Button-1>', afficher)


################ Programme principal ################ 
reinit()
fen.mainloop()        

