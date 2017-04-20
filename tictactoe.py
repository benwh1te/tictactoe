#TIC-TAC-TOE GAME

import os;
import random;

#returns int value of the current board
def movesLeft(board):
	for i in range(3):
		for j in range(3):
			if(board[i][j] == ' '):
				return True;
	return False;

def eval(board):
	for row in range(3):
		if (board[row][0] == board[row][1]) & (board[row][1] == board[row][2]):
			if(board[row][0] == comp):
				return 10; 
			if(board[row][0] == player):
				return -10;
				
	for col in range(3):
		if (board[0][col] == board[1][col]) & (board[1][col] == board[2][col]):
			if(board[0][col] == comp):
				return 10;
			if(board[0][col] == player):
				return -10;	

	if (board[0][0] == board[1][1]) & (board[1][1] == board[2][2]):
		if(board[0][0] == comp):
				return 10;
		if(board[0][0] == player):
				return -10;	

	if (board[0][2] == board[1][1]) & (board[1][1] == board[2][0]):
		if(board[0][2] == comp):
				return 10;
		if(board[0][2] == player):
				return -10;	

	return 0;

def minimax(board, depth, isHuman):
	score = eval(board);
	#print(depth);

	if(score == -10):
		return score-depth;
	if(score == 10):
		return score-depth;
	if(movesLeft(board) is False):
		return 0-depth;
	#print('here');

	if(isHuman):
		besth = 1000;
		for i in range(3):
			for j in range(3):
				if board[i][j] == ' ':
					board[i][j] = player;
					besth = min(besth, minimax(board, depth+1, False));
					board[i][j] = ' ';
		return besth;
	else:
		bestpc = -1000;
		for i in range(3):
			for j in range(3):
				if board[i][j] == ' ':
					board[i][j] = comp;
					bestpc = max(bestpc, minimax(board, depth+1, True));
					board[i][j] = ' ';
		return bestpc;


def findBestMove(board):
	bestVal = -1000;
	#moveVal = -1000;
	# row, col
	bestMove = [-1, -1];
	for i in range(3):
		for j in range(3):
			if board[i][j] == ' ':
				board[i][j] = comp;
				moveVal = minimax(board, 1, True);
				board[i][j] = ' ';
				if(moveVal > bestVal):
					bestVal = moveVal;
					bestMove = [i, j];
	#print(moveVal);
	return bestMove;

'''
comp = "x";
player = "o";
#b = [[' ' for x in range(3)] for y in range(3)];
b = [[comp, comp, player], [' ', player, ' '], [' ', ' ', ' ']];
count = 0;
bestMove = findBestMove(b);

print(bestMove[0]);
print(bestMove[1]);
print(b[0]);
print(b[1]);
print(b[2]);
'''

def checkForWin(board):
	#see if can win in one move
	for i in range(3):
		for j in range(3):
			if board[i][j] == ' ':
				board[i][j] = comp;
				if(eval(board) == -10):
					board[i][j] = ' ';
					bestMove = [i, j];
					return bestMove;
				board[i][j] = ' ';
	return 1;

switch = {'1':[0,0], '2':[0,1], '3':[0,2], '4':[1,0], '5':[1,1], '6':[1, 2], '7':[2,0], '8':[2,1], '9':[2,2]};
player = 'x';
comp = 'o';

def printInstructions():
	print("Instructions for the game are as follows:")
	print(['1', '2', '3']);
	print(['4', '5', '6']);
	print(['7', '8', '9']);
	print("\nWhen it is your turn, you will enter the number of the space that you want.");
	print("\nThe goal is to get 3 in a row before the computer.\n")

def main():
	print("Welcome to Tic-Tac-Toe\n\n");
	print("The player with the first move will be decided at random.\n");
	printInstructions();
	os.system("pause");
	first = random.random();
	compsTurn = True;
	if(first >= 0.5):
		print("\nThe computer will make the first move.\n\n");
		compsTurn = True;
	else:
		print("\nYou will make the first move.\n");
		compsTurn = False;

	print("Are you ready?\n");
	os.system("pause");

	b = [[' ' for x in range(3)] for y in range(3)];

	while (eval(b) == 0) & (movesLeft(b)):
		if(compsTurn):
			k = checkForWin(b);
			if(k == 1):
				compMove = findBestMove(b);
				b[compMove[0]][compMove[1]] = comp;
				compsTurn = False;
			else:
				b[k[0]][k[1]] = comp;
				compsTurn = False;
		else:
			move = input("What is your move? Value must be between 1 and 9.\n");
			rowCol = switch[move];
			if(b[rowCol[0]][rowCol[1]] == ' '):
				b[rowCol[0]][rowCol[1]] = player;
				compsTurn = True;
			else:
				print("That move is invalid, someone has already moved there.\n");	

		print(b[0]);
		print(b[1]);
		print(b[2]);
		print('\n');
		#print(eval(b));	

	if(eval(b) == -10):
		print("YOU WON!!");
	elif(eval(b) == 10):
		print("You lost :(");
	else:
		print("The game ended in a tie.");

main();