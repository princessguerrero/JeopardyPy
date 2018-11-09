import question
from question import startGame

class Player:
	def __init__(self, playerName):
		self.playerName = playerName
	
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

insertAns = input("[O]ne Player or [T]wo player: ")
if insertAns == 'O' or insertAns == 'o':
	print("You have choosen to play alone")
	playerNombre = input("Insert your name: ")
	player1 = Player(playerNombre)
	#player1.playerName = insert("What is your name? ")
	print("Hello {}. Ready to play? ".format(player1.playerName))	

	startGame()

elif insertAns =="T" or insertAns == 't':
	print("Two players!")