import pygame
from pygame.locals import*
pygame.init()
import objets
from constantes import*
fenetre = pygame.display.set_mode((screen_size_x,screen_size_y))
rect=objets.Carre_central(fenetre)
rect.dessin()
rect.score()
Player = objets.Triangle(fenetre)
Player.generer_Liste_config_angle()
Player.dessin()
Missile = objets.weapon(fenetre)
Missile1 = objets.weapon(fenetre)
Missile2 = objets.weapon(fenetre)
Missile3 = objets.weapon(fenetre)
stock = objets.stock_missiles(fenetre)
stock.add_missiles()
pygame.display.update()
fenetre.fill((0,0,0))

def id_tirer(stock):
    for n in range(0,stock.nb_missiles):
        if stock.liste_missiles_valides[n]==1:
            return(n)
    return(stock.nb_missiles+1)

def missiles_a_lancer():
    for s in range(0,stock.nb_missiles):
        if stock.liste_missiles_valides[s]==0:
            objets.tirer(stock.missile[s],Player,stock.missile[s].tempref)
            stock.missile[s].dessin()




def global_update():
        pygame.time.delay(100)
        fenetre.fill((0,0,0))
        rect.dessin()
        rect.score()
        Player.rebond_mur()
        Player.dessin()
        missiles_a_lancer()
        pygame.display.flip()




def main():
    continuer = True
    while continuer:
        global_update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    continuer = False
                if event.key == pygame.K_LEFT:
                    Player.rotation_gauche()
                if event.key == pygame.K_RIGHT:
                    Player.rotation_droite()
                if event.key==pygame.K_UP:
                    Player.mouvement()
                if event.key==pygame.K_DOWN:
                    stock.update_missile_valide()
                    stock.current_missile_shoot_id =id_tirer(stock)

                    if stock.current_missile_shoot_id!=stock.nb_missiles +1:
                        objets.transfert_vers_vaisseau(stock.missile[stock.current_missile_shoot_id],Player)
                        stock.missile[stock.current_missile_shoot_id].initialiser_tir()
                        stock.liste_missiles_valides[stock.current_missile_shoot_id] = 0
                        print("val",stock.current_missile_shoot_id)


    pygame.quit()

main()