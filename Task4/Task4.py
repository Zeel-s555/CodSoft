import random
from tkinter import *

#Dictionary and vars
schema = {
    "Rock":{"Rock":1, "Paper":0, "Scissor":2},
    "Paper":{"Rock":2, "Paper":1, "Scissor":0},
    "Scissor":{"Rock":0, "Paper":2, "Scissor":1}
}
comp_score = 0
player_score = 0

#Functions
def outcome_handler(user_choice):
    global comp_score
    global player_score
    outcomes = ["Rock", "Paper", "Scissor"]
    random_number = random.randint(0,2)
    computer_choice = outcomes[random_number]
    result = schema[user_choice][computer_choice]
    
    player_choice_label.config(fg="green", text="Player Choice : "+str(user_choice))
    computer_choice_label.config(fg="red", text="Computer Choice : "+str(computer_choice))
    
    if result == 2:
        player_score = player_score + 1
        player_score_label.config(text="Player :"+str(player_score))
        outcome_label.config(fg="blue", text="Outcome : Player Won")
        
    elif result == 1:
        player_score = player_score + 0
        comp_score = comp_score + 0
        player_score_label.config(text="Player :"+str(player_score))
        computer_score_label.config(text="Computer :"+str(comp_score))
        outcome_label.config(fg="blue", text="Outcome :Draw")
        
    elif result == 0:
        comp_score = comp_score + 1
        computer_score_label.config(text="Computer :"+str(comp_score))
        outcome_label.config(fg="blue", text="Outcome : Computer Won")    


#Main Screen
master = Tk()
master.title("Rock-Paper-Scissor")

#Labels
Label(master, text="Rock, Paper, Scissor", font=("Calibri", 14)).grid(row=0, sticky=N, pady=10, padx=200)
Label(master, text="Please select an option", font=("Calibri", 12)).grid(row=1, sticky=N)

player_score_label = Label(master, text="Player : 0", font=("Calibri", 12))
player_score_label.grid(row=2, sticky=W)
computer_score_label = Label(master, text="Computer : 0", font=("Calibri", 12))
computer_score_label.grid(row=2, sticky=E)

player_choice_label = Label(master, font=("Calibri", 12))
player_choice_label.grid(row=3, sticky=W)
computer_choice_label = Label(master, font=("Calibri", 12))
computer_choice_label.grid(row=3, sticky=E)

outcome_label = Label(master, font=("Calibri", 12))
outcome_label.grid(row=3, sticky=N)

#Buttons
Button(master, text="Rock", width=15, command=lambda:outcome_handler("Rock")).grid(row=4, sticky=W, padx=5, pady=5)
Button(master, text="Paper", width=15, command=lambda:outcome_handler("Paper")).grid(row=4, sticky=N, pady=5)
Button(master, text="Scissor", width=15, command=lambda:outcome_handler("Scissor")).grid(row=4, sticky=E, padx=5, pady=5)

#Dummy Label
Label(master).grid(row=5)
master.mainloop()