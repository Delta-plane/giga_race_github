import pygame
from constantes import*
from Missiles import*
import numpy as np
class Space_ship():
    def __init__(self,screen):
        self.Is_active = True
        self.id = "Player"
        self.screen = screen
        self.size = 100
        self.nb_missiles = 4
        self.stock = stock_missiles(screen)
        self.screen_size_x = screen_size_x
        self.screen_size_y = screen_size_y
        self.x = 100
        self.y = 100
        self.image0 = pygame.image.load("Vaisseau3.png")
        self.image0 = pygame.transform.scale(self.image0, (75,75))
        self.image1 = self.image0
        self.rect0 = self.image0.get_rect()
        self.rect0_center = (screen_size_x//2,screen_size_y//2)
        self.rect  = self.rect0
        self.rect_center = self.rect0_center
        self.mask=pygame.mask.from_surface(self.image0)
        self.size_x = self.image0.get_width()
        self.size_y =self.image0.get_height()
        self.speed = 10
        self.angle = 0
        self.limit_wall_y = 30
        self.limit_wall_x = 30
        self.rebound_strenght =38
        self.temps_ref = 0
    def dessin(self):
        self.screen.blit(self.image1,self.rect)
    def rotation_gauche2(self):
        self.angle +=15
        self.angle = self.angle%360
        self.image1 = pygame.transform.rotate(self.image0,self.angle)
        self.rect = self.image1.get_rect(center = (self.x,self.y))
    def rotation_droite2(self):
        self.angle -=15
        self.angle = self.angle%360
        self.image1 = pygame.transform.rotate(self.image0,self.angle)
        self.rect = self.image1.get_rect(center = (self.x,self.y))
    def teleport(self):
        self.screen.blit(self.image0,(250,250))
    def mouvement(self):
        self.x -= np.sin(self.angle*np.pi/180)*self.speed
        self.y -= np.cos(self.angle*np.pi/180)*self.speed
        self.rect = self.image1.get_rect(center = (self.x,self.y))
    def rebond_carre(self,carre):
        if self.rect.colliderect(carre.rect):
            offset = (int(carre.rect.x - self.rect.x), int(carre.rect.y - self.rect.y))
            overlap = self.mask.overlap(carre.mask, offset)
            print(overlap)
            if overlap is not None:
                    print("Collision au pixel près détectée !")
    def gerer_tir(self):
                    self.stock.update_missile_valide()
                    self.stock.current_missile_shoot_id =self.stock.id_tirer()
                    if self.stock.current_missile_shoot_id!=self.stock.nb_missiles +1:
                        self.stock.missile[self.stock.current_missile_shoot_id].initialiser_tir(self)
                        self.stock.liste_missiles_valides[self.stock.current_missile_shoot_id] = 0