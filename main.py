import pygame
from pygame.locals import*
pygame.init()
import pygame, sys
from Ennemy import*
from Carre_centre import*
from Vaisseau import*
from Missiles import*
from Interactions import*
from Updates import*
from Input import*
from Niveau import*
from spawn import*
from constantes import*
from Interactions import*
from sons import*
from animation import*
from pygame import mixer


rect=Carre_central(fenetre)
Player = Space_ship(fenetre)
stock = stock_missiles(fenetre)
stock_ennemies = all_ennemies(fenetre)
stock_ennemies.ajout_ennemis()
Niveau_jeu = Level(fenetre)
pygame.display.update()
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.mixer.pre_init(44100,-16,2,2048)

pygame.init()
pygame.display.set_caption('OMEGA RACE')
#def des polices
mini_police=pygame.font.SysFont("monospace",20,bold=True)
police_titre = pygame.font.SysFont("monospace" ,80)
police = pygame.font.SysFont("monospace" ,60)
petite_police=pygame.font.SysFont("monospace",30)
background=pygame.image.load("background1.jpg")
background1=pygame.image.load("background_jeu.jpg")
background2=pygame.image.load("background2.jpg")
DEFAULT_IMAGE_SIZE=(750,750)
background_menu= pygame.transform.scale(background, DEFAULT_IMAGE_SIZE)
background_jeu= pygame.transform.scale(background1, DEFAULT_IMAGE_SIZE)
background_menu1=pygame.transform.scale(background2, DEFAULT_IMAGE_SIZE)

fleche=pygame.image.load("fleche.png")
fleche=pygame.transform.scale(fleche, (75,75))
fleche_gauche=pygame.transform.rotate(fleche,90)
fleche_bas=pygame.transform.rotate(fleche,180)
fleche_droite=pygame.transform.rotate(fleche,270)

def affiche_texte(texte,police, x, y, couleur,fenetre):
    text=police.render(texte,1,couleur)
    fenetre.blit(text,(x,y))

def ecran_defaite(police,fenetre):
    color = (255,0,0)
    x = 125
    y = 0
    text_game_over = police.render("GAME OVER !",False,color)
    while y< screen_size_y/2:
        fenetre.fill((0,0,0))
        fenetre.blit(text_game_over,(x,y))
        y += int(0.01*screen_size_y)
        pygame.display.update()
        pygame.time.delay(25)

def menu_principal():
     click =False
     pygame.mixer.music.load("GIGACHAD_Theme.mp3")
     mixer.music.play(-1)
     pygame.mixer.music.set_volume(0.5)
     rester_dans_menu = True
     while rester_dans_menu:





        fenetre.fill((0,0,0))
        fenetre.blit(background_menu,(0,0))


        affiche_texte('OMEGA RACE', police_titre,130,20, (255, 255, 255), fenetre)

        mx, my = pygame.mouse.get_pos()

        bouton_2 = pygame.Rect(175, 400, 400, 100)
        bouton_1 = pygame.Rect(175, 200, 400, 100)

        pygame.draw.rect(fenetre, (255, 255, 255), bouton_1,5)
        pygame.draw.rect(fenetre, (255, 255, 255), bouton_2,5)
        affiche_texte('options', police,250,410, (255, 255, 255), fenetre)
        affiche_texte('game', police,300,215, (255, 255, 255), fenetre)
        if bouton_1.collidepoint((mx, my)):
            if click:
                rester_dans_menu = False
                jeu()
        if bouton_2.collidepoint((mx, my)):
            if click:
                options()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def jeu():
    pygame.mixer.music.load("musique_jeu.mp3")
    mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    Player.life = Player.max_life
    rect.dessin()
    rect.score()
    Niveau_jeu.current_level = 0
    while Player.life >0:
        Player.stock.despawn_chgmt_lv()
        Niveau_jeu.generer_niveau_main(stock_ennemies,Player,rect)
        continuer = True
        while continuer:
            global_update(Player,stock_ennemies,rect,continuer,Niveau_jeu)
            if Niveau_jeu.has_change_of_lv:
                pygame.time.delay(750)
                Niveau_jeu.has_change_of_lv = False
            gerer_input(Player,rect,stock_ennemies)
            if Player.Is_active==False:
                stock_ennemies.nb_ennemy()
                Niveau_jeu.generer_niveau_main(stock_ennemies,Player,rect)
                stock_ennemies.nb_mine_current=stock_ennemies.liste_nb[0]
                stock_ennemies.nb_basic_ennemy_current=stock_ennemies.liste_nb[1]
                stock_ennemies.nb_thunder_current=stock_ennemies.liste_nb[2]
                stock_ennemies.current_ennemies = stock_ennemies.liste_nb[3]
                stock_ennemies.nb_current_ennemies = stock_ennemies.liste_nb[3]
                stock_ennemies.ennemies_2_kill=stock_ennemies.liste_nb[3]
            if  not stock_ennemies.ennemies_2_kill > 0 or Player.life<1:
                continuer = False
                Niveau_jeu.current_level +=1
    if Player.life == 0:
        fenetre.fill((0,0,0))
        ecran_defaite(police_titre,fenetre)
        pygame.time.delay(1000)
        rect.chgmt_highscore()
        print(rect.hs_value)
        menu_principal()

def options():
    running = True
    click=False
    while running:
        fenetre.fill((0,0,0))

        fenetre.blit(background_menu1,(0,0))

        mx, my = pygame.mouse.get_pos()
        bouton_3 = pygame.Rect(175, 600, 400, 100)
        bouton_2 = pygame.Rect(175, 400, 400, 100)
        bouton_1 = pygame.Rect(175, 200, 400, 100)


        if bouton_1.collidepoint((mx, my)):
            if click:
                paramètre()

        if bouton_2.collidepoint((mx, my)):
            if click:
                touches()

        

        click = False
        pygame.draw.rect(fenetre, (255, 255, 255), bouton_1,5)
        pygame.draw.rect(fenetre, (255, 255, 255), bouton_2,5)
       
        affiche_texte('Options:', police_titre,180,50, (255, 255, 255), fenetre)
        affiche_texte('commandes', police,215,410, (255, 255, 255), fenetre)
        affiche_texte('gameplay', police,230,215, (255, 255, 255), fenetre)
        




        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def touches():
    running = True

    while running:
        fenetre.fill((0,0,0))

        fenetre.blit(background_menu1,(0,0))

        mx, my = pygame.mouse.get_pos()

        fenetre.blit(fleche,(0,290))
        fenetre.blit(fleche_bas,(0,170))
        fenetre.blit(fleche_gauche,(10,480))
        fenetre.blit(fleche_droite,(0,390))


        affiche_texte('commandes:', police_titre,100,50, (255, 255, 255), fenetre)
        affiche_texte('tirer', petite_police,100,200, (255, 255, 255), fenetre)
        affiche_texte('avancer', petite_police,100,300, (255, 255, 255), fenetre)
        affiche_texte('tourner vers la droite', petite_police,100,400, (255, 255, 255), fenetre)
        affiche_texte('tourner vers la gauche', petite_police,100,500, (255, 255, 255), fenetre)




        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)




def paramètre():
    running = True

    while running:
        fenetre.fill((0,0,0))

        fenetre.blit(background_menu1,(0,0))

        mx, my = pygame.mouse.get_pos()
        fenetre.blit(Player.image1.image,(30,300))
        fenetre.blit(stock_ennemies.ennemies[0].image1.image,(50,500))
        fenetre.blit(stock_ennemies.ennemies[1].image1.image,(50,580))
        fenetre.blit(stock_ennemies.ennemies[2].image1.image,(50,650))
        affiche_texte('Gameplay:', police_titre,150,50, (255, 255, 255), fenetre)
        affiche_texte('Joueur:', police,50,200, (255, 255, 255), fenetre)
        affiche_texte('Un vaisseau capable de se déplacer rapidement dans', mini_police,120,270, (255, 255, 255), fenetre)
        affiche_texte('tous les sens et de tirer jusqu\'à 4 missiles qui se', mini_police,120,285, (255, 255, 255), fenetre)
        affiche_texte('rechargent petit à petit mais en contre-partie le', mini_police,120,300, (255, 255, 255), fenetre)
        affiche_texte('vaisseau ne peut pas s\'arrêter quand il le souhaite ', mini_police,120,315, (255, 255, 255), fenetre)
        affiche_texte('et n\'a pas de défense, il explose au premier contact', mini_police,120,330, (255, 255, 255), fenetre)
        affiche_texte('avec un ennemi.', mini_police,120,345, (255, 255, 255), fenetre)
        affiche_texte('Ennemi:', police,50,400, (255, 255, 255), fenetre)
        
        affiche_texte('Un vaisseau ennemi qui tourne autour du', mini_police,120,505, (255, 255, 255), fenetre)
        affiche_texte('carre centrale mais attention au bout d\'un certain', mini_police,120,520, (255, 255, 255), fenetre)
        affiche_texte('temps il se transforme en éclair.', mini_police,120,535, (255, 255, 255), fenetre)
        
        affiche_texte('Une tnt qui ne bouge pas mais comme le vaisseau', mini_police,120,570, (255, 255, 255), fenetre)
        affiche_texte('ennemi se transforme au bout d\'un certain temps.', mini_police,120,585, (255, 255, 255), fenetre)
        
        affiche_texte('L\'ennemi qui est de loin le plus dangereux,' ,mini_police,120,640, (255, 255, 255), fenetre)
        affiche_texte('l\'éclair à des mouvements diagonaux qui le rend', mini_police,120,655, (255, 255, 255), fenetre)
        affiche_texte('difficile à toucher.', mini_police,120,670, (255, 255, 255), fenetre)






        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)



menu_principal()

