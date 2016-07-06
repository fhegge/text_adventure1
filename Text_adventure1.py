import time
hp = 30

print ("You are standing on a path at the edge of a jungle. there is a cave to your left and a beach to your right.")
time.sleep (1)

# Question1
direction1 = input ("Do you want to go left or right? ")

direction1 = direction1.lower ()

if direction1 == "left":
    print ("You walk to the cave and notice there is an opening. You walk through it and fall off a cliff into the water.")
    print ("You lose 20 health points. You have 10 helth points left.")
    hp = hp - 20


elif direction1 == "right":
    print ("you walk to the beach but remember you do not have any swimwear.")
    time.sleep (2)
    print ("The cool water revitalizes you. You have never felt more alive. You gain 70 health points. You now have 100 points!")
    hp += 70

else:
    print ("Sorry, invalid answer. Goodbye.")
time.sleep (2)

#Question2
direction2 = input ("Do you want to fly or swim?\n")

direction2 = direction2.lower ()

#Fly

if direction2 == "fly":
    print ("You fly above the beautiful clear waters to the shore, but are too amazed by the sight to see the flying pigs approach.") 
    time.sleep (2)
    print ("You see the wings flapping, and they aproach you. You try to fly faster, but they catch up and eat you.")
hp = hp - 100


#Swim

if direction2 == "swim":
    print ("You swim across the beautiful clear waters and reach the sandy shore. A grin spreads across your face. You gain 50 points.")



print ("Your jorney has come to an end. Thanks for playing!")
