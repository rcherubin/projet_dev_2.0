import pygame
import sys
import pygame_menu
import menu as mn
from player import Player
from ball import Ball
import settings as stn
import database as db
import affichages as affiche
from pygame_menu.examples import create_example_window
pygame.init()
display = pygame.display.set_mode((stn.WIDTH, stn.HEIGHT))
clock = pygame.time.Clock()
player1 = Player(400, 300,"Cherubin",stn.WHITE)
player2 = Player(100, 100,"Ted",stn.RED)
def start_the_game():

    players_sprites = pygame.sprite.Group() # tous les sprites
    bullets_P1=pygame.sprite.Group() # la sprite des bulletes du joueur 1 
    bullets_P2=pygame.sprite.Group() # la sprite des bulletes du joueur 2
    players_sprites.add(player1) # ajout du joueur 1 dans le groupe des sprites
    players_sprites.add(player2) # ajout du joueur 2 dans le groupe des sprites

    while True:
        display.fill((22, 165, 89))
        textBox1,text1=affiche.display(player1.name+" : "+str(player1.score))
        textBoxHP1,textHP1=affiche.display("HP : "+str(player1.HP))
        # set the center of the rectangular object.
        textBox1.topleft = (0,0)
        textBoxHP1.topleft = (0,40)
        # textRectLives1.topleft = (0,70)
        textBox2,text2=affiche.display(player2.name+" : "+str(player2.score))
        textBoxHP2,textHP2=affiche.display("HP : "+str(player2.HP))
        textBox2.topright = (stn.WIDTH,0)
        textBoxHP2.topright = (stn.WIDTH,40)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.QUIT
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    bullets_P1.add(Ball(player1.rect.x, player1.rect.y, mouse_x, mouse_y))
                if event.key==pygame.K_RETURN:
                    bullets_P2.add(Ball(player2.rect.x, player2.rect.y, mouse_x, mouse_y))
                
        keys = pygame.key.get_pressed()
        
        player1.changeMoveSet([keys[pygame.K_q],keys[pygame.K_d],keys[pygame.K_z],keys[pygame.K_s]])
        player2.changeMoveSet([keys[pygame.K_LEFT],keys[pygame.K_RIGHT],keys[pygame.K_UP],keys[pygame.K_DOWN]])
        players_sprites.update()
        bullets_P1.update()
        bullets_P2.update()
        #collision des bullets avec la victime
        hit_On_P1=pygame.sprite.spritecollide(player1,bullets_P2,True)
        if hit_On_P1:
            print("player1 touché par un bullet")
            player1.takeDamage(player2)
            print(player1.HP)
        hit_On_P2=pygame.sprite.spritecollide(player2,bullets_P1,True)
        if hit_On_P2:
            print("player2 touché par un bullet")
            player2.takeDamage(player1)
        if player2.HP<=0 or player1.HP<=0:
            if player1.score>player2.score:
                gameOverText=player1.name+" est le gagnant avec "+str(player1.score)+" de score!!!"
                db.insertWinner(player1)
            else:
                gameOverText=player2.name+" est le gagnant avec "+str(player2.score)+" de score!!!"
                db.insertWinner(player2)
            scoreEndGame(gameOverText)
            break
        
        
        
        clock.tick(60)
        players_sprites.draw(display)
        bullets_P1.draw(display)
        bullets_P2.draw(display)
        display.blit(text1, textBox1)
        display.blit(textHP1, textBoxHP1)
        display.blit(text2, textBox2)
        display.blit(textHP2, textBoxHP2)
        pygame.display.update()
def menuPrincipal():
    displayScoreBoard=mn.displayScoreBoard()
    modification_joueur1=mn.modifJoueur(player1)
    modification_joueur2=mn.modifJoueur(player2)
    menu = pygame_menu.Menu('Welcome', stn.WIDTH, stn.HEIGHT,
                        theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button('Play',start_the_game)
    menu.add.button('Changer joueur 1', modification_joueur1)
    menu.add.button('Changer joueur 2', modification_joueur2)
    menu.add.button('High Scores', displayScoreBoard)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    surface = create_example_window('TopDownShooter', (stn.WIDTH, stn.HEIGHT))
    menu.mainloop(surface)
def scoreEndGame(str):
    # menu_Principal=menuPrincipal()
    menu = pygame_menu.Menu("Game Over", stn.WIDTH, stn.HEIGHT,
                            theme=pygame_menu.themes.THEME_BLUE,)
    surface = create_example_window('TopDownShooter', (stn.WIDTH, stn.HEIGHT))
    # menu.add.button("Menu Principal", menuPrincipal(funcStart))
    menu.add.button(str, )
    menu.add.button("Menu Principal", menuPrincipal)
    menu.mainloop(surface)
menuPrincipal()
    