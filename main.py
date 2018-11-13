from prettytable import PrettyTable
from basic import *
from players import Player
import question
from question import startGame

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




while True:
        no_of_players = inputInt("\n\nEnter number of players[1-4]: ")
        while no_of_players < 1 or no_of_players > 4:
                print("Invalid player number. Please choose from 1-4")
                no_of_players = inputInt("Enter number of players[1-4]: ")
        
        players = []
        for x in range(no_of_players):
                name = inputString("Enter player {} name: ".format(x+1))
                player = Player(name, 0)
                players.append(player)

        players = startGame(players)
        print("="*20 + " SCORE BOARD " + "="*20)
        table = PrettyTable()
        table.field_names = ["Player Name", "Score"]
        for x in range(no_of_players):
                table.add_row([players[x].name, players[x].score])
        print(table)
        play_again = input("Press <ENTER> to play again or type any key to quit game: ")
        if play_again is not None and play_again.strip() != "":
                break
