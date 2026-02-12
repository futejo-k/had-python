# Pohyb
# Kontrola nárazů
# Pohyb v2 zajíždění za obrazovku
# Jídlo


import pygame
import numpy
from enum import Enum


class Smer(Enum):
    NAHORU = 0
    DOLU = 1
    VLEVO = 2
    VPRAVO = 3


pygame.init()
pygame.font.init()

VELIKOST_OKNA = 500
POCET_POLICEK = 30
SIRKA_POLICKA = VELIKOST_OKNA // POCET_POLICEK

mapa = numpy.zeros((POCET_POLICEK, POCET_POLICEK))
had = [[1, 0], [0, 0]]
screen = pygame.display.set_mode((VELIKOST_OKNA, VELIKOST_OKNA))


def vykresliHada():
    count = 0
    for blok in had:
        if count == 0:
            pygame.draw.rect(screen, (255, 0, 0),
                             (blok[0] * SIRKA_POLICKA, blok[1] * SIRKA_POLICKA, SIRKA_POLICKA, SIRKA_POLICKA))
        else:
            pygame.draw.rect(screen, (0, 255, 0),
                             (blok[0] * SIRKA_POLICKA, blok[1] * SIRKA_POLICKA, SIRKA_POLICKA, SIRKA_POLICKA))

        count += 1


def pohybHada():
    hlava = had[0]
    hadNovy = []
    if smer == Smer.NAHORU:
        hadNovy.append([hlava[0], hlava[1] - 1])
    elif smer == Smer.DOLU:
        hadNovy.append([hlava[0], hlava[1] + 1])
    elif smer == Smer.VLEVO:
        hadNovy.append([hlava[0] - 1, hlava[1]])
    elif smer == Smer.VPRAVO:
        hadNovy.append([hlava[0] + 1, hlava[1]])


smer = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                smer = Smer.NAHORU
            elif event.key == pygame.K_DOWN:
                smer = Smer.DOLU
            elif event.key == pygame.K_LEFT:
                smer = Smer.VLEVO
            elif event.key == pygame.K_RIGHT:
                smer = Smer.VPRAVO

    print(smer)
    screen.fill((144, 144, 144))
    vykresliHada()

    pygame.display.update()


