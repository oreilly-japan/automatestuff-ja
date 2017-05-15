#! python3
# -*- coding: utf-8 -*-
# 三目並べ
#   相川愛三が改良

import random, re

board10 = [None, '1', '2', '3', '4', '5', '6', '7', '8', '9']

def draw_board(board):
    # ボードを表示する
    # "board"は10個の文字列のリスト。インデックス0は無視。
   for i in range(7, 0, -3):
        print('   |   |')
        print(' ' + ' | '.join(board[i:i+3]))
        print('   |   |')
        if i > 1:
            print('-----------')

def input_player_letter():
    # プレイヤーに OかXかを選んでもらう。
    # プレーヤーの駒が先、コンピューターの駒が後のリストを返す。
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('O=先手、X=後手、どちらにしますか？ (O or X)')
        letter = input().upper()

    # [プレーヤーの駒, コンピューターの駒]というリストを返す
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def play_again():
    # プレーヤーがもう一度遊ぶと答えたならTrue、そうでなければFalseを返す。
    print('もう一度遊ぶ？ (yes or no)')
    return input().lower().startswith('y')

def make_move(board, letter, move):
    board[move] = letter

def is_winner(bo, le):
    # プレーヤーがか勝ちならTrueを返す。
    # boはボード、leはプレーヤーの駒
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # 上の行
    (bo[4] == le and bo[5] == le and bo[6] == le) or # 中の行
    (bo[1] == le and bo[2] == le and bo[3] == le) or # 下の行
    (bo[7] == le and bo[4] == le and bo[1] == le) or # 左の列
    (bo[8] == le and bo[5] == le and bo[2] == le) or # 中の列
    (bo[9] == le and bo[6] == le and bo[3] == le) or # 右の列
    (bo[7] == le and bo[5] == le and bo[3] == le) or # 対角線
    (bo[9] == le and bo[5] == le and bo[1] == le)) # 対角線

def get_board_copy(board):
    # ボードのコピーを作る
    return board[:]

def is_space_free(board, move):
    # ボードが空いていればTrue
    return board[move] == ' '

def get_player_move(board):
    # プレーヤーに次の手を入力してもらう
    while True:
        print('1=左下～9=右上のどこに打つ？(1-9)')
        move = input()
        if move in board10:
            imove = int(move)
            if is_space_free(board, imove):
                return imove
            else:
                print('そのマスは空いてません。')
        else:
            print('マスの番号')
            draw_board(board10)

def choose_random_move_from_list(board, moves_list):
    # 渡されたリストから有効な次の手をランダムに選んで返す。
    # 打つ場所がなければNoneを返す
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None

def get_computer_move(board, computer_letter):
    # コンピューターの次の手を選ぶ。
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # 三目並べの人工知能のアルゴリズム
    # まず、次の手で勝てるかどうかを調べる。
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, computer_letter, i)
            if is_winner(copy, computer_letter):
                return i

    # プレーヤーが次の手で勝てるなら、それを防ぐ。
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, player_letter, i)
            if is_winner(copy, player_letter):
                return i

    # 角が空いていれば、そこに打つ。
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move

    # 真ん中が空いていれば、そこに打つ。
    if is_space_free(board, 5):
        return 5

    # 上下左右に打つ。
    return choose_random_move_from_list(board, [2, 4, 6, 8])

def is_board_full(board):
    # ボードが埋まったらTrueを返す。
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


print('三目並べにようこそ！')

while True:
    # ボードをリセットする。
    the_board = [' '] * 10

    player_letter, computer_letter = input_player_letter()
    if player_letter == 'O':
        turn = 'プレーヤー'
    else:
        turn = 'コンピューター'
    print(turn + 'が先手。')

    while True:
       if is_board_full(the_board):
           draw_board(the_board)
           print('引き分け！')
           break

       if is_winner(the_board, player_letter):
           draw_board(the_board)
           print('おめでとう！　あなたの勝ち！')
           break

       if is_winner(the_board, computer_letter):
           draw_board(the_board)
           print('コンピューターの勝ち！')
           break

       if turn == 'プレーヤー':
           # プレーヤーの番
           draw_board(the_board)
           move = get_player_move(the_board)
           make_move(the_board, player_letter, move)
           turn = 'コンピューター'

       else:
           # コンピューターの番
           move = get_computer_move(the_board, computer_letter)
           make_move(the_board, computer_letter, move)
           turn = 'プレーヤー'

    if not play_again():
        break
