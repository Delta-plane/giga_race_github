import pygame
from constantes import*
from Missiles import*
import numpy as np
class basic_ennemy(object):
    def __init__(self,screen):
        self.id = "Ennemy"
        self.id_perso = 1
        self.screen = screen
        self.color = (255,255,255)
        self.x = 0.9*screen_size_y+1
        self.y = 0.9*screen_size_x+1
        self.image1 = pygame.image.load("basic-ship.png")
        self.size_x = self.image1.get_width()
        self.size_y = self.image1.get_height()
        self.speed = 10
        self.rect = self.image1.get_rect()
        self.Is_active = True
        self.coeff = 0.25
        self.move_delay = 250
        self.nb_missiles = 4
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