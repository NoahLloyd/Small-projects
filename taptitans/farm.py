import pyautogui
from time import sleep

p = pyautogui

def tap():
    p.moveTo(836, 423)
    p.click()
    p.keyDown('shift')
    sleep(20)
    p.keyUp('shift')

def upgrade_tap():
    p.click(593, 1031)
    sleep(0.2)
    p.click(1050, 727)
    sleep(0.2)
    p.click(684, 1027)

def upgrade_all_heroes():
    1+1

def upgrade_hero():
    p.click
    sleep(0.01)
    for j in range(1,3):
        p.moveTo(823, 713)
        p.dragTo(829, 972, duration=0.2, tween=pyautogui.easeInOutQuad)
    p.click(1043, 738)
    sleep(0.01)
    p.click(1028, 827)
    sleep(0.01)
    p.click(1041, 921)
    sleep(0.01)
    p.click(1035, 994)

def prestige():
    p.click(586, 1032)
    sleep(0.2)
    p.click(1038, 865)
    sleep(0.2)
    p.click(837, 984)
    sleep(0.2)
    p.click(945, 823)
    sleep(8)
    if p.screenshot().getpixel((759, 998)) == (62, 165, 207):
        p.click(837, 984)
        sleep(0.2)
        p.click(945, 823)
        sleep(8)
        p.click(689, 1031)
    else:
        p.click(689, 1031)

def use_relics():
    p.click(983, 1032)
    sleep(0.2)
    p.click(1042, 866)
    sleep(0.2)
    p.click(692, 1033)

def buy_spells():
    p.click(592, 1028)
    sleep(0.2)
    p.click(1003, 576)
    sleep(0.2)
    for i in range(1,7):
        p.click(1042,420+((i-1)*95))
        sleep(0.1)
    p.click(1011, 12)
    sleep(0.2)
    p.click(690, 1034)


def check_events():
    im = p.screenshot()
    im.getpixel(())

def run():
    while True:
        #upgrade_all_heroes()
        track = 1
        while track % 50 != 0:
            tap()
            #upgrade_hero()

            if track % 50 == 3:
                upgrade_tap()
                sleep(3)
                buy_spells()
            if track % 10 == 0:
                p.click(1094, 577)
                sleep(0.2)
                p.press('e')
                p.press('2')

            track += 1
            print(track)
        prestige()
        use_relics()

def other():
  for i in range(1,100):
      tap()
      tap()
      p.click(767, 535)
      tap()
      p.click(767, 535)
      p.press('y')
      p.press('r')
      p.click(1059, 52)
      
run()
