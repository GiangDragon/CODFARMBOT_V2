import pyautogui as pag
import pyscreeze
import time
from config import *
from utils import *

time.sleep(3)
enter_game()
a = 1
while (a <= NUM_ACCOUNT) :
    change_account(a)
    c = 1
    while (c <= 5) :
        if(Acc[1][c - 1] != "null") :
            clear_popup()
            farm(Acc[a][c - 1])
        if(c < 5) :
            change_character(c + 1)
        else :
            change_character(1)
        c+=1
    a+=1
change_account(1)
time.sleep(2)
pag.hotkey('alt', 'f4')
time.sleep(3)
pag.click(992, 504)
pag.hotkey('alt', 'f4')
