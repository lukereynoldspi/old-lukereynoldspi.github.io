import random



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
for i in games:
    print (i)
for i in music:
    print (i)
