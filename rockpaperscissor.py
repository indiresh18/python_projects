
import random
list=['rock','paper','scissors']
comp=0
user=0
i=1
print("-----WELCOME TO THE ROCK PAPER SCISSOR GAME!-----")
n=int(input("ENTER HOW MANY ROUNDS YOU WANNA PLAY:"))
while(i<=n):
    computer_choice=random.choice(list)
    user_choice=input("Enter your choice (rock, paper, scissors): ")
    if user_choice.lower()== computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice.lower() == 'rock':
        if computer_choice=='paper':
            print("Paper is the choice , computer wins")
            comp+=1
        elif computer_choice=='scissors':
            print("scissors is the choice, you won")
            user+=1
    elif user_choice.lower() == 'paper':
        if computer_choice=='scissors':
            print("scissors is the choice , computer wins")
            comp+=1
        elif computer_choice=='rock':
            print("rock is the choice, you won")
            user+=1
    elif user_choice.lower() == 'scissors':
        if computer_choice=='paper':
            print("Paper is the choice , you won")
            user+=1
        elif computer_choice=='rock':
            print("rock is the choice, computer wins")
            comp+=1
    i+=1
    
print("END RESULTS:")
if(user==comp):
    print("ITS A TIE !!")
elif(user>comp):
    print("YOU WON!!!")
else:
    print("YOU LOST COMPUTER WON")

        
               