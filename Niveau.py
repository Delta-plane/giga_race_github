from spawn import*
from constantes import*
def generer_niveau_2(stock_ennemies,Player,rect):
    stock_ennemies.nb_current_ennemies = 5
    stock_ennemies.nb_basic_ennemy_current = 2
    stock_ennemies.nb_mine_current = 3
    stock_ennemies.ajout_ennemis()
    stock_ennemies.ennemies_2_kill = stock_ennemies.nb_current_ennemies
    for k in range(0,stock_ennemies.nb_current_ennemies):
        spawn_valide(stock_ennemies,k,stock_ennemies.ennemies[k],rect,screen_size_x,screen_size_y,Player)