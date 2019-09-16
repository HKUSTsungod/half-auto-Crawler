from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import random

m = PyMouse()
k = PyKeyboard()


video_end = [603, 648]
refresh = [89.2, 89.7] # refresh page
play = [404, 443] # play video
m3u8 = [1041.4, 369.4] # choose m3u8 request
copy = [1088.7, 491.2] # copy of right-click
copy_response = [1317.28, 511.71] # copy-response button
chrome = [663, 864] # chrome in the dock
finder = [133, 864] # finder in the dock

new_file = [1021.7, 366.9]
new_m3u8 = [1018.6, 412.5]
save = [839.7, 330.5]
close_file = [155.6, 74.5]

m.click(chrome[0], chrome[1], 1)

time.sleep(0.5)
for x in range(220):
    rand = random.randint(2, 10) / 8.0

    m.click(m3u8[0], m3u8[1], 1, 1)
    time.sleep(1 + rand / 2)
    m.click(m3u8[0], m3u8[1], 2, 1)
    time.sleep(1 + rand / 3)
    m.move(copy[0], copy[1])
    m.click(copy[0], copy[1], 1, 1)
    time.sleep(rand)
    m.move(copy_response[0], copy_response[1])
    m.click(copy_response[0], copy_response[1], 1, 1)
    time.sleep(rand + 0.5)

    m.click(finder[0], finder[1])
    time.sleep(rand)
    m.click(new_file[0], new_file[1])
    time.sleep(rand)
    m.click(new_m3u8[0], new_m3u8[1])
    time.sleep(1 + rand)
    m.move(save[0], save[1])
    m.click(save[0], save[1], 1, 1)
    time.sleep(2 + rand)
    k.press_key('command')
    k.tap_key('v')
    k.release_key('command')
    time.sleep( 1 + rand)
    k.press_key('command')
    k.tap_key('s')
    k.release_key('command')
    m.click(close_file[0], close_file[1])
    time.sleep(rand*2)
    m.click(chrome[0], chrome[1], 1)
    time.sleep(rand)
    m.move(191, 650)
    m.press(191, 650)
    time.sleep(1)
    m.drag(600, 650)
    time.sleep(1 + rand)
    m.release(600, 650)
    time.sleep(12)
    m.click(refresh[0], refresh[1])
    time.sleep(11 + rand * 2)
    m.click(play[0], play[1])
    time.sleep(5 + rand)
# k.type_string('Hello, World!')