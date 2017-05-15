import threading, time
print('プログラム開始')

def take_a_nap():  # ❶
    time.sleep(5)
    print('起きた！')

thread_obj = threading.Thread(target=take_a_nap)  # ❷
thread_obj.start()  # ❸

print('プログラム終了')
