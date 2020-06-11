import pygame as pg
from random import randint as rint


def new_fruit():
    new_x = rint(0, x_size / 10 - 1) * 10
    new_y = rint(0, y_size / 10 - 1) * 10
    return new_x, new_y


pg.init()

white = (200, 200, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

x_size = 500
y_size = 300
x = int(x_size / 2)
y = int(y_size / 2)
x_change = 0
y_change = 0
score = 0
fruit_x, fruit_y = new_fruit()
tail = [[x, y]]


dis = pg.display.set_mode((x_size, y_size))
pg.display.set_caption('Snake')

game_over = False
started = False

while not game_over:
    dis.fill(white)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True
        if event.type == pg.KEYDOWN:
            started = True
            if event.key == pg.K_a:
                x_change = -10
                y_change = 0
                break
            elif event.key == pg.K_d:
                x_change = 10
                y_change = 0
                break
            elif event.key == pg.K_w:
                x_change = 0
                y_change = -10
                break
            elif event.key == pg.K_s:
                x_change = 0
                y_change = 10
                break

    pg.time.delay(50)

    x = int(x + x_change)
    y = int(y + y_change)

    if started and [x, y] in tail:
        game_over = True

    tail[0][0] = x
    tail[0][1] = y

    if x == fruit_x and y == fruit_y:
        score += 1
        fruit_x, fruit_y = new_fruit()
        tail.append([x, y])

    for i in reversed(range(len(tail))):
        pg.draw.rect(dis, blue, [tail[i][0], tail[i][1], 10, 10])
        tail[i][0] = tail[i-1][0]
        tail[i][1] = tail[i-1][1]

    if x > x_size or y > y_size or x < 0 or y < 0:
        game_over = True

    pg.draw.rect(dis, red, [fruit_x, fruit_y, 10, 10])
    pg.display.update()




