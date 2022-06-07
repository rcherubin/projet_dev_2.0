import pygame
import sys
import pygame_menu
from player import Player
from ball import Ball
import settings as stn
from pygame_menu.examples import create_example_window
pygame.init()
display = pygame.display.set_mode((stn.WIDTH, stn.HEIGHT))
clock = pygame.time.Clock()
def start_the_game():



    player1 = Player(400, 300)
    player2 = Player(100, 100)
    players_sprites = pygame.sprite.Group() # tous les sprites
    bullets_P1=pygame.sprite.Group() # la sprite des bulletes du joueur 1 
    bullets_P2=pygame.sprite.Group() # la sprite des bulletes du joueur 2
    players_sprites.add(player1) # ajout du joueur 1 dans le groupe des sprites
    players_sprites.add(player2) # ajout du joueur 2 dans le groupe des sprites

    while True:
        display.fill((22, 165, 89))
        
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
        if player2.lives<=0 or player1.lives<=0:
            scoreEndGame("Game Over")
            break
        
        
        
        clock.tick(60)
        players_sprites.draw(display)
        bullets_P1.draw(display)
        bullets_P2.draw(display)
        pygame.display.update()
def menuPrincipal():
    menu = pygame_menu.Menu('Welcome', stn.WIDTH, stn.HEIGHT,
                        theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button('Play',start_the_game)
    # menu.add.button('Change Player 1', change_Player1_menu)
    # menu.add.button('Change Player 2', change_Player2_menu)
    # menu.add.button('High Scores', ScoreBoard)
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
    