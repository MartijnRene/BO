from microbit import *
import random

countdown = [3, 2, 1]

for number in countdown:
    display.show(number)
    sleep(300)
    display.clear()
    sleep(500)

level = 1
highscore = 0

while True:

    order = []
    
    for i in range(level):
        order.append(random.randint(0,1))
        
    for o in order:
        if o is 0:
            display.show(Image.ARROW_W)
        else:
            display.show(Image.ARROW_E)

        sleep(300)
        display.clear()
        sleep(100)

    i = 0
    wrong = False

    while i < len(order):
        if button_a.is_pressed():
            if order[i] is 0:
                i += 1
            else:
                wrong = True
            while button_a.is_pressed():
                1
        if button_b.is_pressed():
            if order[i] is 1:
                i += 1
            else:
                wrong = True
            while button_b.is_pressed():
                1
        if wrong:
            for i in range(10):
                display.show(Image.NO)
                sleep(50)
                display.clear()
                sleep(50)
            display.scroll("Score: " + str(level-1))
            display.scroll("Highscore: " + str(highscore))
            reset()

    display.show(Image.YES)
    sleep(800)
    level += 1