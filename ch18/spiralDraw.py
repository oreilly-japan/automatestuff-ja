import pyautogui, time
time.sleep(5)  # ❶
pyautogui.click() # お絵かきアプリをクリックしてフォーカスする ❷
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)  # 右へ移動 ❸
    distance = distance - 5  # ❹
    pyautogui.dragRel(0, distance, duration=0.2)  # 下へ移動 ❺
    pyautogui.dragRel(-distance, 0, duration=0.2) # 左へ移動 ❻
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2) # 上へ移動

