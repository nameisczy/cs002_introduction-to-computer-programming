key = False
death = False
game_over = False
door = False
import random

def birth_point():
    while True:
        print("You are now in an old residential building.")
        print("You were just sleeping.")
        print("As soon as you opened your eyes, you came here.")
        print("Was it a dream?")
        print("You observe your surroundings.")
        print("In front of you is an old elevator.")
        print("Behind you is the door to get out. Somehow it's a foggy mess outside.")
        
        choice = str.lower(input("What would you like to do? (enter the elevator or leave the building) "))

        if choice == "enter the elevator":
            return "elevator"
        elif choice == "leave the building":
            return "outside"
        else:
            print("I don't understand this choice")

def outside():
    global death
    while True:
        print("You're outside now.")
        print("The fog outside is blood-colored.")
        print("There are faint shadows of other residential buildings in the distance.")
        print("Suddenly, you find the corners of your coat stained with blood.")

        choice1 = str.lower(input("What would you like to do? (keep going or go back to the building) "))

        if choice1 == "keep going":
            while True:
                print("There seems to be some sound")

                choice2 = str.lower(input("What would you like to do? (keep going or go back to the building) "))
                if choice2 == "keep going":
                    while True:
                        print("A dark shadow lunges at you")
                        print("You're dead")
                        print("Try again")
                        death = True
                        return "death"
                elif choice2 == "go back to the building":
                    print("You're back in the old residential building.")
                    print("The blood that gets on your body starts to heat up and you feel uncomfortable all over.")
                    print("You're dead")
                    print("Try again")
                    death = True
                    return "death"
                else:
                    print("I don't understand this choice")
        elif choice1 == "go back to the building":
            print("You're back in the old residential building")
            print("The blood that gets on your body starts to heat up and you feel uncomfortable all over.")
            print("You're dead")
            print("Try again")
            death = True
            return "death"
        else:
            print("I don't understand this choice")

def elevator():
    count = 0
    while True:
        print("This is an old elevator room.")
        print("You notice that there are small advertisements posted on the walls.")
        print("you learn that the residential building has 14 floors through the elevator button.")
        if count >= 2:
            print("It seems that only the button on the 14th floor is working well")
        choice = str.lower(input("What would you like to do? "))
        if choice == "check the ad":
            print("Nothing special about the ad")
        elif choice == "press the eleventh floor" or choice == "press the first floor" or choice == "press the second floor" or choice == "press the third floor" or choice == "press the fourth floor" or choice == "press the fifth floor" or choice == "press the sixth floor" or choice == "press the seventh floor" or choice == "press the eighth floor" or choice == "press the ninth floor" or choice == "press the tenth floor" or choice == "press the twelfth floor" or choice == "press the thirteenth floor":
            print("The button seems to be broken")
            count = count + 1
        elif choice == "press the fourteenth floor":
            return "corridor"
        else:
            print("I don't understand this choice")

def corridor():
    while True:
        print("It is a long corridor.")
        print("There is a half-open door at the end of the corridor.")
        print("The sound of an old-fashioned television set comes from inside the door.")
        choice = str.lower(input("What would you like to do? "))
        if choice == "knock on the door":
            print("A middle-aged woman open the door and say, 'You're here, come on in.'")
            return "living room"
        elif choice == "open the door":
            print("A middle-aged woman stand at the door, seemingly greeted for a long time, and say, 'You're here, come on in'")
            return "living room"
        else:
            print("I don't understand this choice")

def living_room():
    while True:
        print("You walk into the living room of the family.")
        print("The old TV plays boring programs.")
        print("There are three little girls sitting on the couch watching TV.")
        print("The three little girls glance at you lightly and turn their heads to watch TV again.")
        print("What is striking is that these three little girls look exactly the same.")
        print("The middle-aged woman says with little expression, 'These are my daughters, thank you for coming to their birthday.'")
        print("The mom enter the kitchen.")
        print("In front of you is the hallway to your room and on your left is the kitchen.")
        choice = str.lower(input("What would you like to go? "))
        if choice == "hallway":
            return "hallway"
        elif choice == "kitchen":
            print("The kitchen is locked. You can't get in.")
        elif choice == "go out of the door":
            print("The door is locked")
        else:
            print("I don't understand this choice")
            
def livingroom():
    global death
    while True:
        print("This is the living room.")
        print("In front of you is the hallway to your room and on your left is the kitchen.")
        print("There is a cake on the table.")
        print("Three little girls were sitting on the couch watching TV.")
        print("Their mothers are standing next to them.")
        choice = str.lower(input("What would you like to do?"))
        if choice == "hallway":
            return "hallway"
        elif choice == "kitchen":
            print("The kitchen is locked. You can't get in.")
        elif choice == "go out of the door":
            print("The door is locked")
        elif choice == "Eat the cake":
            print("You feel sick to your stomach.")
            print("You're dead")
            print("Try again")
            death = True
            return "death"
        elif choice == "Cut the cake":
            print("You find a key in the cake.")
            key = True
            if door == True:
                print("Get out of here from the rooftop")
            else:
                print("Find the door to get out of here")
        elif choice == "TV":
            print("Nothing special about the TV")
        elif choice == "girls":
            print("The first girl says, 'My name is one.' The second girl says, 'My name is two'. The third girl says, 'My name is three. You must remember us.'")
            answer = str.lower(input("Now you say who I am. "))
            if answer == "one":
                answer = 1
            elif answer == "two":
                answer = 2
            elif answer == "three":
                answer = 3
            num = random.randint(1,3)
            if answer == num:
                print("You're right")
                print("Three little girls smiled at you together")
            else:
                print("The three little girls were angry.")
                print("They threw their handful of drinks on you.")
                print("You smell a puff of blood.")
                print("The blood that gets on your body starts to heat up and you feel uncomfortable all over.")
                print("You're dead")
                print("Try again")
                death = True
                return "death"
        elif choice == "mom":
            print("The mom says:'Thank you for coming to my daughters' birthday. They must have had a great time.'")
        else:
            print("I don't understand this choice")

def hallway():
    while True:
        print("This is the hallway of this home.")
        print("It connects the mother's room, the daughter's room, the bathroom and the stairwell.")
        choice = str.lower(input("What would you like to go? "))
        if choice == "the mother's room" or choice == "the daughter's room":
            print("The door to the room is locked.")
            print("You can't get in.")
        elif choice == "the bathroom":
            return "bathroom"
        elif choice == "stairwell":
            return "stairwell"
        elif choice == "living room":
            return "livingroom"
        else:
            print("I don't understand this choice")

def bathroom():
    global death
    while True:
        print("This is the bathroom.")
        print("There is a sink, a toilet and a shower.")
        choice = str.lower(input("What whould you like to do? "))
        if choice == "wash hands" or "take a shower":
            print("You find that the water is blood-colored.")
            print("The blood that gets on your body starts to heat up and you feel uncomfortable all over.")
            print("You're dead")
            print("Try again")
            death = True
            return "death"
        elif choice == "toilet":
            print("You feel good.")
            print("You find that the water is blood-colored.")
        elif choice == "hallway":
            return "hallway"
        else:
            print("I don't understand this choice")

def stairwell():
    while True:
        print("This is the stairwell.")
        print("You can go up to the rooftop or you can go down.")
        choice = str.lower(input("What would you like to go? "))
        if choice == "up" or choice == "the rooftop":
            return "rooftop"
        elif choice == "down":
            print("You find that only the fourth floor and the first floor are inhabited.")
            print("There is a man living on the fourth floor.")
            print("He looks terrified.")
            print("He urges you to get out of here.")
            print("An old lady lives on the first floor.")
            print("She keeps repeating that she has eaten and doesn't need to eat anymore.")
            print("You go back to the stairwell on the 14th floor")
        elif choice == "hallway":
            return "hallway"

def rooftop():
    while True:
        print("You come to the rooftop and find a door to get out of here")
        door = True
        choice = str.lower(input("What would you like to do? "))
        if choice == "open the door":
            if key == True:
                death = True
                game_over = True
                return "gameover"
            else:
                print("The door is locked")
        elif choice == "stairwell":
            return "stairwell"
        else:
            print("I don't understand this choice")
        
room = "birth point"

while game_over == False:
    death = False
    while death == False:
        if room == "birth point":
            room = birth_point()
        elif room == "outside":
            room = outside()
        elif room == "elevator":
            room = elevator()
        elif room == "corridor":
            room = corridor()
        elif room == "living room":
            room = living_room()
        elif room == "hallway":
            room = hallway()
        elif room == "livingroom":
            room = livingroom()
        elif room == "bathroom":
            room = bathroom()
        elif room == "stairwell":
            room = stairwell()
        elif room == "rooftop":
            room = rooftop()
        print()
    print("Based on the Grimm's fairy tale Fitcher's Bird.")
print()    
print("Game over, you win!")
        
