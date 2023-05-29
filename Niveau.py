from spawn import*
from constantes import*
class Level(object):
    def __init__(self,screen):
        self.current_level = 0
        self.has_change_of_lv = False
    def generer_niveau_1(self,stock_ennemies,Player,rect):
        stock_ennemies.initialise()
        stock_ennemies.nb_current_ennemies = 3
        stock_ennemies.nb_mine_current = 1
        stock_ennemies.nb_basic_ennemy_current = 1
        stock_ennemies.nb_thunder_current = 1
        stock_ennemies.ajout_ennemis()
        stock_ennemies.ennemies_2_kill = 3
        for k in range(0,stock_ennemies.nb_current_ennemies):
            spawn_valide(stock_ennemies,k,stock_ennemies.ennemies[k],rect,screen_size_x,screen_size_y,Player)
        Player.respawn()
    def generer_niveau_sup_basique(self,stock_ennemies,Player,rect): # niveau sup: on ajoute une mine
        stock_ennemies.initialise()
        stock_ennemies.nb_current_ennemies +=1
        stock_ennemies.nb_mine_current +=1
        stock_ennemies.ajout_ennemis()
        stock_ennemies.ennemies_2_kill = stock_ennemies.nb_current_ennemies
        for k in range(0,stock_ennemies.nb_current_ennemies):
            spawn_valide(stock_ennemies,k,stock_ennemies.ennemies[k],rect,screen_size_x,screen_size_y,Player)
        Player.respawn()
    def generer_niveau_sup_1(self,stock_ennemies,Player,rect): # niveau sup type1: on ajoute un vaisseau basic_ship
        stock_ennemies.initialise()
        stock_ennemies.nb_current_ennemies +=1
        stock_ennemies.nb_basic_ennemy_current += 1
        stock_ennemies.ajout_ennemis()
        stock_ennemies.ennemies_2_kill = stock_ennemies.nb_current_ennemies
        for k in range(0,stock_ennemies.nb_current_ennemies):
            spawn_valide(stock_ennemies,k,stock_ennemies.ennemies[k],rect,screen_size_x,screen_size_y,Player)
        Player.respawn()
    def generer_niveau_sup_2(self,stock_ennemies,Player,rect):

        stock_ennemies.initialise()
        stock_ennemies.nb_current_ennemies +=1
        stock_ennemies.nb_thunder_current +=1
        stock_ennemies.ajout_ennemis()

        for k in range(0,stock_ennemies.nb_current_ennemies):
            spawn_valide(stock_ennemies,k,stock_ennemies.ennemies[k],rect,screen_size_x,screen_size_y,Player)
        Player.respawn()
    def generer_niveau_identique(self,stock_ennemies,Player,rect):
        stock_ennemies.initialise()
        stock_ennemies.ennemies_2_kill = stock_ennemies.nb_current_ennemies
        for k in range(0,stock_ennemies.nb_current_ennemies):
            spawn_valide(stock_ennemies,k,stock_ennemies.ennemies[k],rect,screen_size_x,screen_size_y,Player)
        Player.respawn()

    def generer_niv_respawn(self,stock_ennemies,Player,rect):
        stock_ennemies.initialise()
        for k in range(0,stock_ennemies.liste_nb[3]):
            spawn_valide(stock_ennemies,k,stock_ennemies.ennemies[k],rect,screen_size_x,screen_size_y,Player)

        Player.respawn()


    def augmenter_les_vitesses(self,stock_ennemies,Player,rect):
        stock_ennemies.ajout_ennemis()
        stock_ennemies.increase_speed()
    def generer_niveau_main(self,stock_ennemies,Player,rect):
        if Player.Is_active==False:

            self.generer_niv_respawn(stock_ennemies,Player,rect)
        else:
            if self.current_level == 0:
                self.generer_niveau_1(stock_ennemies,Player,rect)
            elif self.current_level <8:
                if self.current_level==4 or self.current_level ==6:
                    self.generer_niveau_sup_1(stock_ennemies,Player,rect)
                elif self.current_level == 2 or self.current_level==3 or self.current_level==1:
                    self.generer_niveau_sup_basique(stock_ennemies,Player,rect)
                else:
                    self.generer_niveau_sup_2(stock_ennemies,Player,rect)
            else:

                self.augmenter_les_vitesses(stock_ennemies,Player,rect)
                self.generer_niveau_identique(stock_ennemies,Player,rect)
            self.has_change_of_lv =True
