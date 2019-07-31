import pyautogui as auto
import time
""" 1919,1079 """
#auto.click()
#auto.click((auto.locateCenterOnScreen('path relativo de la imagen con bordes')))
#auto.press('tecla')
#screenWidth, screenHeight = auto.size()
#currentMouseX, currentMouseY = auto.position()
#auto.PAUSE = 2.5
#auto.moveTo(100, 150)
#auto.click()
#auto.moveRel(None, 10)  # move mouse 10 pixels down
#auto.doubleClick()
#auto.moveTo(500, 500, duration=2, tween=auto.easeInOutQuad)
#auto.typewrite('Hello world!', interval=0.25) 
#auto.press('esc')
#auto.keyDown('shift')
#auto.press(['left', 'left', 'left', 'left', 'left', 'left'])
#auto.keyUp('shift')
#auto.hotkey('ctrl', 'c')
screenWidth, screenHeight = auto.size()

currentMouseX, currentMouseY = auto.position()

auto.moveTo(524,1050)
auto.click()
time.sleep(5)
auto.click((auto.locateCenterOnScreen('terminal.png')))
auto.typewrite('source /c/Script/.comandos.sh')
auto.press('enter')


"""
If you lose control and need to stop the current PyAutoGUI function, keep moving the mouse cursor up and to the left. To disable this feature, set FAILSAFE to False
"""

