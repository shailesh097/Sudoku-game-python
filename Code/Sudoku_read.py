from random import choice

if __name__ != '__main__':
	def random_board():
		board_list = [
		    [
		    [7, 8, 0, 4, 0, 0, 1, 2, 0],
		    [6, 0, 0, 0, 7, 5, 0, 0, 9],
		    [0, 0, 0, 6, 0, 1, 0, 7, 8],
		    [0, 0, 7, 0, 4, 0, 2, 6, 0],
		    [0, 0, 1, 0, 5, 0, 9, 3, 0],
		    [9, 0, 4, 0, 6, 0, 0, 0, 5],
		    [0, 7, 0, 3, 0, 0, 0, 1, 2],
		    [1, 2, 0, 0, 0, 7, 4, 0, 0],
		    [0, 4, 9, 2, 0, 6, 0, 0, 7]
		    ],
		    
		    [
		    [5, 3, 0, 0, 7, 0, 0, 0, 0],
		    [6, 0, 0, 1, 9, 5, 0, 0, 0],
		    [0, 9, 8, 0, 0, 0, 0, 6, 0],
		    [8, 0, 0, 0, 6, 0, 0, 0, 3],
		    [4, 0, 0, 8, 0, 3, 0, 0, 1],
		    [7, 0, 0, 0, 2, 0, 0, 0, 6],
		    [0, 6, 0, 0, 0, 0, 2, 8, 0],
		    [0, 0, 0, 4, 1, 9, 0, 0, 5],
		    [0, 0, 0, 0, 8, 0, 0, 7, 9]
		    ],

		    [
		    [0, 0, 0, 7, 9, 0, 0, 5, 0],
		    [3, 5, 2, 0, 0, 8, 0, 4, 0],
		    [0, 0, 0, 0, 0, 0, 0, 8, 0],
		    [0, 1, 0, 0, 7, 0, 0, 0, 4],
		    [6, 0, 0, 3, 0, 1, 0, 0, 8],
		    [9, 0, 0, 0, 8, 0, 0, 1, 0],
		    [0, 2, 0, 0, 0, 0, 0, 0, 0],
		    [0, 4, 0, 5, 0, 0, 8, 9, 1],
		    [0, 8, 0, 0, 3, 7, 0, 0, 0]
		    ],

		]

		board = choice(board_list)
		return board
else:
	print("This program is not desined to run on its own.")
