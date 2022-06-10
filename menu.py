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
        menu.add.button(i[0]+ " : "+str(i[1]), )
    menu.add.button("Menu Principal", pygame_menu.events.BACK)
    # menu.mainloop(surface)
    return menu