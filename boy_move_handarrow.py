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

def draw_moving_boy():
    global boy_x, boy_y, arrow_x, arrow_y, i, frame

    t = i / 100

    x = (1 - t)*boy_x + t*arrow_x
    y = (1 - t)*boy_y + t*arrow_y

    if arrow_x>=boy_x:
        boy.clip_draw(frame*100, 100, 100, 100, x, y)
    else:
        boy.clip_composite_draw(frame*100, 100, 100, 100, 0, 'h', x, y, 100, 100)
        pass


def set_arrow_pos():
    global arrow_x, arrow_y
    arrow_x,arrow_y = random.randrange(0,800+1),random.randrange(0,600+1)


running = True
boy_x = 800 // 2
boy_y = 600 // 2
arrow_x = random.randrange(0,800+1)
arrow_y = random.randrange(0,600+1)
frame = 0

while running:
    for i in range(0, 100 + 1):
        clear_canvas()
        bg.draw(400, 300)

        draw_moving_boy()

        arrow.draw(arrow_x, arrow_y)

        update_canvas()
        handle_events()
        frame = (frame + 1) % 8
        delay(0.01)
    boy_x,boy_y = arrow_x,arrow_y
    set_arrow_pos()

close_canvas()
