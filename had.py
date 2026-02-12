# Pohyb
# Kontrola nárazů
# Pohyb v2 zajíždění za obrazovku
# Jídlo


import pygame
import numpy
from enum import Enum
import random as rnd


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
clock = pygame.time.Clock()

smer = Smer.VPRAVO
jidlo = [rnd.randint(0, POCET_POLICEK-1), rnd.randint(0, POCET_POLICEK-1)]


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

def vykresliJidlo():
    pygame.draw.rect(screen, (0, 0, 255), (jidlo[0] * SIRKA_POLICKA, jidlo[1] * SIRKA_POLICKA, SIRKA_POLICKA, SIRKA_POLICKA))

def pohybHada():
    global jidlo, running
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

    nova_hlava = hadNovy[0]

    nova_hlava[0] = nova_hlava[0] % POCET_POLICEK
    nova_hlava[1] = nova_hlava[1] % POCET_POLICEK

    if nova_hlava in had:
        running = False
        return

    had.insert(0, nova_hlava)

    if nova_hlava == jidlo:
        while True:
            nove_jidlo = [rnd.randint(0, POCET_POLICEK-1), rnd.randint(0, POCET_POLICEK-1)]
            if nove_jidlo not in had:
                jidlo = nove_jidlo
                break
    else:
        had.pop()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and smer != Smer.DOLU:
                smer = Smer.NAHORU
            elif event.key == pygame.K_DOWN and smer != Smer.NAHORU:
                smer = Smer.DOLU
            elif event.key == pygame.K_LEFT and smer != Smer.VPRAVO:
                smer = Smer.VLEVO
            elif event.key == pygame.K_RIGHT and smer != Smer.VLEVO:
                smer = Smer.VPRAVO

    print(smer)
    screen.fill((144, 144, 144))

    pohybHada()
    vykresliHada()
    vykresliJidlo()

    pygame.display.update()
    clock.tick(10)


