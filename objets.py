import pygame
import numpy as np
from pygame.locals import*
pygame.init()
from constantes import*
police = pygame.font.SysFont("monospace" ,23)
def affiche_texte(texte, x, y, couleur,fenetre):
    text=police.render(texte,1,couleur)
    fenetre.blit(text,(x,y))
    pygame.display.flip()



class Carre_central(object):
    def __init__(self,screen):
        self.sizex =0.3*screen_size_x
        self.sizey =0.25*screen_size_y
        self.x =0.5*screen_size_x-(0.5*self.sizex)
        self.y =0.5*screen_size_y-(0.5*self.sizey)
        self.score_val=0
        self.screen=screen
        self.color=(255,255,255)

    def dessin(self):
        pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.sizex,self.sizey),5)

    def score(self):
        affiche_texte(("score"),(self.x+0.5*self.sizex),(self.y),(255,0,0),self.screen)
        affiche_texte(("10000"),(self.x+0.5*self.sizex),(self.y+23),(255,0,0),self.screen)
        affiche_texte(("high score"),(self.x+0.5*self.sizex-35),(self.y+46+40),(255,0,0),self.screen)
        affiche_texte(("0"),(self.x+0.5*self.sizex),(self.y+69+40),(255,0,0),self.screen)

class Triangle():
    def __init__(self,screen):
        self.screen = screen
        self.color = (255,255,0)
        self.size = 100
        self.middle_x = 100
        self.middle_y = 100
        self.A = (80,80)
        self.B = (120,80)
        self.C = (100,120)
        self.x = 100
        self.y = 100
        self.speed = 25
        self.coeff = 0.25
        self.nb_ro_poss = 12
        self.List_rota = []
        self.current_list_id = 0
        self.limit_wall = 30
        self.rebound_strenght =38
        self.temps_ref = 0
    def generer_Liste_config_angle(self):
        for k in range(0,self.nb_ro_poss):
            self.List_rota.append((2*k*3.1415)/self.nb_ro_poss) #give the angle of self.A

    def rotation2(self):
        self.A = (self.size*self.coeff*np.cos(self.List_rota[self.current_list_id])+self.x,self.size*self.coeff*np.sin(self.List_rota[self.current_list_id])+self.y)
        self.B = (self.size*self.coeff*np.cos(self.List_rota[self.current_list_id]+(2/3)*3.1415)+self.x,self.size*self.coeff*np.sin(self.List_rota[self.current_list_id]+(2/3)*3.1415)+self.y)
        self.C = (self.size*self.coeff*np.cos(self.List_rota[self.current_list_id]+(4/3)*3.1415)+self.x,self.size*self.coeff*np.sin(self.List_rota[self.current_list_id]+(4/3)*3.1415)+self.y)

    def rotation_gauche(self):
        if self.current_list_id ==0:
            self.current_list_id = self.nb_ro_poss-1
        else:
            self.current_list_id -=1
        self.rotation2()

    def rotation_droite(self):
        if self.current_list_id ==self.nb_ro_poss-1:
            self.current_list_id = 0
        else:
            self.current_list_id +=1
        self.rotation2()

    def dessin(self):
        pygame.draw.polygon(self.screen,self.color,(self.A,self.B,self.C))
    def mouvement(self):
        self.x += np.cos(self.List_rota[self.current_list_id])*self.speed
        self.y += np.sin(self.List_rota[self.current_list_id])*self.speed
        self.rotation2()

    def rebond_mur(self):
        if self.x<self.limit_wall:
            self.x += self.rebound_strenght
        elif self.x>screen_size_x - self.limit_wall:
            self.x -= self.rebound_strenght
        elif self.y<self.limit_wall:
            self.y += self.rebound_strenght
        elif self.y>screen_size_y - self.limit_wall:
            self.y -= self.rebound_strenght
    def init_temps_ref(self):
        self.temps_ref = pygame.time.get_ticks()



class weapon(object):
    def __init__(self,screen):
        self.screen = screen
        self.speed = 25
        self.x = 100
        self.y = 100
        self.hauteur = 5
        self.color = (255,255,255)
        self.tempref = 0
        self.has_shoot = False
    def dessin(self):
        pygame.draw.circle(self.screen,self.color,(int(self.x),int(self.y)),3)
    def initialiser_tir(self):
       self.tempref = pygame.time.get_ticks()
       self.has_shoot = True

class stock_missiles(object):
    def __init__(self,screen):
        self.nb_missiles = 4
        self.liste_missiles_valides = []
        self.screen = screen
        self.time_ms_before_shoot = 3000
        self.missile = [weapon(self.screen) for i in range(self.nb_missiles)]
        self.current_missile_shoot_id = 0
    def add_missiles(self):
        for n in range(0,self.nb_missiles):
            self.liste_missiles_valides.append(1)
    def update_missile_valide(self):
        for k in range(0,self.nb_missiles):
            if self.missile[k].tempref+self.time_ms_before_shoot<pygame.time.get_ticks() and not self.missile[k].has_shoot:
                self.liste_missiles_valides[k] = 1

class ennemy(object):
    def __init__(self,screen):
        self.screen = screen
        self.color = (255,255,255)
        self.size = 20
        self.x = 0.9*screen_size_y+1
        self.y = 0.9*screen_size_x+1
        self.speed = 10
        self.coeff = 0.25
        self.move_delay = 250
        self.nb_missiles = 4
        self.missile = [weapon(screen) for i in range(0,4)]
        self.joueur_x_ref = 100
        self.joueur_y_ref = 100
        self.diviser_vit_tir = 50
        self.tempref_tir = pygame.time.get_ticks()
        self.tir_delay = 5000 #time before each shoot in ms

    def dessin(self):
        pygame.draw.circle(self.screen,self.color,(int(self.x),int(self.y)),self.size)

    def mouvement(self):
        if self.x >= screen_size_x*0.9 and self.y <=screen_size_y*0.9:
            self.y += self.speed
        if self.x <= screen_size_x*0.1 and self.y > screen_size_y*0.1:
            self.y -= self.speed
        if self.y <= screen_size_y*0.1 and self.x <screen_size_x*0.9:
            self.x +=self.speed
        if self.y >= screen_size_y*0.9 and self.x >=screen_size_x*0.1:
            self.x -=self.speed


class all_ennemies(object):
    def _init__(self,screen):
        self.current_ennemies = 1
        self.max_ennemies = 10
        self.screen = screen
        self.ennemies = [ennemy(self.screen) for i in range(self.max_ennemies)]
        self.ennemies_can_respawn = [0 for i in range(self.max_ennemies)] # 0 = inactif 1=actif
        self.respawn_time = 10000 #ms, will decrease step by step

    def update_ennemis_valides(self):
        for k in range(self.max_ennemies):
            if self.respawn_time+self.ennemies[k].temps_ref>pygame.time.get_ticks():
                self.ennemies_can_respawn[k] = 1

def transfert_vers_vaisseau(Missile,Vaisseau):
    Missile.x = Vaisseau.A[0]
    Missile.y = Vaisseau.A[1]
def transfert_missile_vers_ennemy(Missile,Ennemy):
    Missile.x = Ennemy.x
    Missile.y = Ennemy.y

def tirer(Missile,Vaisseau,tempref):
       if pygame.time.get_ticks()>Missile.tempref and Missile.has_shoot:
        Missile.x += np.cos(Vaisseau.List_rota[Vaisseau.current_list_id])*Missile.speed
        Missile.y += np.sin(Vaisseau.List_rota[Vaisseau.current_list_id])*Missile.speed
        if pygame.time.get_ticks()>Missile.tempref+1000:
            Missile.has_shoot = False

def viser_vaisseau(Vaisseau,Ennemy):

    Ennemy.joueur_x_ref = (Vaisseau.x-Ennemy.x)/Ennemy.diviser_vit_tir
    Ennemy.joueur_y_ref = (Vaisseau.y-Ennemy.y)/Ennemy.diviser_vit_tir

def tirer_vers_joueur(Missile,Vaisseau,Ennemy):
    Missile.x += Ennemy.joueur_x_ref
    Missile.y += Ennemy.joueur_y_ref

def tir_missile_vers_joueur_global(Missile,Vaisseau,Ennemy): # gere les tirs des ennnemies et donc transfert_missiles_vers_ennemy + viser vaisseau + tirer vers joueur
    if pygame.time.get_ticks() > Ennemy.tempref_tir + Ennemy.tir_delay:
        viser_vaisseau(Vaisseau,Ennemy)
        transfert_missile_vers_ennemy(Missile,Ennemy)
        Ennemy.tempref_tir = pygame.time.get_ticks()
    else:
        tirer_vers_joueur(Missile,Vaisseau,Ennemy)
        Missile.dessin()



