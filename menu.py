import pygame_menu
from settings import WIDTH,HEIGHT
import database as db
def displayScoreBoard():
    menu = pygame_menu.Menu('Score Board', WIDTH, HEIGHT,
                            theme=pygame_menu.themes.THEME_BLUE,)
    # surface = create_example_window('TopDownShooter', (WIDTH, HEIGHT))
    scores=db.getScores()
    for i in scores:
        # displayScoreMenu=scoreOfGame(i[0]+ " : "+str(i[1]),"Score")   
        menu.add.button(i[0]+ "                             "+str(i[1]), )
    menu.add.button("Menu Principal", pygame_menu.events.BACK)
    # menu.mainloop(surface)
    return menu
def modifJoueur(player):
    JoueurModifMenu = pygame_menu.Menu(player.name, WIDTH, HEIGHT,
    theme=pygame_menu.themes.THEME_BLUE)
    JoueurModifMenu.add.text_input('Nom :', default=player.name,onchange=player.changeUsername)
    JoueurModifMenu.add.text_input('Points de vies :', default=str(player.maxHP),onchange=player.changePlayerHealth)
    JoueurModifMenu.add.text_input('dégats :', default=str(player.dmg),onchange=player.changeUserDamage)
    JoueurModifMenu.add.text_input('Vitesse d"attaque :', default=str(player.atkSpeed),onchange=player.changePlayeratkspd)
    JoueurModifMenu.add.text_input('Vitesse de déplacement :', default=str(player.speed),onchange=player.changePlayerSpeed)
    JoueurModifMenu.add.button('Changer', pygame_menu.events.BACK)
    return JoueurModifMenu