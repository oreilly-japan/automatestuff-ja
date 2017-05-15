import random  # ❶
 
def get_answer(answer_number):  # ❷
    if answer_number == 1:  # ❸
        return '確かにそうだ'
    elif answer_number == 2:
        return '間違いなくそうだ'
    elif answer_number == 3:
        return 'はい'
    elif answer_number == 4:
        return 'なんとも。もういちどやってみて'
    elif answer_number == 5:
        return 'あとでもう一度きいてみて'
    elif answer_number == 6:
        return '集中してもう一度きいてみて'
    elif answer_number == 7:
        return '私の答えはノーです'
    elif answer_number == 8:
        return '見通しはそれほどよくない'
    elif answer_number == 9:
        return 'とても疑わしい'

r = random.randint(1, 9) # ❹
fortune = get_answer(r)  # ❺
print(fortune)  # ❻
