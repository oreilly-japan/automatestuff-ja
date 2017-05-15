the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

the_board2 = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
              'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
              'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}

def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

print_board(the_board)
print_board(the_board2)
