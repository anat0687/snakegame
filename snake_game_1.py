import pygame as pg
from random import randint as rint


def newfruit ():
    newx = rint(0, xsize/10)*10
    newy = rint(0, ysize/10)*10
    print(newx, newy)

    return newx, newy


pg.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

xsize = 800
ysize = 600
x = int(xsize/2)
y = int(ysize/2)
xchange = 0
ychange = 0
score = 0
fruitx = rint(0, xsize/10)*10
fruity = rint(0, ysize/10)*10

dis = pg.display.set_mode((xsize, ysize))
pg.display.set_caption('Snake')

game_over = False
fruit_toggle = False


while not game_over:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                xchange = -10
                ychange = 0
                break
            elif event.key == pg.K_RIGHT:
                xchange = 10
                ychange = 0
                break
            elif event.key == pg.K_UP:
                xchange = 0
                ychange = -10
                break
            elif event.key == pg.K_DOWN:
                xchange = 0
                ychange = 10
                break

    pg.time.delay(50)
    x = int(x + xchange)
    y = int(y + ychange)

    if x == fruitx and y == fruity:
        score += 1
        print(score)
        fruitx, fruity = newfruit()

    pg.draw.rect(dis, red, [fruitx, fruity, 10, 10])
    pg.display.update()


    if x > xsize or y > ysize or x < 0 or y < 0:
        game_over = True

    dis.fill(white)
    pg.draw.rect(dis, blue, [x, y, 10, 10])

