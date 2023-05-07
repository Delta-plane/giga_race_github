
def est_dans_carre(Vaisseau,Carre):
    if Carre.x<=Vaisseau.A[0]<=Carre.x+Carre.sizex:
        if Carre.y<=Vaisseau.A[1]<=Carre.x+Carre.sizey:
            print("est dedans")
            