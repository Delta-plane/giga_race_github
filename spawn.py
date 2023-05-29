from random import randint
from Interactions import*
def spawn_valide(All_ennemies,id,Objet,carre,taille_ecran_x,taille_ecran_y,Player):
    Respawn_valide = False
    while not Respawn_valide:
        if Objet.id == "Basic-Ennemy"  :
            Objet.respawn()
       
            
        else:
            Objet.x = randint(40,taille_ecran_x-40)
            Objet.y = randint(40,taille_ecran_y-40)
        Objet.dessin()
        if verifier_collisions_respawn(All_ennemies,Player,carre,Objet,id) and Objet.id !="Player":
            Respawn_valide = True



