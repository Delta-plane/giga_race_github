import pygame
from constantes import*
import numpy as np
from sons import*
pygame.mixer.pre_init(44100,-16,2,2048)

pygame.init()

musique=sons()
class weapon(object):
    def __init__(self,screen):
        self.screen = screen
        self.speed = 25
        self.x = 100
        self.y = 100
        self.hauteur = 5
        self.color = (255,255,255)
        self.image1=pygame.sprite.Sprite()
        self.image1.image = pygame.image.load("Missile.png")
        self.width = self.image1.image.get_width()
        self.height = self.image1.image.get_height()
        self.image1.image = pygame.transform.scale(self.image1.image,(self.width,self.height))
        self.image1.rect = self.image1.image.get_rect()
        self.image1.mask = pygame.mask.from_surface(self.image1.image)
        self.tempref = 0
        self.angle = 0
        self.nb_touche = 0
        self.ref_vise_x = 1
        self.ref_vise_y = 0
        self.has_shoot = False
        self.Must_be_changed = False
        self.id_objet_touche = 0
    def dessin(self):
        self.image1.image = pygame.image.load("Missile.png")
        self.image1.image = pygame.transform.rotozoom(self.image1.image,self.angle,1)
        self.image1.rect = self.image1.image.get_rect(center=(self.x,self.y))
        self.screen.blit(self.image1.image,self.image1.rect)
        self.image1.mask = pygame.mask.from_surface(self.image1.image)

    def re_definir_missile(self):
        self.image1=pygame.sprite.Sprite()
        self.image1.image = pygame.image.load("Missile.png")
        self.image1.rect = self.image1.image.get_rect()
        self.image1.mask = pygame.mask.from_surface(self.image1.image)

    def initialiser_tir(self,Vaisseau):
       musique.tire_sound.play()
       self.tempref = pygame.time.get_ticks()
       self.image1.image = pygame.transform.rotate(self.image1.image,Vaisseau.angle - self.angle)
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
        self.liste_missile_non_val=[]
        self.liste_missiles_valides = [1 for i in range(self.nb_missiles)]
        self.screen = screen
        self.time_ms_before_shoot = 3000
        self.missile = [weapon(self.screen) for i in range(self.nb_missiles)]
        self.current_missile_shoot_id = 0
    def remettre_val(self):
        for miss in self.liste_missile_non_val:
            miss.has_shoot=True
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
                self.missile[n].image1.mask =pygame.mask.from_surface(self.missile[n].image1.image)
                self.missile[n].dessin()

    
    def despawn_chgmt_lv(self):
        for n in range(0,self.nb_missiles):
            self.missile[n].has_shoot = False




