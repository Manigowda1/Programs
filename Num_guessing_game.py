import math
import random

l = int(input("Enter lower bound "))
u = int(input("Enter Upper bound "))
x = random.randint(l, u)
print(x)
chance=round(math.log2(u - l + 1))
print(f"You have got {chance} chances to guess")
count =0
while count<chance:
    count=count+1
    guess = int(input("Enter your guess here "))
    if guess == x:
        print("Congrats you have guessed correct number")
        exit()
        '''Dont use break here because it only terminates loop'''
    elif guess<x:
        print("Try again! you entered lesser number than the number. Try higher value")
    elif guess>x:
        print("Try again! you entered greater number than the number. Try smaller value")
    else:print(f"Guess the number within range{u} to {l}")
print(f"your lost all the chances. The number is {x} .Better luck next time")




