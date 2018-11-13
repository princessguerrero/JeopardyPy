# This function repeatedly prompts for input until an integer is entered.
def inputInt(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except:
           print("Invalid input. Enter an integer")
    

# This function repeatedly prompts for input until something other than whitespace is entered.
def inputString(prompt):
    while True:
        user_input = input(prompt)
        if user_input is not None and user_input.strip() != "":
            return user_input
        else:
            print("Please enter something!!!")
    
