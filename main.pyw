#!/usr/bin/env python
from tkinter import *

def carre():
    """ Calcul du carré """
    Resultat.set("Carré = "+str(float(Valeur.get())**2))

# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title("Spinbox widget")

Valeur = StringVar()
Valeur.set(2.0)
# Création d'un widget Spinbox
boite = Spinbox(Mafenetre,from_=0,to=10,increment=0.5,textvariable=Valeur,width=5,command=carre)
boite.pack(padx=30,pady=10)

# Création d'un widget Label
Resultat = StringVar()
carre()
Label(Mafenetre,textvariable=Resultat).pack(padx=30,pady=10)

Mafenetre.mainloop()