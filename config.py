# Configurações do jogo
from os import path
import pygame

largura = 580
altura = 700
fps = 60

Imagens = path.join(path.dirname(__file__), 'assets', 'img')
Fontes = path.join(path.dirname(__file__), 'assets', 'fonts')
Botoes = path.join(path.dirname(__file__), 'assets', 'img', 'Botoes')

quit = 0
iniciando = 1
jogando = 2
skins = 3

# Cores principais

Roxo = (99,46,98)
