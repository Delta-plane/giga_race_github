from constantes import*
from Interactions import*
def global_update(Player,stock_ennemies,rect):
    fenetre.fill((0,0,0))
    Player.dessin()
    #stock_ennemies.update_ennemis_valide()
    #stock_ennemies.respawn_ennemis_valide()
    stock_ennemies.dessin_ennemis_valide()
    rect.dessin()
    Player.stock.dessin_missiles_valide()
    verifier_les_collisions(stock_ennemies,Player,rect)
    pygame.time.delay(30)
    pygame.display.update()

