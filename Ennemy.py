import pygame
from constantes import*
from Missiles import*
from Updates import*

import numpy as np
from random import randint

class basic_ennemy(object):
    def __init__(self,screen):
        self.id = "Basic-Ennemy"
        self.origin="basic"
        self.temp_explosion=0
        self.temp_transfo=0
        self.tran=False
        self.value_when_killed = 1500
        self.id_perso = 1
        self.screen = screen
        self.color = (255,255,255)
        self.x = 0.9*screen_size_y+1
        self.y = 0.9*screen_size_x+1
        self.explo=False
        self.explox=self.x
        self.exploy=self.y
        self.coeff_agrandir_img = 0.07
        self.image1=pygame.sprite.Sprite()
        self.image1.image = pygame.image.load("basic-ship.png")
        self.image1.image = pygame.transform.scale(self.image1.image,(int(self.coeff_agrandir_img *screen_size_x),int(self.coeff_agrandir_img *screen_size_y))).convert_alpha()
        self.rect_explo = self.image1.image.get_rect(center = (self.explox,self.exploy))
        self.size_x = self.image1.image.get_width()
        self.size_y = self.image1.image.get_height()
        self.image1.mask = pygame.mask.from_surface(self.image1.image)
        self.speed = 10
        self.image1.rect = self.image1.image.get_rect()
        self.Is_active = True
        self.coeff = 0.25
        self.move_delay = 250
        self.spawn = (self.x,self.y)
        self.time_before_respawn = 1000
        self.tempref_respawn = 0
        self.respawn_case = 0
        self.angle = 3.1415/2
        self.joueur_x_ref = 100
        self.joueur_y_ref = 100
        

    def dessin(self):
        self.image1.rect = self.image1.image.get_rect(center=(self.x,self.y))
        self.screen.blit(self.image1.image,self.image1.rect)
        self.image1.mask = pygame.mask.from_surface(self.image1.image)

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

    
    def despawn(self):
        self.Is_active =False
        self.tempref_respawn = pygame.time.get_ticks()
    def respawn(self):
        if pygame.time.get_ticks() > self.tempref_respawn+self.time_before_respawn:
            self.respawn_case = randint(0,3)
            if self.respawn_case == 1:
                 self.x = 0.9*screen_size_x
                 self.y = 0.1*screen_size_y
            if self.respawn_case == 2:
                 self.x = 0.1*screen_size_x
                 self.y = 0.9*screen_size_y
            if self.respawn_case == 0:
                 self.x = 0.9*screen_size_x
                 self.y = 0.9*screen_size_y
            self.Is_active=True
    def temp_explo(self,explosion):
        if (self.explo and self.temp_explosion<44):

            if (self.temp_explosion==0):

                self.explox=self.x
                self.exploy=self.y
                self.rect_explo=self.image1.image.get_rect(center = (self.explox,self.exploy))


            self.temp_explosion+=1
            pygame.time.delay(1)
            self.screen.blit(explosion.images[self.temp_explosion],self.rect_explo)
        else:
            self.temp_explosion=0
            self.explo=False
    def temp_trans(self):
        if self.temp_transfo  >pygame.time.get_ticks():
            self.tran = True
            self.temp_transfo = pygame.time.get_ticks()

        else:
            self.temp_transfo+=37
            self.tran = False


class Mine(object):
    def __init__(self,screen):
        self.id = "Mine"
        self.origin="Mine"
        self.x= 200
        self.y =200
        self.temp_explosion=0
        self.temp_transfo=0
        self.tran=False
        self.screen =screen
        self.value_when_killed = 500
        self.aggrandissement_x = 0.05
        self.aggrandissement_y = 0.05
        self.image1=pygame.sprite.Sprite()
        self.image1.image = pygame.image.load("Tnt.png")#"Tnt.png"
        self.image1.image = pygame.transform.scale(self.image1.image,(int(screen_size_x*self.aggrandissement_x),int(screen_size_y*self.aggrandissement_y)))
        self.image1.rect = self.image1.image.get_rect()
        self.size_x = self.image1.image.get_width()
        self.size_y = self.image1.image.get_height()
        self.image1.rect.center=(self.x+self.size_x,self.y+self.size_y)
        self.image1.mask = pygame.mask.from_surface(self.image1.image)
        self.tempref_respawn =0
        self.nb_missiles = 0
        self.Is_active = True
        self.time_before_respawn = 1600
        self.explo=False
        self.explox=self.x
        self.exploy=self.y
        self.rect_explo = self.image1.image.get_rect(center = (self.explox,self.exploy))

    def dessin(self):
        self.screen.blit(self.image1.image,(self.x,self.y))
        self.image1.rect = self.image1.image.get_rect(center=(self.x+self.size_x/2,self.y+self.size_y/2))
        self.image1.mask = pygame.mask.from_surface(self.image1.image)
    def despawn(self):

        self.Is_active =False
        self.tempref_respawn = pygame.time.get_ticks()
    def respawn(self):
        if pygame.time.get_ticks() > self.tempref_respawn+self.time_before_respawn:
            self.Is_active = True
    def temp_explo(self,explosion):
        if (self.explo and self.temp_explosion<44):

            if (self.temp_explosion==0):

                self.explox=self.x
                self.exploy=self.y
                self.rect_explo=self.image1.image.get_rect(center = (self.explox,self.exploy))


            self.temp_explosion+=1
            pygame.time.delay(1)
            self.screen.blit(explosion.images[self.temp_explosion],self.rect_explo)
        else:
            self.temp_explosion=0
            self.explo=False

    def temp_trans(self):
        if self.temp_transfo>pygame.time.get_ticks():
            self.tran = True
            self.temp_transfo = pygame.time.get_ticks()

        else:
            self.temp_transfo+=37
            self.tran = False





class thunder_ennemy(object):
    def __init__(self,screen):

        self.id = "thunder_ennemy"
        self.temp_transfo=0
        self.tran=False
        self.temp_explosion=0
        self.value_when_killed = 1500
        self.id_perso = 1
        self.screen = screen
        self.color = (255,255,255)
        self.x = 650
        self.y = 600
        self.explo=False
        self.explox=self.x
        self.exploy=self.y
        self.coeff_agrandir_img = 0.04
        self.image1=pygame.sprite.Sprite()
        self.image1.image = pygame.image.load("eclair.png")
        self.image1.image = pygame.transform.scale(self.image1.image,(int(self.coeff_agrandir_img *screen_size_x),int(self.coeff_agrandir_img *screen_size_y))).convert_alpha()
        self.image0=self.image1
        self.rect_explo = self.image1.image.get_rect(center = (self.explox,self.exploy))
        self.size_x = self.image1.image.get_width()
        self.size_y = self.image1.image.get_height()
        self.image1.mask = pygame.mask.from_surface(self.image1.image)
        self.speed =10
        self.image1.rect = self.image1.image.get_rect()
        self.Is_active = True
        self.coeff = 0.25
        self.move_delay = 250
        self.spawn = (self.x,self.y)
        self.time_before_respawn = 1000
        self.tempref_respawn = 0
        self.respawn_case = 0
        self.angle = 135
        self.joueur_x_ref = 100
        self.joueur_y_ref = 100
      

    def dessin(self):
        self.image1.rect = self.image0.image.get_rect(center=(self.x,self.y))
        self.screen.blit(self.image0.image,self.image0.rect)
        self.image1.mask = pygame.mask.from_surface(self.image0.image)

    def mouvement(self,carre):
        if self.image0.rect.colliderect(carre.rect):
            offset = (int(carre.rect.x - self.image1.rect.x), int(carre.rect.y - self.image1.rect.y))
            overlap = self.image1.mask.overlap(carre.mask, offset)
            if overlap is not None:


                if self.x > carre.x + 1 :
                    if self.y >carre.y +1 :
                        if self.x < carre.x+carre.sizex-1:

                           # cas ou bas du carré
                            self.angle=225
                            self.y += self.speed*1.2
                        else:
                            self.angle=315
                            self.x += self.speed*1.2#cas ou coté droit du carré


                    else: #haut du carré
                        self.angle=45
                        self.y -= self.speed*1.2

                else:
                    if  self.y >carre.y +1 :  #gauche du carré
                        self.angle=135
                        self.x -= self.speed*1.2
                    else:
                         self.x += np.sin(-self.angle*np.pi/180)*self.speed*1.2
                         self.y += np.cos(-self.angle*np.pi/180)*self.speed*1.2
        else:

         if(self.x<=0+20):
            self.angle=225
            self.x += self.speed*1.3
        if (self.x>=750-20):
            self.angle=45
            self.x -= self.speed*1.2
        if(self.y<=0+20):
            self.angle=135
            self.y += self.speed*1.7
        if (self.y>=750-20):
            self.angle=325
            self.y -= self.speed*1.2
        else:
            self.x -= np.sin(self.angle*np.pi/180)*self.speed
            self.y -= np.cos(self.angle*np.pi/180)*self.speed


  
    def despawn(self):
        self.Is_active =False
        self.tempref_respawn = pygame.time.get_ticks()
    def respawn(self):
        if pygame.time.get_ticks() > self.tempref_respawn+self.time_before_respawn:
            self.x=500
            self.y=600
            self.Is_active=True
    def temp_explo(self,explosion):
        if (self.explo and self.temp_explosion<44):

            if (self.temp_explosion==0):

                self.explox=self.x
                self.exploy=self.y
                self.rect_explo=self.image1.image.get_rect(center = (self.explox,self.exploy))


            self.temp_explosion+=1
            pygame.time.delay(1)
            self.screen.blit(explosion.images[self.temp_explosion],self.rect_explo)
        else:
            self.temp_explosion=0
            self.explo=False



class all_ennemies(object):
    def __init__(self,screen):
        self.screen = screen
        self.indice=0
        self.current_ennemies = 3
        self.ennemies_2_kill = self.current_ennemies
        self.max_ennemies = 10
        self.nb_mine_current = 1
        self.nb_thunder_current=1
        self.increase_speed_value = 3
        self.nb_basic_ennemy_current = 1
        self.nb_current_ennemies = 3
        self.ennemies = [basic_ennemy(self.screen) for i in range(self.nb_basic_ennemy_current)]
        self.ennemies_can_respawn = [0 for i in range(self.max_ennemies)] # 0 = inactif 1=actif
        self.respawn_time = 10000 #ms, will decrease step by step
        self.initiale=[]
        self.liste_nb=[self.nb_mine_current,self.nb_basic_ennemy_current,self.nb_thunder_current,self.current_ennemies]


    def update_ennemis_valide(self):
        for k in range(0,self.nb_current_ennemies):
            if self.respawn_time+self.ennemies[k].tempref_respawn>pygame.time.get_ticks():
                self.ennemies_can_respawn[k] = 1
    def ajout_ennemis(self):
        self.ennemies = []
        for t in range(0,self.nb_basic_ennemy_current):
            self.ennemies.append(basic_ennemy(self.screen))
        for s in range(self.nb_mine_current):
            self.ennemies.append(Mine(self.screen))
        for j in range(self.nb_thunder_current):
            self.ennemies.append(thunder_ennemy(self.screen))

    def dessin_ennemis_valide(self,carre):
        for s in range(0,self.nb_current_ennemies):
            if self.ennemies[s].Is_active:
               if hasattr(self.ennemies[s],"mouvement"):
                   if (self.ennemies[s].id!="thunder_ennemy"):
                       self.ennemies[s].mouvement()
                       self.ennemies[s].dessin()
                   else:

                       self.ennemies[s].mouvement(carre)
                       self.ennemies[s].dessin()
               else:
                   self.ennemies[s].dessin()
    def respawn_ennemies_valide(self):
        for s in range(0,self.nb_current_ennemies):
            if not self.ennemies[s].Is_active and self.ennemies_can_respawn[s] == 1:
                
                self.ennemies[s].respawn()
    def increase_speed(self):
        for s in range(0,self.nb_current_ennemies):
            if hasattr(self.ennemies[s],"mouvement"):
                self.ennemies[s].speed += self.increase_speed_value

    def new_basic_ennemy(self,ind):

        self.nb_mine_current-=1
        self.nb_basic_ennemy_current+= 1
        self.ennemies[ind]=basic_ennemy(self.screen)
        self.initiale.append(self.ennemies[ind])
        self.initiale.append(ind)

    def new_thunder(self,ind):

        self.nb_basic_ennemy_current-= 1
        self.nb_thunder_current+=1
        self.ennemies[ind]=thunder_ennemy(self.screen)
        self.initiale.append(self.ennemies[ind])
        self.initiale.append(ind)

    def initialise(self):

        valsup=0
        nb=len(self.initiale)
        for i in range(1,len(self.initiale)+1,2):

            val=i-1
           
            if i==nb-1:
                
                valsup+=2
                
            
            
            
            if self.initiale[val-valsup].id=="thunder_ennemy":
                
                if self.initiale[val-valsup].origin=="Mine":
                    self.nb_mine_current+=1
                    self.nb_thunder_current-= 1



                    self.ennemies[self.initiale[i-valsup]]=Mine(self.screen)
                    del[self.initiale[i-valsup]]
                    del[self.initiale[val-valsup]]
                    valsup=+2
                
                else:
                    self.nb_basic_ennemy_current+= 1
                    self.nb_thunder_current-=1

                    self.ennemies[self.initiale[i-valsup]]=basic_ennemy(self.screen)
               
                    del[self.initiale[i-valsup]]
                
                    del[self.initiale[val-valsup]]
                    valsup=+2



            elif self.initiale[val-valsup].id=="Basic-Ennemy":

                self.nb_mine_current+=1
                self.nb_basic_ennemy_current-= 1



                self.ennemies[self.initiale[i-valsup]]=Mine(self.screen)
                del[self.initiale[i-valsup]]
                del[self.initiale[val-valsup]]
                valsup=+2



    def nb_ennemy(self):
        self.liste_nb[0]=self.nb_mine_current
        self.liste_nb[1]=self.nb_basic_ennemy_current
        self.liste_nb[2]=self.nb_thunder_current
        self.liste_nb[3]=self.nb_mine_current+self.nb_basic_ennemy_current+self.nb_thunder_current

        for i in self.ennemies:
            i.Is_active=True








