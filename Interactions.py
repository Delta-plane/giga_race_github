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



def verifier_les_collisions(All_ennemies,Player):
    for n in range(0,All_ennemies.nb_current_ennemies): #joueur avec ennemis
        if All_ennemies.ennemies[n].Is_active and Player.Is_active:
            offset = calc_offset(All_ennemies.ennemies[n].rect,Player.rect)
            if calc_overlap(All_ennemies.ennemies[n].mask,Player.mask,offset):
             print("collision entre joueur et l'ennemi numéro:",n)
            for k in range(0,All_ennemies.ennemies[n].nb_missiles): #balles de l'ennemi avec le joueur
                if All_ennemies.ennemies[n].missile.has_shoot:
                    offset = calc_offset(All_ennemies.ennemies[n].missile.rect,Player.rect)
                    if calc_overlap(All_ennemies.ennemies[n].missile.mask,Player.mask,offset):
                     print("collision entre le joueur et du missile",k ,"de l'ennemi numéro",n)
    for s in range(0,All_ennemies.nb_current_ennemies):
        if All_ennemies.ennemies[s].Is_active and Player.Is_active:
            for j in range(0,Player.nb_missiles):
                offset = calc_offset(Player.stock.missile[j].rect,All_ennemies.ennemies[s].rect)
                if calc_overlap(Player.stock.missile[j].mask,All_ennemies.ennemies[s].mask,offset):
                    print("collison entre le missile ",j,"du joueur et l'ennemi numero",s)


