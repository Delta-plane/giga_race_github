import pygame
from constantes import*
from Missiles import*
import numpy as np
from random import randint
class basic_ennemy(object):
    def __init__(self,screen):
        self.id = "Ennemy"
        self.value_when_killed = 1500
        self.id_perso = 1
        self.screen = screen
        self.color = (255,255,255)
        self.x = 0.9*screen_size_y+1
        self.y = 0.9*screen_size_x+1
        self.coeff_agrandir_img = 0.07
        self.image1 = pygame.image.load("basic-ship.png")
        self.image1 = pygame.transform.scale(self.image1,(int(self.coeff_agrandir_img *screen_size_x),int(self.coeff_agrandir_img *screen_size_y))).convert_alpha()
        self.size_x = self.image1.get_width()
        self.size_y = self.image1.get_height()
        self.mask = pygame.mask.from_surface(self.image1)
        self.speed = 10
        self.rect = self.image1.get_rect()
        self.Is_active = True
        self.coeff = 0.25
        self.move_delay = 250
        self.nb_missiles = 4
        self.spawn = (self.x,self.y)
        self.time_before_respawn = 3000
        self.tempref_respawn = 0
        self.respawn_case = 0
        self.angle = 3.1415/2
        self.missile = weapon(screen)
        self.joueur_x_ref = 100
        self.joueur_y_ref = 100
        self.diviser_vit_tir = 50
        self.tempref_tir = pygame.time.get_ticks()
        self.has_shoot = False
        self.tir_delay = 3000 #time before each shoot in ms
        self.missile_lifespan = 1000 #time when weapon is active

    def dessin(self):
        self.screen.blit(self.image1,self.rect)
        self.rect = self.image1.get_rect(center=(self.x,self.y))

    def mouvement(self):
        if self.x >= screen_size_x*0.9 and self.y <=screen_size_y*0.9:
            self.y += self.speed
            self.angle = np.pi/2
        if self.x <= screen_size_x*0.1 and self.y >= screen_size_y*0.1:
            self.y -= self.speed
            self.angle = (3/2)*np.pi
        if self.y <= screen_size_y*0.1 and self.x <=screen_size_x*0.9:
            self.x +=self.speed
            self.angle = 0
        if self.y >= screen_size_y*0.9 and self.x >=screen_size_x*0.1:
            self.x -=self.speed
            self.angle = np.pi

    def transfert_missile_vers_basic_ship(self):
        self.missile.x = self.x - np.sin(self.angle)
        self.missile.y = self.y - np.cos(self.angle)
    def tirer_haut(self):
        if self.tempref_tir + self.tir_delay >pygame.time.get_ticks():
            self.has_shoot = True
            self.tempref_tir = pygame.time.get_ticks()
        #if self.has_shoot():
    def despawn(self):
        self.Is_active =False
        self.tempref_respawn = pygame.time.get_ticks()
    def respawn(self):
        if not self.Is_active and pygame.time.get_ticks() > self.tempref_respawn+self.time_before_respawn:
            self.respawn_case = randint(0,4)
            if self.respawn_case == 0:
                 self.x = 0.1*screen_size_x
                 self.y = 0.1*screen_size_y
            if self.respawn_case == 1:
                 self.x = 0.9*screen_size_x
                 self.y = 0.1*screen_size_y
            if self.respawn_case == 2:
                 self.x = 0.1*screen_size_x
                 self.y = 0.9*screen_size_y
            if self.respawn_case == 3:
                 self.x = 0.9*screen_size_x
                 self.y = 0.9*screen_size_y
            self.Is_active=True








class all_ennemies(object):
    def __init__(self,screen):
        self.screen = screen
        self.current_ennemies = 1
        self.max_ennemies = 10
        self.nb_current_ennemies = 1
        self.ennemies = [basic_ennemy(self.screen) for i in range(self.max_ennemies)]
        self.ennemies_can_respawn = [0 for i in range(self.max_ennemies)] # 0 = inactif 1=actif
        self.respawn_time = 10000 #ms, will decrease step by step

    def update_ennemis_valides(self):
        for k in range(0,self.nb_current_ennemies):
            if self.respawn_time+self.ennemies[k].temps_ref>pygame.time.get_ticks():
                self.ennemies_can_respawn[k] = 1

    def dessin_ennemis_valide(self):
        for s in range(0,self.nb_current_ennemies):
            if self.ennemies[s].Is_active:
                self.ennemies[s].mouvement()
                self.ennemies[s].dessin()
