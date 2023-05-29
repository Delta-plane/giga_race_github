import pygame
from constantes import*
from Missiles import*
import numpy as np
class Space_ship():
    def __init__(self,screen):
        self.Is_active = True
        self.id = "Player"
        self.life = 3
        self.max_life = 3
        self.screen = screen
        self.size = 100
        self.nb_missiles = 4
        self.stock = stock_missiles(screen)
        self.screen_size_x = screen_size_x
        self.screen_size_y = screen_size_y
        self.x = 100
        self.y = 100
        self.temp_explosion=0
        self.respawn_x = 150
        self.respawn_y = 100
        self.contact_carre_hb = False
        self.contact_carre_gd= False
        self.modify_y_velocity = False
        self.explo=False
        self.explox=self.x
        self.exploy=self.y
      
        self.image1 = pygame.sprite.Sprite()
        self.image0=pygame.sprite.Sprite()
        self.image0.image = pygame.image.load("Vaisseau2.png").convert_alpha()
        self.image0.image = pygame.transform.scale(self.image0.image, (75,75))
        self.image1.image=self.image0.image
        self.image1.rect = self.image1.image.get_rect()
        self.image1.mask = pygame.mask.from_surface(self.image0.image)#1
        self.rect_explo = self.image1.image.get_rect(center = (self.explox,self.exploy))
        self.image0.rect0 = self.image0.image.get_rect()
        self.image1.rect = self.image0.rect0
        self.size_x = self.image0.image.get_width()
        self.size_y =self.image0.image.get_height()
        self.image1.rect.center=(self.x+self.size_x,self.y+self.size_y)
        self.speed = 10
        self.angle = 0
       
        self.rebound_strenght =38
        self.temps_ref = 0
        self.velocité = 0
        self.coeff_velocité_y = 1
        self.coeff_velocité_x = 1
        self.gliang=0
        self.temps_ref_pour_respawn = 1500
        self.temps_ref_respawn = 0
    def respawn(self):
        self.x = self.respawn_x
        self.y = self.respawn_y
        self.Is_active = True
    def respawn_apres_mort(self):
        if pygame.time.get_ticks() > self.temps_ref_respawn+self.temps_ref_pour_respawn and self.Is_active==False:
            self.respawn()

    def despawn(self):
        self.Is_active = False
        self.temps_ref_respawn = pygame.time.get_ticks()
    def dessin(self):
        self.image1.rect = self.image1.image.get_rect(center=(self.x,self.y))
        self.screen.blit(self.image1.image,self.image1.rect)
        self.image1.mask = pygame.mask.from_surface(self.image1.image)
    def rotation_gauche2(self):
        self.angle +=15
        self.angle = self.angle%360
        self.image1.image = pygame.transform.rotate(self.image0.image,self.angle)
        self.image1.rect = self.image1.image.get_rect(center = (self.x,self.y))
        self.image1.mask = pygame.mask.from_surface(self.image1.image)
    def rotation_droite2(self):
        self.angle -=15
        self.angle = self.angle%360
        self.image1.image = pygame.transform.rotate(self.image0.image,self.angle)
        self.image1.rect = self.image1.image.get_rect(center = (self.x,self.y))
        self.image1.mask = pygame.mask.from_surface(self.image1.image)
    def teleport(self):
        self.screen.blit(self.image0.image,(250,250))
    def mouvement(self):
        if (self.contact_carre_hb==False and self.contact_carre_gd==False ):
            if self.velocité < 5:
                self.velocité += 1
            self.x -= np.sin(self.angle*np.pi/180)*self.speed
            self.y -= np.cos(self.angle*np.pi/180)*self.speed
            if self.coeff_velocité_y !=1:
                self.coeff_velocité_y = 1
            if self.coeff_velocité_x !=1:
                self.coeff_velocité_x = 1
            self.gliang=self.angle
            self.image1.rect = self.image1.image.get_rect(center = (self.x,self.y))
            self.image1.mask = pygame.mask.from_surface(self.image1.image)
    def glisse(self):
        if (self.velocité>0):
            if self.contact_carre_hb:
                self.y-=self.speed
                self.contact_carre_hb = False
                self.coeff_velocité_y = self.coeff_velocité_y*(-1)
                self.coeff_velocité_x = self.coeff_velocité_x*(-1)
            elif self.contact_carre_gd:

                    self.x-=self.speed-3
                    self.contact_carre_gd = False

            else:
                self.x-=np.sin(self.gliang*np.pi/180)*self.velocité*self.coeff_velocité_x
                self.y-=np.cos(self.gliang*np.pi/180)*self.velocité*self.coeff_velocité_y
                self.velocité-=0.05
            self.image1.rect = self.image1.image.get_rect(center = (self.x,self.y))
            self.image1.mask = pygame.mask.from_surface(self.image1.image)

    def gerer_tir(self):
                    self.stock.update_missile_valide()
                    self.stock.current_missile_shoot_id =self.stock.id_tirer()
                    if self.stock.current_missile_shoot_id!=self.stock.nb_missiles +1:

                        self.stock.missile[self.stock.current_missile_shoot_id].initialiser_tir(self)
                        self.stock.liste_missiles_valides[self.stock.current_missile_shoot_id] = 0
    def temp_explo(self,explosion):
        if (self.explo and self.temp_explosion<44):
            if (self.temp_explosion==0):
                self.explox=self.x
                self.exploy=self.y
                self.rect_explo=self.image1.image.get_rect(center = (self.explox,self.exploy))

            self.temp_explosion+=1
            self.screen.blit(explosion.images[self.temp_explosion],self.rect_explo)
        else:
            self.temp_explosion=0
            self.explo=False

