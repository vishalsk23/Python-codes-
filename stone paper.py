#stone paper scissors

import random as rd

st = ["stone","paper","scissors"]

flag = True

while True:
    ans1 = input("Enter your Choice : \n1. stone \n2. Paper \n3. scissors \n")
    ans = ans1.lower()
    
    if (ans == "0"):
        False
        break

    choi = rd.choice(st)
    print(f"computer choice is : {choi}")

    if((ans == "stone")or(ans == "1")):
        if(choi == "scissors"):
            print("You Win")
        elif(choi == "paper"):
            print("Computer Win")
        else:
            print("Draw")

    elif((ans == "paper")or(ans == "2")):
        if(choi == "stone"):
            print("you Win")
        elif(choi == "scissors"):
            print("Computer Win")
        else:
            print("Draw")        

    elif((ans == "scissors")or(ans == "3")):
        if(choi == "paper"):
            print("You win")
        elif(choi == "stone"):
            print("Computer Win")
        else:
            print("Draw")
            
    else:
        print("Invalid Input")
