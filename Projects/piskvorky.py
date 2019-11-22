#Pavel Drexler
#Tic-Tac-Toe project
#Python 3.8.0
#version 0.1

#Define field

field = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
separator = 30*"="

def piskvorky():
	gameContinue = 1
	playerWin = 0
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


	

	def getInput():		
		print(player+ "'s turn.")
		position =input ("Select position from 1-9: ")

		
		#validity check
		valid = False
		while not valid:
			#  input validity check
			#Cheat
			#if position == "666":
			#	winner = "Pavel!"
			#	print (10*"*","Who dares wins.",10*"*")
			#	return winner

			while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
				position = input("Choose a position from 1-9: ")
 
			# Index correction
			position = int(position) - 1

			# Is spot available?
			if field[int(position)] == "-":
				valid = True
			else:
				print("You can't go there. Go again.")
		return position




		

	#check if there is a winner:
	def checkWinner(fieldInput):
		#row
		row_1 = fieldInput[0] == fieldInput[1] == fieldInput[2] != "-"
		row_2 = fieldInput[3] == fieldInput[4] == fieldInput[5] != "-"
		row_3 = fieldInput[6] == fieldInput[7] == fieldInput[8] != "-"
		gameContinue = 1
			
		if row_1: 
			winner = fieldInput[0]
			gameContinue = 0
		elif row_2: 
			winner = fieldInput[3]
			gameContinue = 0
		elif row_3: 
			winner = fieldInput[6]
			gameContinue = 0		
		#column
		col_1 = fieldInput[0] == fieldInput[3] == fieldInput[6] != "-"
		col_2 = fieldInput[1] == fieldInput[4] == fieldInput[7] != "-"
		col_3 = fieldInput[2] == fieldInput[5] == fieldInput[8] != "-"

		if col_1: 
			winner = fieldInput[0]
			gameContinue = 0
		elif col_2: 
			winner = fieldInput[1]
			gameContinue = 0
		elif col_3: 
			winner = fieldInput[2]
			gameContinue = 0

		#diagonal
		diag_1 = fieldInput[0] == fieldInput[4] == fieldInput[8] != "-"
		diag_2 = fieldInput[2] == fieldInput[4] == fieldInput[6] != "-"
		if diag_1: 
			winner = fieldInput[0]
			gameContinue = 0
		elif diag_2: 
			winner = fieldInput[2]
			gameContinue = 0

		#Deuce
		if "-" not in fieldInput:
			winner = "Developer - you guys sux!"
			gameContinue = 0
		elif gameContinue != 0:
			winner = 0

		return winner



	
	#Flip player
	def flipPlayer(playerInput):
		if playerInput == "X":
			playerInput = "O"
  
		elif playerInput == "O":
			playerInput = "X"
		return playerInput


	#Function of the game
	while gameContinue:
		#repeat game
		displayField()
		
		field[int(getInput())] = player
		print (separator)
		playerWin = checkWinner(field)
		if playerWin != 0 :
			print("Final state:")
			displayField()
			print (separator)
			return playerWin
		player = flipPlayer(player)


		

victor = piskvorky()
print("Victory goes to ", victor)