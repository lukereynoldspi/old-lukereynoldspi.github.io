import random
import sys
def mastermind():
    game = 1
    guesses = 8
    colors = ["R", "G", "B", "W",]
    spotone = random.choice(colors)
    spottwo = random.choice(colors)
    spotthree = random.choice(colors)
    spotfour = random.choice(colors)
    colorlist = []
    colorlist.append(spotone)
    colorlist.append(spottwo)
    colorlist.append(spotthree)
    colorlist.append(spotfour)



    print("Welcome to Mastermind! You have 8 guesses to find the correct color combo,")
    print("there are 4 colors, Red, Green, Blue, White.")
    print("To input your answer, put the first letter of each color in the order")
    print("you want, such as RGBW for example. B means right color wrong position,")
    print("C means right position and color, and N means the color is not in the combo.")
    print("------Good Luck!------")
    while game == 1: 
        guess = input()
        guess = guess.upper()
        guess = list(guess)
        print (guess)
        #print (colorlist)
        if len(guess) == len(colorlist):
            if guess == colorlist:
                print ("YOU WIN!")
                print ("Would you like to play again? Y/N")
                answer = input()
                answer = answer.upper()
                if answer == "Y":
                    mastermind()
                if answer == "N":
                    end()
                if answer != "Y" or "N":
                    print ("Sorry, what?")

            for item in guess[0]:
                if item in colorlist[0]:
                    print ("C")
                if item in colorlist [1-3] and item not in colorlist[0]:
                    print ("B")
                elif item not in colorlist[0-3]:
                    print("N")
            for item in guess[1]:
                if item in colorlist[1]:
                    print ("C")
                if item in colorlist[0] or colorlist[2-3] and item not in colorlist[1]:
                    print ("B")
                elif item not in colorlist[0-3]:
                    print("N")
            for item in guess[2]:
                if item in colorlist[2]:
                    print ("C")
                if item in colorlist[0-1] or colorlist[3] and item not in colorlist[2]:
                    print ("B")
                elif item not in colorlist[0-3]:
                    print("N")
            for item in guess[3]:
                if item in colorlist[3]:
                    print ("C")
                if item in colorlist[0-2] and item not in colorlist[3]:
                    print ("B")
                elif item not in colorlist[0-3]:
                    print("N")
                    

            #if guess not in colorlist:
            #print ("None match :(")
            guesses = guesses - 1
            print ("You have")
            print (guesses)
            print ("guesses left!")
            if guesses == 0:
                print("Game Over")
                print(colorlist)
                print("Press enter to play again! ")
                input("")
                mastermind()
        if len(guess) != len(colorlist):
            print ("please select 4 colors.")
def end():
    print ("Thanks for playing!")
    input()
    end()
mastermind()
