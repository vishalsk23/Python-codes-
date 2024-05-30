#Quiz Game programme
#Speak function
#File Hnadling for high score
#No line wise randdom selection
#exception Handling
from login_method import login
from question_ans import questionbnk
from voice_access import say
from random_generate import random_num 
import pyttsx3

#na = input("Before start Enter Your name : ")
game = input("\nPress 1 for KBC and Other key Quiz Game : ")
game = True if (game == "1") else False
voice_input = input("press 1 for activate voice ")
voice = True if voice_input == 1 else False
 

game = True

   

def wonprize(money):
    if (money >= 2000)and (money <= 7000):
        print("congratulaiton you won 1000")
    elif (money >= 8000)and (money <= 14000):
        print("congratulaiton you won 14000")
    else:
        print("Bad luck you won 0")
        

def qmatch():
    pass
              

def kmatch(ques,rnum):
    '''Question Printing and matching from the list and return true false if question is wrong or right pass parameter(listname,questionIndex) for matching answere '''
    
    #qlen = len(ques)   
    #rnum = random_num(qlen,random_num_list)
    #random_num_list.append(rnum)
    rnum = rnum
    question = ques[rnum][0]
    print(question)
    print(f"1. {ques[rnum][1]}",f"\n2. {ques[rnum][2]}",f"\n3. {ques[rnum][3]}",f"\n4. {ques[rnum][4]}")
    
    
    option = f"1. {ques[rnum][1]}",f"2. {ques[rnum][2]}",f"3. {ques[rnum][3]}",f"4. {ques[rnum][4]}"

    voice = True
    if  voice == True:
        try:
            say(question)
            say(option)
        except ModuleNotFoundError :
            print("You Haven't install module pyttsx3 install it")
            voice = False
    
    
    
    r = input("type ans or press 0 for Quit  : ")

    if (r == "0"):
        return exit
    elif ( (r  == f"{(ques[rnum][-1])}") or (r  == f"{(ques[rnum][-2])}") ):
        return True
    else:
        return False
        
"""def ran(qlen,random_num_list):
    rnm1 =  random_num_list
    stmt = True 
    while stmt:
         r = random.randrange(0,qlen)
         if(r in rnm1):
             continue
         else :
             stmt = False
             return r  """

def call(ques):
    ans = []
    random_num_list = []
    level = [1000,4000,8000,14000]
    qlen = len(ques)
    for i in range (0,qlen):
        
        rnum = random_num(qlen,random_num_list)
        random_num_list.append(rnum)
           
        #if (game):
        print(f"\nQuestion for {level[i]} Rs ")  
        a = kmatch(ques,rnum)
        
        money = level[i]
        if (a == exit):
            money = level[i-1]
            print(f"\nYou'r taking money {money} Thank-you for playing the KBC Game")
            break
        elif(len(level) == 3):
            wonprize(money)
        elif (a == False):
            print("Wrong Answere...! \t Better Luck next time")
            wonprize(money)
            break

        """else :
            print(ques[i][0])
            print(f"1. {ques[i][1]}",f"\n2. {ques[i][2]}",f"\n3. {ques[i][3]}",f"\n4. {ques[i][4]}")
            """
##            res = input("type ans : ")
##            ans.append(res)
            
    print()
    




flag = True #login()
if flag:
    ques = questionbnk()
    call(ques)






























