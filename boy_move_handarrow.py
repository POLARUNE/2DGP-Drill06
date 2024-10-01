from pico2d import *

import random
import math

open_canvas()
bg = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False


running = True
x = 800 // 2
y = 600 // 2
frame = 0

while running:
    clear_canvas()
    bg.draw(400, 300)
    character.clip_draw(frame*100,100,100,100,x,y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)


close_canvas()
