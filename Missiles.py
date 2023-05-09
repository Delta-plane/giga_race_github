import pygame
from constantes import*
import numpy as np
class weapon(object):
    def __init__(self,screen):
        self.screen = screen
        self.speed = 25
        self.x = 100
        self.y = 100
        self.hauteur = 5
        self.color = (255,255,255)
        self.image = pygame.image.load("Missile.png")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.tempref = 0
        self.angle = 0
        self.nb_touche = 0
        self.ref_vise_x = 1
        self.ref_vise_y = 0
        self.has_shoot = False
        self.id_objet_touche = 0
    def dessin(self):
        self.screen.blit(self.image,(self.x,self.y))
        self.rect = self.image.get_rect(center=(self.x,self.y))
    def initialiser_tir(self,Vaisseau):
       self.tempref = pygame.time.get_ticks()
       self.image = pygame.transform.rotate(self.image,Vaisseau.angle - self.angle)
       self.angle = Vaisseau.angle
       self.x = Vaisseau.x - np.sin(self.angle*np.pi/180)*Vaisseau.size_x/2
       self.y = Vaisseau.y - np.cos(self.angle*np.pi/180)*Vaisseau.size_y/2
       self.has_shoot = True
    def mouvement(self):
        self.x -= np.sin(self.angle*np.pi/180)*self.speed
        self.y -= np.cos(self.angle*np.pi/180)*self.speed
    def tirer(self,temps_entre_tirs):
        if pygame.time.get_ticks()>self.tempref and self.has_shoot:
            self.x -= np.sin(self.angle*np.pi/180)*self.speed
            self.y -= np.cos(self.angle*np.pi/180)*self.speed
        if pygame.time.get_ticks()>self.tempref+temps_entre_tirs:
            self.has_shoot = False
class stock_missiles(object):
    def __init__(self,screen):
        self.nb_missiles = 4
        self.liste_missiles_valides = [1 for i in range(self.nb_missiles)]
        self.screen = screen
        self.time_ms_before_shoot = 3000
        self.missile = [weapon(self.screen) for i in range(self.nb_missiles)]
        self.current_missile_shoot_id = 0
    def update_missile_valide(self):
        for k in range(0,self.nb_missiles):
            if self.missile[k].tempref+self.time_ms_before_shoot<pygame.time.get_ticks() and not self.missile[k].has_shoot:
                self.liste_missiles_valides[k] = 1
    def id_tirer(self):
        for n in range(0,self.nb_missiles):
            if self.liste_missiles_valides[n]==1:
                return(n)
        return(self.nb_missiles+1)
    def dessin_missiles_valide(self):
        for n in range(0,self.nb_missiles):
            if self.liste_missiles_valides[n] == 0 and self.missile[n].has_shoot:
                self.missile[n].tirer(self.time_ms_before_shoot)
                self.missile[n].mask =pygame.mask.from_surface(self.missile[n].image)
                self.missile[n].dessin()








