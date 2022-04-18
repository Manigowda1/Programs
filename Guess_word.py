import random

name = input("Enter your name ")

print("Good Luck!", name)

words = ["Mani", "Python", "Oneplus", "Nokia"]

word=random.choice(words)


turn=5

guesses=''
while turn>0:
    fail=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            fail+=1

    if fail == 0:
        print("You win")
        print("The word is " + word)
        break
    guess = input("Enter the characters ")
    guesses = guesses + guess
    if guess not in word:
        turn -= 1
        print(f"you have {turn} chances")
    if turn ==0:
        print("You lost")










