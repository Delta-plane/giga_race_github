from constantes import*
from Interactions import*
from animation import*
from transfo import*

import pygame
background1=pygame.image.load("background_jeu.jpg")
DEFAULT_IMAGE_SIZE=(750,750)
background_jeu= pygame.transform.scale(background1, DEFAULT_IMAGE_SIZE)
def global_update(Player,stock_ennemies,rect,continuer,Niveau):
    fenetre.fill((0,0,0))
    fenetre.blit(background_jeu,(0,0))

    timer(stock_ennemies.ennemies)
    if Player.Is_active:
        Player.dessin()
    else:

        Player.respawn_apres_mort()
        
    stock_ennemies.dessin_ennemis_valide(rect)
    bordure(Player)
    rect.dessin()
    rect.score()
    Player.stock.dessin_missiles_valide()
    verifier_les_collisions(stock_ennemies,Player,rect)
    if Player.life !=Player.max_life:
        if (Player.explo):
            explosion=Explose(Player.explox,Player.exploy,fenetre)
            Player.temp_explo(explosion)
    if Player.life !=0:
        if(stock_ennemies.ennemies[stock_ennemies.indice].explo):
            explosion=Explose(stock_ennemies.ennemies[stock_ennemies.indice].explox,stock_ennemies.ennemies[stock_ennemies.indice].exploy,fenetre)
            stock_ennemies.ennemies[stock_ennemies.indice].temp_explo(explosion)
    transformation(stock_ennemies.ennemies,stock_ennemies)
    pygame.time.delay(30)
    pygame.display.update()

