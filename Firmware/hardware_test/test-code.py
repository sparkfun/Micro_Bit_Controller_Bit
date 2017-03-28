# Add your Python code here. E.g.
from microbit import *

junkup = Image ("99999:77777:55555:33333:11111")
junkdn = Image ("11111:33333:55555:77777:99999")
junkl  = Image ("97531:97531:97531:97531:97531")
junkr  = Image ("13579:13579:13579:13579:13579")
junka  = Image ("97531:75310:53100:31000:10000")
junkb  = Image ("13579:01357:00135:00031:00001")
junk12  = Image ("10000:31000:53100:75310:97531")
junk16  = Image ("00001:00013:00135:01357:13579")

pin12.read_digital()

#pin8.set_pull(pin8.PULL_DOWN)
#pin12.set_pull(pin12.PULL_UP)
#pin16.set_pull(pin16.PULL_UP)
#pin8.set_pull(PULL_UP)
#pin12.set_pull(PULL_UP)
#pin16.set_pull(PULL_UP)

while True:
    if pin0.read_digital():
        display.show(junkup)
    elif pin1.read_digital():
        display.show(junkl)
    elif pin2.read_digital():
        display.show(junkr)
    elif pin8.read_digital():
        display.show(junkdn)
    elif button_a.is_pressed():
        display.show(junka)
    elif button_b.is_pressed():
        display.show(junkb)
    elif pin12.read_digital():
        display.show(junk12)
    elif pin16.read_digital():
        display.show(junk16)
    else:
        display.clear()

    sleep(10)
