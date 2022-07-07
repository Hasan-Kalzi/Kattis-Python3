# Emag Eht Htiw Em Pleh
# Solution by Hasan Kalzi 12-03-2021
# Link to problem in Kattis: https://open.kattis.com/problems/empleh
import re
import sys


def place_pieces(player, board):
    for i in range(1, len(player)):
        if player[0] == "White":
            if len(player[i]) == 3:
                board[player[i][1:3]] = player[i][0].upper()
            elif len(player[i]) == 2:
                board[player[i]] = 'P'
        else:
            if len(player[i]) == 3:
                board[player[i][1:3]] = player[i][0].lower()
            elif len(player[i]) == 2:
                board[player[i]] = 'p'
    return board


chess_board = {
    'a1': ':', 'a2': '.', 'a3': ':', 'a4': '.', 'a5': ':', 'a6': '.', 'a7': ':', 'a8': '.',
    'b1': '.', 'b2': ':', 'b3': '.', 'b4': ':', 'b5': '.', 'b6': ':', 'b7': '.', 'b8': ':',
    'c1': ':', 'c2': '.', 'c3': ':', 'c4': '.', 'c5': ':', 'c6': '.', 'c7': ':', 'c8': '.',
    'd1': '.', 'd2': ':', 'd3': '.', 'd4': ':', 'd5': '.', 'd6': ':', 'd7': '.', 'd8': ':',
    'e1': ':', 'e2': '.', 'e3': ':', 'e4': '.', 'e5': ':', 'e6': '.', 'e7': ':', 'e8': '.',
    'f1': '.', 'f2': ':', 'f3': '.', 'f4': ':', 'f5': '.', 'f6': ':', 'f7': '.', 'f8': ':',
    'g1': ':', 'g2': '.', 'g3': ':', 'g4': '.', 'g5': ':', 'g6': '.', 'g7': ':', 'g8': '.',
    'h1': '.', 'h2': ':', 'h3': '.', 'h4': ':', 'h5': '.', 'h6': ':', 'h7': '.', 'h8': ':',
}
edge = "+---+---+---+---+---+---+---+---+"
pieces = [[], [], [], [], [], [], [], []]
white_pitch = True

player1 = re.split(": |,|\n|\\s", sys.stdin.readline())
chess_board = place_pieces(player1, chess_board)
player2 = re.split(": |,|\n|\\s", sys.stdin.readline())
chess_board = place_pieces(player2, chess_board)

sys.stdout.write(
    "+---+---+---+---+---+---+---+---+\n" +
    "|." + chess_board['a8'] + ".|:" + chess_board['b8'] + ":|." + chess_board['c8'] + ".|:" + chess_board[
        'd8'] + ":|." + chess_board['e8'] + ".|:" + chess_board['f8'] + ":|." + chess_board['g8'] + ".|:" + chess_board[
        'h8'] + ":|\n" +
    "+---+---+---+---+---+---+---+---+\n" +
    "|:" + chess_board['a7'] + ":|." + chess_board['b7'] + ".|:" + chess_board['c7'] + ":|." + chess_board[
        'd7'] + ".|:" + chess_board['e7'] + ":|." + chess_board['f7'] + ".|:" + chess_board['g7'] + ":|." + chess_board[
        'h7'] + ".|\n" +
    "+---+---+---+---+---+---+---+---+\n" +
    "|." + chess_board['a6'] + ".|:" + chess_board['b6'] + ":|." + chess_board['c6'] + ".|:" + chess_board[
        'd6'] + ":|." + chess_board['e6'] + ".|:" + chess_board['f6'] + ":|." + chess_board['g6'] + ".|:" + chess_board[
        'h6'] + ":|\n" +
    "+---+---+---+---+---+---+---+---+\n" +
    "|:" + chess_board['a5'] + ":|." + chess_board['b5'] + ".|:" + chess_board['c5'] + ":|." + chess_board[
        'd5'] + ".|:" + chess_board['e5'] + ":|." + chess_board['f5'] + ".|:" + chess_board['g5'] + ":|." + chess_board[
        'h5'] + ".|\n" +
    "+---+---+---+---+---+---+---+---+\n" +
    "|." + chess_board['a4'] + ".|:" + chess_board['b4'] + ":|." + chess_board['c4'] + ".|:" + chess_board[
        'd4'] + ":|." + chess_board['e4'] + ".|:" + chess_board['f4'] + ":|." + chess_board['g4'] + ".|:" + chess_board[
        'h4'] + ":|\n" +
    "+---+---+---+---+---+---+---+---+\n" +
    "|:" + chess_board['a3'] + ":|." + chess_board['b3'] + ".|:" + chess_board['c3'] + ":|." + chess_board[
        'd3'] + ".|:" + chess_board['e3'] + ":|." + chess_board['f3'] + ".|:" + chess_board['g3'] + ":|." + chess_board[
        'h3'] + ".|\n" +
    "+---+---+---+---+---+---+---+---+\n" +
    "|." + chess_board['a2'] + ".|:" + chess_board['b2'] + ":|." + chess_board['c2'] + ".|:" + chess_board[
        'd2'] + ":|." + chess_board['e2'] + ".|:" + chess_board['f2'] + ":|." + chess_board['g2'] + ".|:" + chess_board[
        'h2'] + ":|\n" +
    "+---+---+---+---+---+---+---+---+\n" +
    "|:" + chess_board['a1'] + ":|." + chess_board['b1'] + ".|:" + chess_board['c1'] + ":|." + chess_board[
        'd1'] + ".|:" + chess_board['e1'] + ":|." + chess_board['f1'] + ".|:" + chess_board['g1'] + ":|." + chess_board[
        'h1'] + ".|\n" +
    "+---+---+---+---+---+---+---+---+"
)
