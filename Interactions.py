import pygame
import numpy as np
from animation import*
from constantes import*
from sons import*
from Ennemy import*


pygame.mixer.pre_init(44100,-16,2,2048)

pygame.init()

musique=sons()
def calc_offset(objet_rect,objet2_rect):
    offset= (objet_rect[0]-objet2_rect[0], objet_rect[1]-objet2_rect[1])
    return(offset)
def calc_overlap(objet_mask,objet2_mask,offset):
    overlap =objet_mask.overlap(objet2_mask,offset)
    if overlap is not None:
        return(True)
    else:
        return(False)

def collisions_Player_Ennemy(Player,All_ennemies):

    for n in range(0,All_ennemies.nb_current_ennemies): #joueur avec ennemis
        if All_ennemies.ennemies[n].Is_active and Player.Is_active:
            if pygame.sprite.collide_rect(Player.image1,All_ennemies.ennemies[n].image1):
                if pygame.sprite.collide_mask(Player.image1, All_ennemies.ennemies[n].image1):



                    Player.explo=True
                    musique.explose_sound.play()
                    Player.despawn()
                    Player.life -=1

             

def collisions_Balles_Joueur_Ennemy(Player,All_ennemies,rect):

    for s in range(0,All_ennemies.nb_current_ennemies): #balles du joueur avec l'ennemi
        if All_ennemies.ennemies[s].Is_active and Player.Is_active:
            for j in range(0,Player.nb_missiles):
                if Player.stock.missile[j].has_shoot:
                    if pygame.Rect.colliderect(Player.stock.missile[j].image1.rect,All_ennemies.ennemies[s].image1.rect):
                        offset = calc_offset(Player.stock.missile[j].image1.rect,All_ennemies.ennemies[s].image1.rect)

                        if calc_overlap(Player.stock.missile[j].image1.mask,All_ennemies.ennemies[s].image1.mask,offset) is not None:

                            All_ennemies.ennemies[s].explo=True

                            All_ennemies.indice=s

                            musique.explose_sound.play()

                            rect.increase_score(All_ennemies.ennemies[s].value_when_killed)
                            All_ennemies.ennemies[s].despawn()
                            All_ennemies.ennemies_2_kill -=1




def collision_joueur_carre(Player,carre):
        if Player.image1.rect.colliderect(carre.rect):
            offset = (int(carre.rect.x - Player.image1.rect.x), int(carre.rect.y - Player.image1.rect.y))
            overlap = Player.image1.mask.overlap(carre.mask, offset)

            if overlap is not None:
                Player.gliang=-Player.gliang
                if Player.x > carre.x + 1:
                    if Player.y >carre.y +1:
                        if Player.x < carre.x+carre.sizex-1:
                            Player.contact_carre_hb = True# cas ou bas du carré
                            Player.y += Player.speed*1.2
                        else:
                            Player.x += Player.speed*1.2#cas ou coté droit du carré
                    else: #haut du carré
                        Player.y -= Player.speed*1.2
                        Player.contact_carre_hb = True
                else:
                    if  Player.y >carre.y +1:  #gauche du carré
                        Player.x -= Player.speed*1.2
                    else:
                        Player.x += np.sin(Player.angle*np.pi/180)*Player.speed*1.2
                        Player.y += np.cos(Player.angle*np.pi/180)*Player.speed*1.2
                Player.image1.rect = Player.image1.image.get_rect(center = (Player.x,Player.y))

def verifier_collisions_respawn(All_ennemies,Player,rect,ennemy,id_ennemy):
    for n in range(0,id_ennemy):
            offset = calc_offset(All_ennemies.ennemies[n].image1.rect,ennemy.image1.rect)
            if calc_overlap(All_ennemies.ennemies[n].image1.mask,ennemy.image1.mask,offset):
                return(False)
    offset = calc_offset(ennemy.image1.rect,rect.rect)
    if calc_overlap(ennemy.image1.mask,rect.mask,offset):
        return(False)
    offset = calc_offset(ennemy.image1.rect,Player.image1.rect)
    if calc_overlap(ennemy.image1.mask,Player.image1.mask,offset):
        return(False)
    if rect.x+1+rect.sizex > ennemy.x > rect.x - 1:
        if rect.y+1+rect.sizey > ennemy.y > rect.y - 1:
            return(False)
    return(True)

def verifier_les_collisions(All_ennemies,Player,rect):
    collisions_Player_Ennemy(Player,All_ennemies)
    collisions_Balles_Joueur_Ennemy(Player,All_ennemies,rect)
    collision_joueur_carre(Player,rect)
    collisions_Balles_carre(Player,rect)



def bordure(Player):

    if(Player.x<=0+20):
        Player.gliang=-Player.gliang
        Player.contact_carre_gd = True
        Player.x += Player.speed*1.3


    if (Player.x>=750-20):
        Player.gliang=-Player.gliang
        Player.contact_carre_gd = True
        Player.x -= Player.speed*1.2

    if(Player.y<=0+20):

        Player.gliang=-Player.gliang
        Player.contact_carre_hb = True
        Player.y += Player.speed*1.7
    if (Player.y>=750-20):
        Player.gliang=-Player.gliang
        Player.contact_carre_hb = True
        Player.y -= Player.speed*1.2


def collisions_Balles_carre(Player,carre):
     if Player.Is_active:
         for j in range(0,Player.nb_missiles):
             if Player.stock.missile[j].has_shoot:

                 if pygame.Rect.colliderect(Player.stock.missile[j].image1.rect,carre.rect):

                    offset = (int(carre.rect.x - Player.image1.rect.x), int(carre.rect.y - Player.image1.rect.y))
                    overlap = Player.image1.mask.overlap(carre.mask, offset)
                    if calc_overlap(Player.stock.missile[j].image1.mask,carre.mask,offset) is not None:


                        Player.stock.missile[j].has_shoot=False













