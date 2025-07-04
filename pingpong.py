from pygame import *

# GAME WINDOW -----------
win_width = 300
win_height = 600
img_back = "foto.jpg"
display.set_caption("[PINGFROM THE PONG]")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))


#DATA GAME
finish = False #the "game is over" variable: as soon as True is there, sprites stop working in the main loop
run = True #the flag is reset by the window close button

# GAME LOOPS -----------
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(background,(0,0))
        display.update()


