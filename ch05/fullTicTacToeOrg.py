#! python3
# -*- coding: utf-8 -*-
# 三目並べ

import random

def drawBoard(board):
    # ボードを表示する

    # "board"は10個の文字列のリスト。インデックス0は無視。
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    # プレイヤーに OかXかを選んでもらう。
    # プレーヤーの駒が先、コンピューターの駒が後のリストを返す。
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('どちらの駒にしますか？ (O or X)')
        letter = input().upper()

    # [プレーヤーの駒, コンピューターの駒]というリストを返す
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # 先手をランダムに選ぶ
    if random.randint(0, 1) == 0:
        return 'コンピューター'
    else:
        return 'プレーヤー'

def playAgain():
    # プレーヤーがもう一度遊ぶと答えたならTrue、そうでなければFalseを返す。
    print('もう一度遊ぶ？ (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
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

def getBoardCopy(board):
    # ボードのコピーを作る
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    # ボードが空いていればTrue
    return board[move] == ' '

def getPlayerMove(board):
    # プレーヤーに次の手を入力してもらう
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('どこに打つ？ (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # 渡されたリストから有効な次の手をランダムに選んで返す。
    # 打つ場所がなければNoneを返す
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # コンピューターの次の手を選ぶ。
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # 三目並べの人工知能のアルゴリズム
    # まず、次の手で勝てるかどうかを調べる。
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # プレーヤーが次の手で勝てるなら、それを防ぐ。
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # 角が空いていれば、そこに打つ。
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # 真ん中が空いていれば、そこに打つ。
    if isSpaceFree(board, 5):
        return 5

    # 上下左右に打つ。
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # ボードが埋まったらTrueを返す。
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('三目並べにようこそ！')

while True:
    # ボードをリセットする。
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(turn + 'が先手。')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'プレーヤー':
            # プレーヤーの番
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('おめでとう！　あなたの勝ち！')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('引き分け！')
                    break
                else:
                    turn = 'コンピューター'

        else:
            # コンピューターの番
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('コンピューターの勝ち！')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('引き分け！')
                    break
                else:
                    turn = 'プレーヤー'

    if not playAgain():
        break
