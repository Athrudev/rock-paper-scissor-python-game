import random
import os

l=['r','p','s']
d={
    'r':'ROCK',
    'p':'PAPER',
    's':'SCISSOR'
}

user_score = 0
com_score = 0



def rock_paper_scissors_art():
    return """
    Let's shake hands and count to three, just like old times. Rock, Paper, Scissors!
    
         _______
     ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
         ROCK
    
         _______
     ---'    ____)____
                ______)
               _______)
              _______)
    ---.__________)
         PAPER
    
         _______
     ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
        SCISSORS
    """




def menu(user_name,age):
    global user_score,com_score
    while True:
        
        print("\n\t\t\t|--------------MENU--------------|")
        print("\t\t\t\t1.Menu\n\t\t\t\t2.Update User Details\n\t\t\t\t3.Start Game\n\t\t\t\t4.View Score\n\t\t\t\t5.Exit")
        print("\t\t\t|--------------------------------|")
        
        c=int(input("Enter your choice:"))
        if c==1:
            menu(user_name,age)
        elif c==2:
            user_details()
        elif c==3:
           user_score,com_score = play_game(user_name,age,user_score,com_score)
        elif c == 4:
            view_score(user_name)
        elif c==5:
            print("Thank you for Playing with us\nI hope you enjoy your time...!")
            exit()
        else:
            print("Invalid Choice")
            break
    
def user_details():
    
    user_name=input("Enter Your Name: ")
    age=input("Enter Your age: ")
    menu(user_name,age)

def get_user(l):
    c=input("Your move:").lower()
    if c in l:
        return c
    else:
        print("Invalid Choice")

def get_computer(l):
    c=random.choice(l)
    return c

def winner(user_c,com_c):
    
    if user_c == com_c:
        return "Its a Tie...!" 
    elif(
        (user_c=='r' and com_c=='s')or
        (user_c=='s' and com_c=='p')or
        (user_c=='p' and com_c=='r')
        ):
        return "You win..!"
    else:
        return "Computer win...!"
    

def play_game(user_name,age,user_score,com_score):
   # global user_score,com_score
    rounds=int(input("What do you want to play\n Best of 3 or 5: "))
    if rounds==3 or rounds==5:
        for _ in range(rounds):
            
            
            print("\nPress 'r' for ROCK")
            print("Press 'p' for PAPER")
            print("Press 's' for SCISSOR\n")
            
            user_choice=get_user(l)
            com_choice=get_computer(l)
            
            if user_choice in l:    
                
                print(f"\n{user_name} choose '{d[user_choice]}'")
                print(f"Computer choose '{d[com_choice]}'")
                
                res=winner(user_choice,com_choice)
                if "You" in res:
                    user_score+=1
                elif "Computer" in res:
                    com_score+=1
                    
                print(res,"\n")
                
            else:
                #break
                return user_score, com_score
        print("\n\n\t|------------------------------------------------------|")        
        print(f"\t\t\t'{user_name}' score is {user_score}")
        print(f"\t\t\t'Computer' score is '{com_score}'")
        if user_score == com_score:
            print(f"\t\toh It's a 'Tie'\n\t\t\tPlay Again to beat Computer....?")
        elif user_score > com_score:
            print(f"\t\tCongrat's '{user_name}' you are the ultimate Winner...!")
        else:
            print(f"\t\tSorry '{user_name}' You have lost against Computer\n\t\t\tPlay Again to beat Computer....?")
        print("\t|------------------------------------------------------|\n\n")
        
        #break
        return user_score, com_score       
    else:
        print("\nSorry Invalid Choice")
        return user_score, com_score
        
    
def view_score(user_name):
        
        global user_score, com_score
        print(f"\n----- Current Scores -----")
        print(f"{user_name}'s score: {user_score}")
        print(f"Computer's score: {com_score}")
        print("---------------------------\n")

print("|---------------------------------------|WELCOME TO GAME|---------------------------------------|")
print(rock_paper_scissors_art())
print("\n\nFirst Register with your Name (You can update it later)")
user_name,age=user_details()


