#! python3
# mouseNow.py - マウスカーソル座標を表示する

import pyautogui
print('中断するにはCtrl-Cを押してください。')

try:
    while True:
        # マウス座標を取得して表示する
        x, y = pyautogui.position()
        position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pixel_color = pyautogui.screenshot().getpixel((x, y))
        position_str += ' RGB: (' + str(pixel_color[0]).rjust(3)
        position_str += ', ' + str(pixel_color[1]).rjust(3)
        position_str += ', ' + str(pixel_color[2]).rjust(3) + ')'
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)  # ❶

except KeyboardInterrupt: # ❶
    print('\n終了。')     # ❷
