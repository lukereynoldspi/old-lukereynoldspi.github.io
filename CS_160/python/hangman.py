import random
def random_word():
    words = random.randint(1,5)
    if words == 1:
        words = "APPLE"
    if words == 2:
        words = "CHAIR"
    if words == 3:
        words = "SPICY"
    if words == 4:
        words = "GAMES"
    if words == 5:
        words = "STAIN"
def user_input():
    input()
def hangman():
    print ("  ______")
    print ("  l     l")
    print ("  O     l")
    print ("--l--   l")
    print (" ( )    l")
    print ("        l")
    print ("---------")

