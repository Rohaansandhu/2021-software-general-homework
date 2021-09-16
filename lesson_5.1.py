class robot:

    def __init__(self, position, arm_position, has_cube, score,):
        self.position = position
        self.arm_position = arm_position
        self.has_cube = has_cube
        self.score = score

    def move(self, direction,):
        if direction == "forward" or direction == "f":
            if self.position != 7:
                self.position += 1
                return(print("You moved forward, your postion is now " + str(self.position)))
        if direction == "backward" or direction =="b":
            if self.position != 0:
                self.position -= 1
                return(print("You moved backward, your position is now " + str(self.position)))
        print("Can't move that direction any more")

    def armmove(self, direction):
        if direction == "up" or direction == "u":
            if self.arm_position != 15:
                self.arm_position += 1
                return(print("Your arm moved up, your arm position is now " + str(self.arm_position)))
        if direction == "down" or direction == "d":
            if self.arm_position != 0:
                self.arm_position -= 1
                return(print("Your arm moved down, your arm position is now " + str(self.arm_position)))
        print("The arm can't move that direction any more")

    def pickup_cube(self):
        if self.position == 3:
            if self.arm_position == 0:
                if self.has_cube == False:
                    self.has_cube = True
                    return(print("You have picked up a cube"))
        print("You cannot pick up a cube")

    def score_cube(self):
        if self.position == 7:
            if self.has_cube:
                if self.arm_position == 10:
                    self.score += 5
                    self.has_cube = False
                    return(print("You scored! Your score is now: " + str(self.score)))
        print("You cannot score")

r1 = robot(0, 0, False, 0)

def start():
    print("Welcome to robot thing")
    print("Press w to go forward, s to go backward, a to go up, d to go down")
    print("Press q to pick up cube and press e to score or i for instructions")
    print("Type quit to quit")
    mainloop()

def mainloop():
    while True:
        user_input = input("Enter choice: ")
        if user_input == "w":
            r1.move("f")
        elif user_input == "s":
            r1.move("b")
        elif user_input == "a":
            r1.armmove("up")
        elif user_input == "d":
            r1.armmove("down")
        elif user_input == "q":
            r1.pickup_cube()
        elif user_input == "e":
            r1.score_cube()
        elif user_input == "quit":
            print("Your final score was " + str(r1.score))
            break
        elif user_input == "i":
            print("Press w to go forward, s to go backward, a to go up, d to go down")
            print("Press q to pick up cube and press e to score")
            print("Type quit to quit")
        else:
            print("Use one of the commands or press i for instructions")

start()