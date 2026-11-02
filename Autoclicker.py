import pyautogui
import time
import keyboard




def click_keyboard():
    pyautogui.press('x')
    time.sleep(0.5)
    pyautogui.press('x')

def click():
    pyautogui.click()
    



def main():
    time.sleep(0.5)
    status = 0
    while True:
        click_keyboard()

        if keyboard.is_pressed('-'):
            break
main()



    
