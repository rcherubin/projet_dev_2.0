import pygame
import settings as stn
import database as db
from random import randint
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y,name,HP=1000,dmg=200,score=0,lives=5):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.name=name
        self.dmg=dmg
        self.maxHP=HP
        self.HP=self.maxHP
        self.score=score
        self.lives=lives
        self.image=pygame.Surface((60,60))
        self.image.fill(stn.RED)
        # self.image=pygame.image.load(os.path.join(stn.img_folder,img)).convert()
        # self.image.set_colorkey(stn.BLACK)
        self.rect=self.image.get_rect()
        self.rect.center=(self.x,self.y)
        
        
    def update(self):
        #joueur va à gauche
        if self.moveset[0]:
            self.rect.x -= 5
            if self.rect.right<0:
                self.rect.left=stn.WIDTH

        #joueur va à droite
        if self.moveset[1]:
            self.rect.x += 5
            if self.rect.left>stn.WIDTH:
                self.rect.right=0

        #joueur va en haut
        if self.moveset[2]:
            self.rect.y -= 5
            if self.rect.bottom<0:
                self.rect.top=stn.HEIGHT

        #joueur va en bas
        if self.moveset[3]:
            self.rect.y += 5
            if self.rect.top>stn.HEIGHT:
                self.rect.bottom=0
    def changeMoveSet(self, buttons):
        self.moveset = [buttons[0],buttons[1],buttons[2],buttons[3]]
    def decreaseHP(self,dmg):
        self.HP-=dmg
        if self.HP<=0:
            self.respawn()
    def respawn(self):
        self.decreaseScore(100)
        x=randint(50,stn.WIDTH-50)
        y=randint(50,stn.HEIGHT-50)
        self.rect.center=(x,y)
        self.lives-=1
        self.HP=self.maxHP
    def decreaseScore(self,score):
        self.score-=score
        if self.score<0:
            self.score=0
    def increaseScore(self,score):
        self.score+=score
    def takeDamage(self,player):
        self.decreaseHP(player.dmg)
        player.increaseScore(50)
    def changeUsername(self,username):
        if(username!=""):
            self.name=username
            db.insertValue(self,self.pos)
        print(self.name)
        #changement de dégat
    def changeUserDamage(self,damage):
        if(damage!="" and damage.isnumeric()):
            self.Dmg=int(damage)
            #on input change your value is returned here
            db.insertValue(self,self.pos)
        print('Player damage is', self.Dmg)


        #changement de points de vie
    def changePlayerHealth(self,Health):
        if(Health!="" and Health.isnumeric()):
            self.maxHP=float(Health)
            #on input change your value is returned here
            db.insertValue(self,self.pos)
        print('Player health is', self.maxHP)

        #changement de vitesse d'attaque
    def changePlayeratkspd(self,atkspd):
        if(atkspd!="" and atkspd.isnumeric()):
            self.atkSpeed=int(atkspd)
            #on input change your value is returned here
            db.insertValue(self,self.pos)
        print('Player attack speed is', self.atkSpeed)


        #changement de nombre de vies
    def changePlayerLives(self,lives):
        if(lives!="" and lives.isnumeric()):
            self.lives=int(lives)
            #on input change your value is returned here
            db.insertValue(self,self.pos)
        print('Player lives is', self.lives)


        #changement de vitesse de déplacement
    def changePlayerSpeed(self,speed):
        if(speed!="" and speed.isnumeric()):
            self.speed=int(speed)
            #on input change your value is returned here
            db.insertValue(self,self.pos)
        print('Player speed is', self.speed)
