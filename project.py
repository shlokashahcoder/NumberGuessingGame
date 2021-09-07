import random

luckNum = random.randint(1,100)
chances= 3

while(chances>0):
    userNum = int(input("enter your guess"))
    if userNum>luckNum:
        chances = chances-1
        if chances>0:
            print("guess a smaller number")
        else:
            print("your chances are over")
            print("the lucky number is :"+ str(luckNum))
        
    elif userNum==luckNum:
        print("your guess is correct!")
        chances = 0
    else: 
        chances = chances-1
        if chances>0:
            print("guess a bigger number")
        else:
            print("your chances are over")
            print("the lucky number is :"+ str(luckNum))
        

 