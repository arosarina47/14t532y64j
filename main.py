from pygame import*

window = display.set_mode((500,700))
display.set_caption('Доганялки')
background = transform.scale(image.load("background.png"),(500,700)
clock = time.Clock()
FPS = 60
run = True #запуск циклу
x1 = 100
y1 = 350
sprite1 = transform.scale(image.load('sprite1.png'), (100,100))
x2 = 400
y2 = 350
sprite2 = transform.scale(image.load('sprite1.png'), (100,100))
while True:
    window.blit(background,(0,0))
    window.blit(sprite1, (x1,y1))
    window.blit(sprite2, (x2, y2))
    for e in event.get():
        if e.type == QUIT:
            run = False

    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= 10
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += 10
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= 10

    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += 10
    display.update()
    clock.tick(FPS)

