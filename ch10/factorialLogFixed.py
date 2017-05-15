import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('プログラム開始')

def factorial(n):
    logging.debug('factorial({})開始'.format(n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i = {}, total = {}'.format(i, total))
    logging.debug('factorial({})終了'.format(n))
    return total

print(factorial(5))
logging.debug('プログラム終了')
