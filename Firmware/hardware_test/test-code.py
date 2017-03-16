# Add your Python code here. E.g.
from microbit import *

junkup = Image ("99999:77777:55555:33333:99999")
junkl  = Image ("97531:97531:97531:97531:97531")
junkr  = Image ("13579:13579:13579:13579:13579")

while True:
#    if button_a.is_pressed() and button_b.is_pressed():
    if pin0.is_touched():
        display.show(junkup)
#    elif button_a.is_pressed():
    elif pin1.is_touched():
        display.show(junkl)
#    elif button_b.is_pressed():
    elif pin2.is_touched():
        display.show(junkr)
    else:
        display.clear()

    sleep(10)
