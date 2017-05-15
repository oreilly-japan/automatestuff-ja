import time
def calc_prod():  # ❶
    # 1～99,999の積を求める
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

start_time = time.time()  # ❷
prod = calc_prod()
end_time = time.time()  # ❸
print('計算結果は{}桁です。'.format(len(str(prod))))  # ❹
print('計算時間は{}秒でした。'.format(end_time - start_time))  # ❺
