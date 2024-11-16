from graphics import*

print("Part1")

progressCount=0
excludeCount=0
moduleRetrieverCount=0
moduleTrailerCount=0
total_count=0

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
    
    # predict the progression outcome based on the entered credits
    outcome = predict_progression(pass_credits, defer_credits, fail_credits)
    return outcome

def main():
    # ask the user type student or staff
    while True:
        user_type = input("Please enter your user type (student or staff): ")

        # if the user is student predict the progression outcome and display it
        if user_type.lower() == 'student':
            result = predict_progression_for_student()
            print(result)
            break

        # if the user is staff continue the loop for predicting outcomes
        elif user_type.lower() == 'staff':
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
            
                # break the loop if q is entered
                if continue_prompt.lower() == 'q':
                    break

            def display_histogram():
                win=GraphWin("My Window", 800, 500)
                win.setBackground(color_rgb(232, 245, 233))
                
            #draw line
                
                pt1 = Point(50, 400)
                pt2 = Point(700, 400)
                ln = Line(pt1, pt2)
                ln.setOutline(color_rgb(100, 100, 100))
                ln.setWidth(0.625)
                ln.draw(win)

            #display histogram result
                
                txt = Text(Point(168, 50), "Histogram Results")
                txt.setTextColor(color_rgb(55, 71, 79))
                txt.setStyle('bold')
                txt.setSize(17)
                txt.setFace("times roman")
                txt.draw(win)

            #display outcomes in total
                
                outcome_text = "{} Outcomes in total".format(total_count)
                txt_total_outcome = Text(Point(180, 470), outcome_text)
                txt_total_outcome.setTextColor(color_rgb(55, 71, 79))
                txt_total_outcome.setStyle('bold')
                txt_total_outcome.setSize(15)
                txt_total_outcome.setFace("times roman")
                txt_total_outcome.draw(win)

            #display progress,trailler,retriever,excluded
                
                txt = Text(Point(125, 413), "Progress")
                txt.setTextColor(color_rgb(55, 71, 79))
                txt.setStyle('bold')
                txt.setSize(10)
                txt.setFace("times roman")
                txt.draw(win)
                
                txt = Text(Point(243, 413), "Trailler")
                txt.setTextColor(color_rgb(55, 71, 79))
                txt.setStyle('bold')
                txt.setSize(10)
                txt.setFace("times roman")
                txt.draw(win)
                
                txt = Text(Point(361, 413), "Retriever")
                txt.setTextColor(color_rgb(55, 71, 79))
                txt.setStyle('bold')
                txt.setSize(10)
                txt.setFace("times roman")
                txt.draw(win)

                txt = Text(Point(479, 413), "Excluded")
                txt.setTextColor(color_rgb(55, 71, 79))
                txt.setStyle('bold')
                txt.setSize(10)
                txt.setFace("times roman")
                txt.draw(win)


            #draw bars
                
                bar1 = Rectangle(Point(75, 400), Point(185, (400 - progressCount * 20)))
                bar1.setFill(color_rgb(144, 238, 144))
                bar1.draw(win)
                
                bar2 = Rectangle(Point(193, 400), Point(303, (400 - moduleTrailerCount * 20)))
                bar2.setFill(color_rgb(147, 197, 114))
                bar2.draw(win)
                
                bar3 = Rectangle(Point(311, 400), Point(421, (400 - moduleRetrieverCount * 20)))
                bar3.setFill(color_rgb(138, 154, 91))
                bar3.draw(win)
                
                bar4 = Rectangle(Point(429, 400), Point(539, (400 - excludeCount * 20)))
                bar4.setFill(color_rgb(224, 191, 184))
                bar4.draw(win)
                

            # labelling the bars

                label_progress = Text(Point(130, (400 - progressCount * 20) - 10), str(progressCount))
                label_progress.setTextColor(color_rgb(55, 71, 79))
                label_progress.setStyle('bold')
                label_progress.setSize(10)
                label_progress.setFace("times roman")
                label_progress.draw(win)

                label_trailer = Text(Point(248, (400 - moduleTrailerCount * 20) - 10), str(moduleTrailerCount))
                label_trailer.setTextColor(color_rgb(55, 71, 79))
                label_trailer.setStyle('bold')
                label_trailer.setSize(10)
                label_trailer.setFace("times roman")
                label_trailer.draw(win)

                label_retriever = Text(Point(366, (400 - moduleRetrieverCount * 20) - 10), str(moduleRetrieverCount))
                label_retriever.setTextColor(color_rgb(55, 71, 79))
                label_retriever.setStyle('bold')
                label_retriever.setSize(10)
                label_retriever.setFace("times roman")
                label_retriever.draw(win)

                label_exclude = Text(Point(484, (400 - excludeCount * 20) - 10), str(excludeCount))
                label_exclude.setTextColor(color_rgb(55, 71, 79))
                label_exclude.setStyle('bold')
                label_exclude.setSize(10)
                label_exclude.setFace("times roman")
                label_exclude.draw(win)

                win.getMouse()
                win.close()
                
            display_histogram()
            break
        else:
            print("Invalid user type")
main()


