import pygame
import settings as stn

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y,HP=100,dmg=50):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.dmg=dmg
        self.HP=HP
        # self.width = width
        # self.height = height
        self.image=pygame.Surface((60,60))
        self.image.fill(stn.RED)
        # self.image=pygame.image.load(os.path.join(stn.img_folder,img)).convert()
        # self.image.set_colorkey(stn.BLACK)
        self.rect=self.image.get_rect()
        self.rect.center=(self.x,self.y)
        
    # def main(self, display):
    #     pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, self.width, self.height))
        
    def update(self):
        #joueur va à gauche
        if self.moveset[0]:
            self.rect.x -= 5
            # self.prevX=1
            # self.directionX=1
            # self.directionY=0
            if self.rect.right<0:
                self.rect.left=stn.WIDTH


        #joueur va à droite
        if self.moveset[1]:
            self.rect.x += 5
            # self.prevX=1
            # self.directionX=-1
            # self.directionY=0
            if self.rect.left>stn.WIDTH:
                self.rect.right=0

        #joueur va en haut
        if self.moveset[2]:
            prevY=1
            self.rect.y -= 5
            # if self.prevX<=0:
            #     self.directionX=0
            # else:
            #     prevY=0
            # self.directionY=prevY
            if self.rect.bottom<0:
                self.rect.top=stn.HEIGHT

        #joueur va en bas
        if self.moveset[3]:
            prevY=-1
            self.rect.y += 5
            # if self.prevX<=0:
            #     self.directionX=0
            # else:
            #     prevY=0
            # self.directionY=prevY
            if self.rect.top>stn.HEIGHT:
                self.rect.bottom=0
    def changeMoveSet(self, buttons):
        self.moveset = [buttons[0],buttons[1],buttons[2],buttons[3]]