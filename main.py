print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

first = input('You\'re at a cross road. Where do you want to go? Type "left" or "right".')
if first == "left" :
    second = input("""You've come to a lake. There is an island in the middle of the lake.
               Type wait to "wait" for a boat. Type swim to "swim" across: """)
    if second == "wait":
        third = input("""You arrive at the island unharmed. There is a house with 3 doors.One red,
              one yellow and one blue. Which colour do you choose?: """)
        if third == "red":
            print("game over")
        elif third == "blue":
            print("game over")
        elif third == "yellow":
            print("you win")
        else:
            print("game over")

    else:
        print("game over")
else:
    print("game over")



