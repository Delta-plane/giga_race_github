import pygame
import numpy as np
def transfert_vers_vaisseau(Missile,Vaisseau): #vaisseau
    Missile.x = Vaisseau.A[0]
    Missile.y = Vaisseau.A[1]
    
def viser_avec_vaisseau(Missile,Vaisseau):
    Missile.ref_vise_x = np.cos(Vaisseau.List_rota[Vaisseau.current_list_id])
    Missile.ref_vise_y = np.sin(Vaisseau.List_rota[Vaisseau.current_list_id])


def tirer(Missile,Vaisseau,tempref): #vaisseau
       if pygame.time.get_ticks()>Missile.tempref and Missile.has_shoot:
        Missile.x += Missile.ref_vise_x*Missile.speed
        Missile.y += Missile.ref_vise_y*Missile.speed
        if pygame.time.get_ticks()>Missile.tempref+1000:
            Missile.has_shoot = False



def transfert_missile_vers_ennemy(Missile,Ennemy):
    Missile.x = Ennemy.x
    Missile.y = Ennemy.y

def viser_vaisseau(Vaisseau,Ennemy):

    Ennemy.joueur_x_ref = (Vaisseau.x-Ennemy.x)/Ennemy.diviser_vit_tir
    Ennemy.joueur_y_ref = (Vaisseau.y-Ennemy.y)/Ennemy.diviser_vit_tir

def tirer_vers_joueur(Missile,Vaisseau,Ennemy):
    Missile.x += Ennemy.joueur_x_ref
    Missile.y += Ennemy.joueur_y_ref

def tir_missile_vers_joueur_global(Missile,Vaisseau,Ennemy): # gere les tirs des ennnemis et donc transfert_missiles_vers_ennemy + viser vaisseau + tirer vers joueur
    if pygame.time.get_ticks() > Ennemy.tempref_tir + Ennemy.tir_delay:
        viser_vaisseau(Vaisseau,Ennemy)
        transfert_missile_vers_ennemy(Missile,Ennemy)
        Ennemy.tempref_tir = pygame.time.get_ticks()
    else:
        tirer_vers_joueur(Missile,Vaisseau,Ennemy)
        Missile.dessin()
