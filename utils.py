import pyautogui as pag
import pyscreeze
import time
from config import *

#hàm farm 5 mỏ
def farm(rss : str) :
    time.sleep(5)
    #ra đồng
    pag.press('space')
    #farm 5 mỏ
    for i in range(5):
        time.sleep(FARM_DELAY)
        #mở tab tìm kiếm
        pag.press("f")
        time.sleep(FARM_DELAY)
        #chọn loại rss
        if(i == 0) :
            pag.click(farm_location[rss])
            time.sleep(FARM_DELAY)
        #tìm mỏ
        pag.click(farm_location[f"{rss}_search"])
        time.sleep(FARM_DELAY + 2)
        #nhấn thu thập
        pag.click(farm_location["gather"])
        time.sleep(FARM_DELAY)
        #tạo đội quân
        pag.click(farm_location["create_legion"])
        time.sleep(FARM_DELAY)
        #xóa tướng phụ
        pag.click(farm_location["delete_deputy"])
        time.sleep(0.5)
        #chọn số lượng lính farm
        pag.click(farm_location["legion_size"])
        time.sleep(0.5)
        pag.typewrite(LEGION_SIZE, interval=0.05)
        time.sleep(0.1)
        pag.click(farm_location["confirm_size"])
        time.sleep(1)
        #hành quân
        pag.click(farm_location["march"])

#chọn tài khoản
def choose_account(name : str) :
    try:
        cur_acc = pag.locateOnScreen(f"media/{name}.png", confidence=0.95)
    except pag.ImageNotFoundException:
        cur_acc = None

    if (cur_acc == None) :
        pag.click(setting_location["switch_account"])
        time.sleep(ACT_DELAY + 4)
        pag.click(setting_location["expand_accounts"])
        time.sleep(2)
        while True :
            try:
                acc_pos = pag.locateOnScreen(f"media/{name}.png", confidence=0.95)
            except pag.ImageNotFoundException:
                acc_pos = None
            if(acc_pos != None) :
                pag.click(acc_pos)
                break
            else :
                pag.click(x=1209, y=579)
                pag.scroll(-10)
                time.sleep(5)
    else :
        pag.click(1230, 234)
        time.sleep(2)
        pag.click(1230, 234)
        time.sleep(1)
        pag.press('esc')
        time.sleep(1)
        pag.press('esc')



#chuyển tài khoản
def change_account(a : int) :
    #vào profile
    time.sleep(5)
    pag.click(setting_location["profile"])
    #vào setting (nhấn 2 lần cho chắc)
    time.sleep(ACT_DELAY)
    pag.click(setting_location["settings"])
    time.sleep(0.1)
    pag.click(setting_location["settings"])
    time.sleep(ACT_DELAY)
    #vào cài đặt tài khoản
    pag.click(setting_location["acc/char"])
    time.sleep(ACT_DELAY)
    #vào tài khoản
    pag.click(setting_location["accounts"])
    time.sleep(ACT_DELAY + 4)
    #chọn tài khoản
    choose_account(Acc_name[a])
    time.sleep(3)
    #vào game
    pag.click(setting_location["start_acc"])
    time.sleep(SWITCH_ACCOUNT_DELAY)
    #click vào giữa màn hình để chọn cửa sổ game và bật full màn hình   
    pag.click(992, 504)
    time.sleep(1) 
    pag.hotkey('win', 'up')

# chuyển nhân vật
def change_character(c : int) :
    time.sleep(5)
    pag.click(setting_location["profile"])
    time.sleep(ACT_DELAY)
    pag.click(setting_location["settings"])
    time.sleep(0.1)
    pag.click(setting_location["settings"])
    time.sleep(ACT_DELAY)
    pag.click(setting_location["acc/char"])
    time.sleep(ACT_DELAY)
    pag.click(setting_location[f"char{c}"])
    time.sleep(ACT_DELAY)
    pag.click(setting_location["confirm_switch_char"])
    time.sleep(SWITCH_CHAR_DELAY)   
    pag.click(992, 504)
    time.sleep(1) 
    pag.hotkey('win', 'up')

#vào game
def enter_game() :
    #nhấn start
    time.sleep(3)
    pag.click(1699, 951)
    #vào game
    time.sleep(40)
    pag.click(992, 504)
    time.sleep(1)
    pag.hotkey('win', 'up')
    time.sleep(5)

#clear linh tinh
def clear_popup() :
    #clear gói nạp xàm nho
    time.sleep(3)
    pag.click(x=1354, y=299)
    #clear thư lãnh đạo
    time.sleep(2)
    pag.click(x=1226, y=281)
    
    