import pygame as pg

pg.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

xsize = 800
ysize = 600

clock = pg.time.Clock()


dis = pg.display.set_mode((xsize, ysize))
pg.display.set_caption('Snake')
game_over = False


x = int(xsize/2)
y = int(ysize/2)

while not game_over:

    xchange = 0
    ychange = 0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                xchange = -10
                ychange = 0
            elif event.key == pg.K_RIGHT:
                xchange = 10
                ychange = 0
            elif event.key == pg.K_UP:
                xchange = 0
                ychange = -10
            elif event.key == pg.K_DOWN:
                xchange = 0
                ychange = 10

        x = int(x + xchange)
        y = int(y + ychange)
        dis.fill(white)
        pg.draw.rect(dis, blue, [x, y, 10, 10])

        pg.display.update()

        clock.tick(3000)

        #print(event)

pg.quit()
quit()


