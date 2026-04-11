import pyautogui as pag
import pyscreeze
import time

#config
#_____________________________________________________________________
LEGION_SIZE = "10000"
NUM_ACCOUNT = 3
FARM_DELAY = 2.5
ACT_DELAY = 5
SWITCH_CHAR_DELAY = 20
SWITCH_ACCOUNT_DELAY = 20
#danh sách tên tài khoản, phần trước @gmail.com của email
Acc_name = {
    1 : "truonggiang.tlccv",
    2 : "kanghyeongnim3",
    3 : "truonggiang.tlc69",
    4 : "haidiepa7"
}
#danh sách nhu cầu farm, vàng = "gold", gỗ = "wood", quặng = "ore", nước = "mana"
#Nếu muốn acc không farm thì để "null"
Acc = {
    1 : ("gold", "wood", "ore", "wood", "gold"),
    2 : ("mana", "mana", "gold", "wood", "gold"),
    3 : ("mana", "ore", "wood", "gold", "mana"),
}

farm_location = {
    "gather" : (1216, 673),
    "create_legion" : (1670, 328),
    "march" : (1357, 818),
    "gold" : (763, 937),
    "wood" : (956, 940),
    "ore" : (1157, 946),
    "mana" : (1350, 947),
    "gold_search" : (756, 822),
    "wood_search" : (957, 828),
    "ore_search" : (1156, 823),
    "mana_search" : (1357, 820),
    "delete_deputy" : (952, 398),
    "legion_size" : (1421, 497),
    "confirm_size": (1437, 785)
}

setting_location = {
    "fullscreen" : (1815, 49),
    "profile" : (46, 67),
    "settings" : (373, 970),
    "acc/char" : (275, 597),
    "char1" : (768, 612),
    "char2" : (1426, 511),
    "char3" : (790, 507),
    "char4" : (1445, 408),
    "char5" : (804, 405),
    "confirm_switch_char" : (1084, 630),
    "accounts" : (784, 249),
    "switch_account" : (955, 748),
    "expand_accounts" : (1167, 483),
    "start_acc" : (962, 620)
}