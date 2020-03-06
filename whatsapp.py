import webbrowser
import time
import pyautogui as gui

interval = 3

position = 1023,230

numbers ={919644507294}

msg="hello jayesh"

for i in numbers:
    url= 'https://wa.me/{}?text={}'.format(i,msg)
    webbrowser.open(url)
    time.sleep(4)
    gui.click(position)
    time.sleep(5)
    gui.press('enter')
    time.sleep(interval)