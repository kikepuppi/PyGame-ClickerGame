# O JOGO

import pygame
import os 
from config import largura, altura, fps, iniciando, quit, jogando, skins 
from telainicial import telainicial
from telajogo import telajogo
from telaskins import telaskins

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Beringela Clicker ')

state = iniciando
while state != quit:
    if state == iniciando:
        state = telainicial(tela)
    elif state == jogando:
        state = telajogo(tela)
    elif state == skins:
        state = telaskins(tela)
    else:
        state = quit

pygame.quit()