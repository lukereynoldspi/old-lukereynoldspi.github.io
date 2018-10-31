import random
def game():
    words = ["APPLE","CHAIR","SPICY","GAMES","STAIN","SMART","PITCH","STAMP"]
    wordchoice = random.choice(words)
    mistakes = 0
    print("Welcome to hangman! the max amount of letters in the word is 5.")
    #def keyword():


    def printhangman():
        if mistakes == 0:
            print ("  ______")
            print ("  l     l")
            print ("        l")
            print ("        l")
            print ("        l")
            print ("        l")
            print ("---------")
        if mistakes == 1:
            print ("  ______")
            print ("  l     l")
            print ("  O     l")
            print ("        l")
            print ("        l")
            print ("        l")
            print ("---------")
        if mistakes == 2:
            print ("  ______")
            print ("  l     l")
            print ("  O     l")
            print ("  l     l")
            print ("        l")
            print ("        l")
            print ("---------")
        if mistakes == 3:
            print ("  ______")
            print ("  l     l")
            print ("  O     l")
            print ("--l     l")
            print ("        l")
            print ("        l")
            print ("---------")
        if mistakes == 4:
            print ("  ______")
            print ("  l     l")
            print ("  O     l")
            print ("--l--   l")
            print ("        l")
            print ("        l")
            print ("---------")
        if mistakes == 5:
            print ("  ______")
            print ("  l     l")
            print ("  O     l")
            print ("--l--   l")
            print (" (      l")
            print ("        l")
            print ("---------")
        if mistakes == 6:
            print ("  ______")
            print ("  l     l")
            print ("  O     l")
            print ("--l--   l")
            print (" ( )    l")
            print ("        l")
            print ("---------")
            print ("GAME OVER")
            print ("The word was:")
            print (wordchoice)
            print ("Press enter to play again!") 
            input() 
            game()
    printhangman()
    #def guessinput():
    guessedletters = []
    while mistakes < 6:
        #guessinput()
        print ("Press 1 to guess the word. Guess a letter: ")
        print("---------------------------------------------")
        letterguess = input()
        if letterguess == "1":
            print("---------------------------------------------")
            print("What is the word?")
            print("---------------------------------------------")
            word = input()
            word = word.upper()
            if word == wordchoice:
                print("---------------------------------------------")
                print("CONGRATULATIONS")
                print("YOU WIN")
                print("Press enter to play again!")
                print("---------------------------------------------")
                input()
                game()
        letterguess = letterguess.upper()
        guessedletters.append(letterguess)
        print ("Guessed Letters:")
        print (guessedletters)
        
        if letterguess in wordchoice:
            printhangman()
            print ("Yes")
            print("---------------------------------------------")
        if letterguess not in wordchoice:
            mistakes = mistakes + 1
            printhangman()
            print ("No")
            print("---------------------------------------------")
            #guessinput()
        
    print(wordchoice)   
game()
