# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
# Student ID:  w2053165
# Date: 10/12/2023

print("Part3")

progressCount=0
excludeCount=0
moduleRetrieverCount=0
moduleTrailerCount=0
total_count=0
progression_data = []

# estimate the progression outcome based on credits
def predict_progression(pass_credits, defer_credits, fail_credits):
    global progressCount, moduleTrailerCount, moduleRetrieverCount, excludeCount, total_count
    
    # calculating the total of all three marks entered.
    total_credits = pass_credits + defer_credits + fail_credits
    
    # checking if total credits are not equal to 120
    if total_credits != 120:
        return "Total incorrect"
    
     # checking the credit values
    if pass_credits == 120:
        progressCount=progressCount+1
        outcome = "Progress"
        
    elif pass_credits == 100:
        moduleTrailerCount=moduleTrailerCount+1
        outcome = "Progress (module trailer)"

    elif pass_credits == 0 and defer_credits == 120:
        moduleRetrieverCount=moduleRetrieverCount+1
        outcome = "Do not progress – module retriever"
        
    elif pass_credits >= 60 or (pass_credits >= 20 and defer_credits >= 60):
        moduleRetrieverCount=moduleRetrieverCount+1
        outcome = "Do not progress – module retriever"          
        
    elif fail_credits >= 80:
        excludeCount=excludeCount+1
        outcome = "Exclude"

    elif fail_credits > 0:
        moduleRetrieverCount = moduleRetrieverCount + 1
        outcome = "Do not progress – module retriever"
         
    else:
        outcome = "Invalid input"
    
    total_count=progressCount+moduleTrailerCount+moduleRetrieverCount+excludeCount
    return outcome

# checking if a value can be converted to an integer
def integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# checking the credit values are in this list
def valid_credit(credit):
    return credit in [0, 20, 40, 60, 80, 100, 120]

# input the credits at pass, defer and fail
def predict_progression_for_student():
    pass_credits = input("Please enter your credits at pass: ")
    
    # checking the input can be converted to an integer
    if not integer(pass_credits):
        return "Integer required"
    pass_credits = int(pass_credits)
    # checking the integer in credit range
    if not valid_credit(pass_credits):
        return "Out of range."

    defer_credits = input("Please enter your credits at defer: ")
    # checking the input can be converted to an integer
    if not integer(defer_credits):
        return "Integer required"
    defer_credits = int(defer_credits)
    # checking the integer in credit range
    if not valid_credit(defer_credits):
        return "Out of range."

    fail_credits = input("Please enter your credits at fail: ")
    # checking the input can be converted to an integer
    if not integer(fail_credits):
        return "Integer required"
    fail_credits = int(fail_credits)
    # checking the integer in credit range
    if not valid_credit(fail_credits):
        return "Out of range."
    
    credits_identifier = f"{pass_credits},{defer_credits},{fail_credits}"

    # checking to see if there is a file if there is not create it
    try:
        with open("progression_data.txt", "r"):
            pass
    except FileNotFoundError:
        open("progression_data.txt", "w").close()

    with open("progression_data.txt", "r") as file:
        if credits_identifier + '\n' in file.readlines():
            return "Progression data already exists for these credits."

    outcome = predict_progression(pass_credits, defer_credits, fail_credits)

    with open("progression_data.txt", "a") as file:
        file.write(f"{outcome} - {credits_identifier}\n")

    return outcome
    
# loop continuosly predict the progression outcome of students
while True:
    result = predict_progression_for_student()
    print(result)
    
    # ask the user to continue or quit
    while True:
        continue_prompt = input("Enter 'y' to predict for another student or 'q' to quit: ")
        
        # checking if the input is q or y
        if continue_prompt.lower() == 'q':
            break
        elif continue_prompt.lower() == 'y':
            break
        else:
            print("Invalid input")
            continue
        
    # break the loop if q is entered
    if continue_prompt.lower() == 'q':
        break

# getting the stored data and printing them
def print_stored_progression_data():
    with open("progression_data.txt", "r") as file:
        stored_data = file.readlines()
        for data in stored_data:
            print(data.strip())

# print the stored progression data
print_stored_progression_data()
