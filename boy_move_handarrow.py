from pico2d import *

import random
import math

open_canvas()
bg = load_image('TUK_GROUND.png')
boy = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

def move_boy():
    pass

def set_arrow_dir():
    global arrow_x, arrow_y
    arrow_x,arrow_y = random.randrange(0,800+1),random.randrange(0,600+1)


running = True
boy_x = 800 // 2
boy_y = 600 // 2
arrow_x = random.randrange(0,800+1)
arrow_y = random.randrange(0,600+1)
frame = 0

while running:
    clear_canvas()
    bg.draw(400, 300)
    boy.clip_draw(frame*100,100,100,100,boy_x,boy_y)
    arrow.draw(arrow_x,arrow_y)

    move_boy()
    if boy_x == arrow_x and boy_y == arrow_y:
        set_arrow_dir()

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)


close_canvas()
