import pygame
import numpy as np
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
            offset = calc_offset(All_ennemies.ennemies[n].rect,Player.rect)
            #if calc_overlap(All_ennemies.ennemies[n].mask,Player.mask,offset):
             #print("collision entre joueur et l'ennemi numéro:",n)
            for k in range(0,All_ennemies.ennemies[n].nb_missiles): #balles de l'ennemi avec le joueur
                if All_ennemies.ennemies[n].missile.has_shoot:
                    offset = calc_offset(All_ennemies.ennemies[n].missile.rect,Player.rect)
                    if calc_overlap(All_ennemies.ennemies[n].missile.mask,Player.mask,offset):
                     print("collision entre le joueur et du missile",k ,"de l'ennemi numéro",n)

def collisions_Balles_Joueur_Ennemy(Player,All_ennemies,rect):
    for s in range(0,All_ennemies.nb_current_ennemies): #balles du joueur avec l'ennemi
        if All_ennemies.ennemies[s].Is_active and Player.Is_active:
            for j in range(0,Player.nb_missiles):
                if Player.stock.missile[j].has_shoot:
                    if pygame.Rect.colliderect(Player.stock.missile[j].rect,All_ennemies.ennemies[s].rect):
                        offset = calc_offset(Player.stock.missile[j].rect,All_ennemies.ennemies[s].rect)
                        if calc_overlap(Player.stock.missile[j].mask,All_ennemies.ennemies[s].mask,offset) is not None:
                            rect.increase_score(All_ennemies.ennemies[s].value_when_killed)
                            All_ennemies.ennemies[s].despawn()
                            print("collison entre le missile ",j,"du joueur et l'ennemi numero",s)

def collision_joueur_carre(Player,carre):
        if Player.rect.colliderect(carre.rect):
            offset = (int(carre.rect.x - Player.rect.x), int(carre.rect.y - Player.rect.y))
            overlap = Player.mask.overlap(carre.mask, offset)
            print(overlap)
            if overlap is not None:
                    print("Collision au pixel près détectée !")
                    Player.x+=np.sin(Player.angle*np.pi/180)*Player.speed
                    Player.y+=np.cos(Player.angle*np.pi/180)*Player.speed
                    Player.rect = Player.image1.get_rect(center = (Player.x,Player.y))


def verifier_les_collisions(All_ennemies,Player,rect):
    collisions_Player_Ennemy(Player,All_ennemies)
    collisions_Balles_Joueur_Ennemy(Player,All_ennemies,rect)
    collision_joueur_carre(Player,rect)



