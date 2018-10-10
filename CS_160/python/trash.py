import random

x = input("Type games or music. ")
if x == ("games"):
    print ("So you like games?")
    print ("What is your favorite?")
    print ("a. Overwatch")
    print ("b. Smash")
    print ("c. Xenoblade")
    x = input()
    if x == ("a"):
        print ("Play of the Game")
    if x == ("b"):
        print ("Ultimate Choice")
    if x == ("c"):
        print ("Weeb")

if x == ("music"):
    print ("So you like music?")
    print ("What is your favorite?")
    print ("a. ELO")
    print ("b. Bowie")
    print ("c. Rogers")
    x = input()
    if x == ("a","A","a."):
        print ("That's out of the blue")
    if x == ("b"):
        print ("You are like a Star, man")
    if x == ("c"):
        print ("Hold it!")

print ("Hello World!")
music = ["ELO", "Bowie", "Parsons" ]
x=0
print (music[0])
print (music[1])
print (music[2])
print (len(music))
if x==0:
    music.append("Rogers")
print (music[3])
if x==0:
    music.remove("Parsons")
print (music)
print (music[2])
games = ["Overwatch","Smash",]
print (games)
games.append("Xenoblade")
print (games)
music.sort()
print (music)
print (music + games)
everything = (music + games)
print (everything)
print (everything[5])
for i in range(10):
    print (everything[5])
print(type(games))