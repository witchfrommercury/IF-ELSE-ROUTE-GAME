#PLEASE RUN IT ON VS CODE OR GOOGLE COLLAB<3
#WITCHFROMMERCURYGITHUB

print("Hello! Welcome to my small game that I created.")
username = input("Pleade enter your username:")
print("Username is: " + username)

print(" ")    

a = input( username + "Do you want to enter the game? (yes/no)")

print(" ")    

if a == "yes":
    print("Great, let's continue!")
else:
    print("You don't have a choice :p .")


print(" ")    

print("You woke up from a dream and the first thing you notice is no one is there. What will you do?")

print(" ")    

print("A. You look at the kitchen.")
print("B. You go to the bathroom.")
print("C. You went to sleep again.")

print(" ")    

b = input("Answer:" " ")

print(" ")

if b == "A":
    print("You went to the kitchen and heard a sound.")
    print(" ")
    print("A. Peak thru the ladder.")
    print("B. Stop and went back to the bedroom.")
    print("C. Ignore it. ")
    print(" ")
if b == "A":
    print(" ")
    c = input("Answer: ")
if b == "B":
    print("You went to the bathroom and notice something on the mirror.")
    print(" ")
    print(" A. Look at the shower room. ")
    print(" B. RUn down the house.")
    print(" C. Look closely at it.")
else:
    print("NOTE :PLEASE USE CAPITAL LETTERS.")

print(" ")

if c == "A":
    print(" You died.")
else:
    print("NOTE :PLEASE USE CAPITAL LETTERS.")
