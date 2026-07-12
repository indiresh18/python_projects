print("program to guess random number")
print("====================================GUESS THE NUMBER GAME====================================")
import random
guess=random.randint(1,100)
count=0
def guessnum():
    global count
    print("guess a number between 1 and 100")
    num=int(input("enter your guess: "))
    count+=1
    if num==guess:
        print("congratulations! you guessed the number")
        print(f"you took {count} guesses.")
        return
    elif num<1 or num>100:
        print("invalid input! please enter a number between 1 and 100.")
    elif num+5>guess>num-5:
        print("you are very much close! try again.")
    elif num+10>guess>num-10:
        print("you are close! try again.")
    elif num<guess:
        print("too low! try again.")
    elif num>guess:
        print("too high! try again.")
    print("do u want to try again: (y/n)")
    choice=input().lower()
    if choice=='y':
        guessnum()
    else:
        print("thanks for playing!")
guessnum()