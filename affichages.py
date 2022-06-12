import pygame
import settings as stn
def display(textInput, textColor=stn.GREEN, bgColor=stn.BLUE):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(textInput,True, textColor, bgColor)
    textRect = text.get_rect()
    return textRect, text