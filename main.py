import question
from question import startGame

class Player:
	def __init__(self, playerName, playerScore):
		self.playerName = playerName
		self.playerScore = 0
	
	#def insertPlayer():



print(" __    __     _                            _        ")
print("/ / /\ \ \___| | ___ ___  _ __ ___   ___  | |_ ___ ") 
print("\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \ ") 
print(" \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |")
print("  \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/ ")
print("")                                                    
print("          __                                 _          ")
print("          \ \  ___  ___  _ __   __ _ _ __ __| |_   _    ")
print("           \ \/ _ \/ _ \| '_ \ / _` | '__/ _` | | | |   ")
print("        /\_/ /  __/ (_) | |_) | (_| | | | (_| | |_| |")  
print("        \___/ \___|\___/| .__/ \__,_|_|  \__,_|\__, |   ")
print("                        |_|                    |___/ ")

insertAns = input("[O]ne Player or [T]wo player:\n ")
if insertAns == 'O' or insertAns == 'o':
	print("You have choosen to play alone")
	playerNombre = input("Insert your name: ")
	player1 = Player(playerNombre, 0)
	#player1.playerName = insert("What is your name? ")
	print("\nHello {}. Ready to play?\n ".format(player1.playerName))	
	print("You have a score of {} points\n".format(player1.playerScore))
	startGame(player1.playerScore)

elif insertAns =="T" or insertAns == 't':
	print("Two players coming soon!")