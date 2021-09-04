import math
# A student has taken 3 tests in a class, and wants to know their current grade 
# (which is only calculated by these tests). 

# Ask the user to input all three of the test scores for the student, one by one. 

# The program should then calculate the average test score (average is adding all three 
# test scores together then dividing by 3), and then print the student's letter grade 
# (as well as the average score as a number).



def testScores():
    try:
        math = input("Enter Math Score: ")
        math = int(math)
        if math > 100:
            print("Error, test scores must be below 100")
            return
        english = input("Enter English Score: ")
        english = int(english)
        if english > 100:
            print("Error, test scores must be below 100")
            return
        science = input("Enter Science Score: ")
        science = int(science)
        if science > 100:
            print("Error, test scores must be below 100")
            return
    except:
        print("Use numbers only")
        return

    average = (math + english + science) / 3
    if average >= 90:
        print("A")
    elif average >= 80:
        print("B")
    elif average >= 70:
        print("C")
    elif average >= 60:
        print("D")
    else:
        print("F")
    print(average)

testScores()

#########################################################

# Gregory wants to know how many toys they can buy at Toys'N'Us

# They prioritize buying the most expensive toys first (For ejm. If Gregory had $50 
# they'd end up buying 2 Jumbo Baby Yoda Plushies, 1 Beyblade, and 5 Sticky Hands with 
# a remainder of $0.30 left)


# Have the user input how much money Gregory has then print how many of each 
# toy they can afford, as well as how much money they'd have remaining

# The toys and prices are as follows:
# Jumbo Baby Yoda Plush - $20
# Beyblades - $7.20
# Sticky Hands - $0.50

baby_yoda = 20
beyblades = 7.2
hands = 0.5

def toys():
    m = input("Enter the amount of money Gregory has: ")
    m = float(m)
    g = True
    h = True
    i = True
    by = 0
    bb = 0
    sticky = 0
    while g:
        if m >= baby_yoda:
            m -= baby_yoda
            by += 1
            continue
        else:
            g = False
            break
    while h:
        if m >= beyblades:
            m -= beyblades
            bb += 1
            continue
        else:
            h = False
            break
    while i:
        if m >= hands:
            m -= hands
            sticky += 1
            continue
        else:
            i = False
            break
    m = round(m, 3)
    print("Gregory can afford " + str(by) + " Baby Yodas " + str(bb) + " Beyblades " + str(sticky) + " Sticky hands with a remainder of $" + str(m))


toys()

##########################################################################################

# Ryan is doing his math homework, but the (x!) key on Ryan’s calculator is broke, 
# you wanting to show off your programming skills so you told him that you will code something to help him do that.
# Your program will only accept an integer that is between 0 and 10; 
# if the number is less or equal to 0, 
# you will tell him that he broke the program and the program will now shut down. 
# If the number is more or equals to 10 and is an even number, 
# you will tell him that he overflood the program and print out the infinity inside the math library, math.inf. Otherwise just print “error”.
# If he entered a valid number, 
# you will then use the factorial fabs() function inside the math library to calculate the factorial.
# If this calculated factorial is below 100, print out this number. 
# If it is over 100, square it, print it out, and then ask Ryan if this seems correct. 
# If he guessed right, send him a congrats, but if he guessed it wrong, 
# tell him that his computer doesn’t like him anymore and print out a bunch of random letters.


def assignment_3():
    num = input("Enter a number between 0 and 10: ")
    try:
        num = int(num)
    except:
        print("no")
        quit()
    dum = num % 2
    if num <= 0:
        print("You broke the program and now the program will shut down")
        quit()
    elif num >= 10 and dum == 0:
        print("You overflooded the program")
        print(math.inf)
        quit()
    else:
        ans = math.factorial(num)
        if ans < 100:
            print(ans)
        else:
            ans *= ans
            print(ans)
    e = True
    c = 0
    while e:
        f = input("Did you guess right? (yes/no) ")
        if f == "yes":
            print("Congrats!")
            break
        elif f == "no":
            print("Your computer hates you")
            print("sawsedrftgyhjkmsdvcbqouwalrnfjsd")
            break
        else:
            print("it was a yes or no...")
            c += 1
            if c == 3:
                print("aqwsedrftvgyhuwoeausfbhjdbsfaiugfywueavfhjsdv")
                break


assignment_3()
