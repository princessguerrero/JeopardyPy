class Question:
    def __init__(self, ques, ans):
        self.ques = ques
        self.ans = ans

# questions for GenOne
q1, q2 = Question("How many members were selected for the GenOne program?", "20"), Question("Which company worked with #YesWeCode for the GenOne initiative?", "infor")
q3, q4 = Question("Who is the founder of #YesWeCode?", "van jones"), Question("What is the DreamCorps logo?", "dragon")

# questions for Linux
q5 = Question("What animal is the mascot for Linux?", "penguin")
q6 = Question("What is the command that tells the process to die gracefully?", "kill")
q7 = Question("What is the command that changes file permissions?", "chmod")
q8 = Question("Who is the founder of Linux?", "linus torvalds")

# questions for Python
q9 = Question("What is an immutable array in Python?", "list")
q10 = Question("What keyword do you use to get a library?", "import")
q11 = Question("What do you use to extract content from a website?", "web scraping")
q12 = Question("What is the process of detecting and removing potential errors in your program?", "debug")

# questions for Career Building
q13 = Question("What is the best social platform to connect to professionals?", "linkedin")
q14 = Question("What is infor's software that has educational training resources to learn more about their company?", "lms")
q15 = Question("The process of developing contacts in one's career.", "networking")
q16 = Question("What is the acronym for the research tool that was developed by Kenneth Thomas and Ralph Kilmann in the early 1970s?", "tki")


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

def startGame():
    choice = ""


    while choice != "quit":
        for k in my_hash.keys():
            print(k)


        choice = input("Pick a category: ")
        #choice = choice.lower()

        #Logic 1: Allows  
        if choice in my_hash:
            my_hash[choice]
            chosen_category = my_hash[choice]

            for k in chosen_category.keys():
                print(k)

            choice_val = int(input("Pick a value category: "))
            question = chosen_category[choice_val][0].ques



            if type(ans) is str:
                ans = ans.lower()
                
        choice_val = int(input("Pick a value: "))
        question = chosen_category[choice_val][0].ques
        

        print("Here is your question:")
        print(question)
        ans = input("Enter your answer: ")


            print(ans == str(chosen_category[choice_val][0].ans))




        # print(ans == str(chosen_category[choice_val][0].ans))
        if ans == str(chosen_category[choice_val][0].ans):
            print("Your answer is correct!")
        else:
            print("Sorry, wrong answer.")

    else:
        print("Please choose from the given categories by typing exactly how it is shown. Type 'quit' if you're done playing")

