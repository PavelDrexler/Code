#Pavel Drexler
#Tic-Tac-To project
#Python 3.8.0

#Define field

field = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
separator = 30*"="

def game():
	gameContinue = 1
	winner = 0
	player = "X"
	print (separator)
	print("Welcome to Tic-Tac-Toe, best game of the year!")
	print("First player will use X and second one O.\nLet the better one emerge victor!")
	print (separator)

	def displayField():
		print("\n")	
		print(field[0] + " | " + field[1] + " | " + field[2] + "     1 | 2 | 3")
		print(field[3] + " | " + field[4] + " | " + field[5] + "     4 | 5 | 6")	
		print(field[6] + " | " + field[7] + " | " + field[8] + "     7 | 8 | 9")
		print("\n")


	while gameContinue:
		#repeat game
		displayField()

		print(player+ "'s turn.")
		position =input ("Select position from 1-9: ")

		
		#validity check
		valid = False
		while not valid:
			#  input validity check
			if position == "666":
				winner = "Drex you bitch!"
				print (10*"*","Who dares wins.",10*"*")
				return winner

			while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
				position = input("Choose a position from 1-9: ")
 
			# Index correction
			position = int(position) - 1

			# Is spot available?
			if field[int(position)] == "-":
				valid = True
			else:
				print("You can't go there. Go again.")
		


		field[int(position)] = player
		print (separator)

		#check if winner:

		#row
		row_1 = field[0] == field[1] == field[2] != "-"
		row_2 = field[3] == field[4] == field[5] != "-"
		row_3 = field[6] == field[7] == field[8] != "-"
			
		if row_1: 
			winner = field[0]
			gameContinue = 0
		elif row_2: 
			winner = field[3]
			gameContinue = 0
		elif row_3: 
			winner = field[6]
			gameContinue = 0		
		#column
		col_1 = field[0] == field[3] == field[6] != "-"
		col_2 = field[1] == field[4] == field[7] != "-"
		col_3 = field[2] == field[5] == field[8] != "-"

		if col_1: 
			winner = field[0]
			gameContinue = 0
		elif col_2: 
			winner = field[1]
			gameContinue = 0
		elif col_3: 
			winner = field[2]
			gameContinue = 0

		#diagonal
		diag_1 = field[0] == field[4] == field[8] != "-"
		diag_2 = field[2] == field[4] == field[6] != "-"
		if diag_1: 
			winner = field[0]
			gameContinue = 0
		elif diag_2: 
			winner = field[2]
			gameContinue = 0

		#Deuce
		elif "-" not in field:
			winner = "Developer - you guys sux!"
			gameContinue = 0



		#Flip player
		if player == "X":
			player = "O"
  
		elif player == "O":
			player = "X"


		


		
	print("Final state:")
	displayField()
	print (separator)
	return winner

victor = game()
print("Victory goes to ", victor)