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

def startGame(score):
    choice = ""
    playerScore = score

    while choice != "quit":
        print("\nThe categories are:")

        for k in my_hash.keys():
            print(k)


        choice = input("\nPick a category: ")
        #choice = choice.lower()

        #Logic 1: Allows  
        if choice in my_hash:
            my_hash[choice]
            chosen_category = my_hash[choice]

            for k in chosen_category.keys():
                print(k)

            choice_val = int(input("Pick a value: "))
            question = chosen_category[choice_val][0].ques
        

            print("\nHere is your question:")
            print(question)
            ans = input("\nEnter your answer: ")

            if type(ans) is str:
                ans = ans.lower()
        #Deindent
            #print(ans == str(chosen_category[choice_val][0].ans))
            #if chosen_category[choice_val][0].picked == False:
        # Logic to add and remove points
                if ans == str(chosen_category[choice_val][0].ans):
                    print("\nCorrect!")
                    playerScore = playerScore + chosen_category[choice_val][0].val
                    print("\nCURRENT SCORE: {} \n".format(playerScore))
           
                else:
                    print("\nSorry, wrong answer.\n")
                    playerScore = playerScore - chosen_category[choice_val][0].val
                    print("CURRENT SCORE {} \n".format(playerScore))

        else:
            print("\nPlease choose from the given categories by typing exactly how it is shown. Type 'quit' if you're done playing")

