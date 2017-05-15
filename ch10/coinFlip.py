import random
heads = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:  # ❶
        heads = heads + 1
    if i == 500:
        print('半分完了！')  # ❷
print('表は' + str(heads) + '回出ました。')
