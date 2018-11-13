from basic import *
from prettytable import PrettyTable

class Question:
    def __init__(self, ques, ans, val, picked):
        self.ques = ques
        self.ans = ans
        self.val = val
        self.picked = False

# questions for GenOne
q1, q2 = Question("How many members were selected for the GenOne program?", "20", 100, False), Question("Which company worked with #YesWeCode for the GenOne initiative?", "Infor", 200, False)
q3, q4 = Question("Who is the founder of #YesWeCode?", "Van Jones", 300, False), Question("What is the DreamCorps logo?", "dragon", 400, False)

# questions for Linux
q5 = Question("What animal is the mascot for Linux?", "penguin", 100, False)
q6 = Question("What is the command that tells the process to die gracefully?", "kill", 200, False)
q7 = Question("What is the command that changes file permissions?", "chmod", 300, False)
q8 = Question("Who is the founder of Linux?", "Linus Torvalds", 400, False)

# questions for Python
q9 = Question("What is an immutable array in Python?", "list", 100, False)
q10 = Question("What keyword do you use to get a library?", "import", 200, False)
q11 = Question("What do you use to extract content from a website?", "web scraper", 300, False)
q12 = Question("What is the process of detecting and removing potential errors in your program?", "debug", 400, False)

# questions for Career Building
q13 = Question("What is the best social platform to connect to professionals?", "linkedin", 100, False)
q14 = Question("What is Infor's software that has educational training resources to learn more about their company?", "lms", 200, False)
q15 = Question("The process of developing contacts in one's career.", "networking", 300, False)
q16 = Question("What is the acronym for the research tool that was developed by Kenneth Thomas and Ralph Kilmann in the early 1970s?", "tki", 400, False)


my_hash = {
    "GenOne": {
        100: [q1],
        200: [q2],
        300: [q3],
        400: [q4]
    },
    "Linux": { 
        100: [q5],
        200: [q6],
        300: [q7],
        400: [q8]
    },
    "Python": {
        100: [q9],
        200: [q10],
        300: [q11],
        400: [q12]
    },
    "Career Building": {
        100: [q13],
        200: [q14],
        300: [q15],
        400: [q16]
    }
}

def show_options():
    table = PrettyTable()
    column_names = list(my_hash.keys())
    print(column_names)
    counter = 0
    for key,category in my_hash.items():
        col = []
        for ckey,value in category.items():
            if not value[0].picked:
                col.append(ckey)
            else:
                col.append("")
        table.add_column(column_names[counter], col)
        counter += 1
    print(table)

def choose_category():
    choice = inputString("Pick a category: ")
    while choice.lower() not in [x.lower() for x in list(my_hash.keys())] and choice.lower() != "quit":
        print("Please enter valid category name or type 'quit' if you're done playing")
        choice = inputString("Pick a category: ")
    return choice

def choose_level(chosen_category):
    remaining = []
    for key,value in chosen_category.items():
        if not value[0].picked:
            remaining.append(key)
    choice_val = inputInt("Pick a value: ")
    while choice_val not in remaining and choice_val != 1:
        print("Please enter valid value or type 1 if you want to escape.")
        choice_val = inputInt("Pick a value: ")
    if choice_val != 1:
        chosen_category[choice_val][0].picked = True
    return choice_val
         
def startGame(players):
    while True:
        if len(players) > 1:
            select_player = inputInt("Select player number to play: ")
            while select_player <= 0 or select_player > len(players):
                print("Please select valid player number. {} players are playing".format(len(players)))
                select_player = inputInt("Select player number to play: ")
            current_player = players[select_player-1]
        else:
            current_player = players[0]
        print("\n{} is playing...".format(current_player.name))
        show_options()
        choice = choose_category()
        if choice.lower() == "quit":
            break
        hash_keys = {k.lower(): v for k, v in my_hash.items()}
        chosen_category = hash_keys[choice]
        choice_val = choose_level(chosen_category)
        if choice_val == 1:
            continue
        question = chosen_category[choice_val][0].ques
        print("Here is your question:")
        print(question)
        ans = inputString("Enter your answer: ")
        if ans == str(chosen_category[choice_val][0].ans):
            print("Correct!")
            current_player.score = current_player.score + chosen_category[choice_val][0].val
        else:
            print("Sorry, wrong answer.")
            current_player.score = current_player.score - chosen_category[choice_val][0].val
        print("CURRENT SCORE: {}".format(current_player.score))
    return players

