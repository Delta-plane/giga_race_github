import pygame
from pygame.locals import*
pygame.init()
from constantes import*
from Ennemy import*
from Carre_centre import*
from Vaisseau import*
from Missiles import*
from Limite_bordure import*
from Limite_carre_central import*
fenetre = pygame.display.set_mode((screen_size_x,screen_size_y))
rect=Carre_central(fenetre)
Player = Space_ship(fenetre)
Player.teleport()
Player.dessin()

stock = stock_missiles(fenetre)
stock.add_missiles()

Opponent = basic_ennemy(fenetre)
pygame.display.update()
fenetre.fill((0,0,0))

def global_update():
    fenetre.fill((0,0,0))
    Player.dessin()
    stock.dessin_missiles_valide(Opponent)
    Opponent.dessin()
    Opponent.mouvement()
    if Opponent.rect.colliderect(stock.missile[0].rect):
        print("uwu")
    pygame.time.delay(30)
    pygame.display.update()


def main():
    continuer = True
    while continuer:
        global_update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_q:
                    pygame.quit()
                if event.key == K_DOWN:
                    stock.update_missile_valide()
                    stock.current_missile_shoot_id =stock.id_tirer()
                    if stock.current_missile_shoot_id!=stock.nb_missiles +1:
                        stock.missile[stock.current_missile_shoot_id].initialiser_tir(Player)
                        stock.liste_missiles_valides[stock.current_missile_shoot_id] = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            Player.rotation_gauche2()
        if keys[pygame.K_RIGHT]:
            Player.rotation_droite2()
        if keys[pygame.K_UP]:
            Player.mouvement()
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            Player.rotation_gauche2()
            pygame.time.delay(10)
            Player.mouvement()
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            Player.rotation_droite2()
            pygame.time.delay(10)
            Player.mouvement()



    pygame.quit()

main()