from constantes import*
def limite_gauche_valide(limite_x,Vaisseau):
    if (Vaisseau.x+limite_x>=screen_size_x):
        return(False)
    else:
        return(True)
        
def limite_droite_valide(limite_x,Vaisseau):
    if (Vaisseau.x-limite_x<=0):
        return(False)
    else:
        return(True)
    
def limite_haut_valide(limite_y,Vaisseau):
    if (Vaisseau.y-limite_y<=0):
        return(False)
    else:
        return(True)
    
def limite_bas_valide(limite_y,Vaisseau):
    if (Vaisseau.y+limite_y>=screen_size_y):
        return(False)
    else:
        return(True)
    
def test_les_limites(limite_x,limite_y,Vaisseau):
    if limite_bas_valide(limite_y,Vaisseau) and limite_haut_valide(limite_y,Vaisseau) and limite_droite_valide(limite_x,Vaisseau) and limite_gauche_valide(limite_x,Vaisseau):
        return(True)
    else:
        return(False)