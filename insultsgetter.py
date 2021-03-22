
import pyautogui as pag

while True:

     pag.leftClick(-2837,718)
     pag.moveTo(-3199,661,duration=0.3)
     pag.dragTo(-2455,664,duration=0.3)  

     pag.hotkey('ctrl', 'c')

     pag.leftClick(2216,1575)

     pag.hotkey('ctrl', 'v')

     pag.typewrite(['enter'],interval=0.1)
