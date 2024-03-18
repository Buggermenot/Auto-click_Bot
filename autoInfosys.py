import time

import pyautogui as pg
from PIL import ImageGrab

play_button_cell = (744, 630)       # Cell to check if play button
play_color = (106, 112, 120)

play_bar_cell = (1240, 970)         # Cell to check if play bar is present
play_bar_color = (30, 36, 44)

next_button = (1244, 510)           # Click position for next button
seek_to = (1015, 965)               # Click position for seeking

def click(pos: tuple[int, int]):
    x, y, = pos
    print("Clicked", pos)
    pg.moveTo(x, y)
    # time.sleep(4)
    pg.click()

def play_enabled():
    return ImageGrab.grab().getpixel(play_button_cell) == play_color

def play_video():
    global move
    while not play_enabled():
        pass
    print("Play Video")
    click(play_button_cell)
    move = 1

def seek_enabled():
    return ImageGrab.grab().getpixel(play_bar_cell) == play_bar_color

def seek_ahead():
    global move
    while not seek_enabled():
        pass
    time.sleep(1.5)
    print("Seek Ahead")
    click(seek_to)
    move = 2

def next_video():
    global move, loops
    print("Next Video")
    click(next_button)
    move = 0
    loops += 1


def loop():
    global moves, move
    while True:
        moves[move]()

loops = 1
move = 0
moves = [play_video, seek_ahead, next_video]

if __name__ == '__main__':
    time.sleep(5)       # Buffer time
    loop()
