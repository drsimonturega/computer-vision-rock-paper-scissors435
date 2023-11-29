import random

class man_rps():

    def __init__(self):
        """Inintailises the class varibles bound to an instance of the class"""
        weapon_list = ["rock","paper","sissors"]
        self.weapon_list = weapon_list
        weapon_of_choice = str()
        weapon_of_computer = str()
        self.weapon_of_computer = weapon_of_computer
        self.weapon_of_choice = weapon_of_choice
       



def get_computer_choice(self, weapon_list):
    self.weapon_of_computer = random.choice(self.weapon_list)
    #print(f'Computer chosse {self.weapon_of_computer}')
    return self.weapon_of_computer

def get_user_choice(self, weapon_list):
    while True:
        self.weapon_of_choice = input('Choose rock, paper or sissors, ')
        self.weapon_of_choice = self.weapon_of_choice.lower()
        if self.weapon_of_choice in weapon_list:
            break
        else:
            print('Try again!')
            continue
    return self.weapon_of_choice

def get_winner(self, weapon_of_choice, weapon_of_computer):
    # checks choices if user choice is "rock"
    #print(f"check 1 computer {self.weapon_of_computer} you {self.weapon_of_choice}")
    if self.weapon_of_choice == "rock" and self.weapon_of_computer == "sissors":
       print(f' Your {self.weapon_of_choice} beats {self.weapon_of_computer}, YOU WIN')
    elif self.weapon_of_choice == "rock" and self.weapon_of_computer == "paper":
        print(f' Your {self.weapon_of_choice} is beaten by  {self.weapon_of_computer}, YOU LOSE')
    else:
        if self.weapon_of_choice == "rock" and self.weapon_of_computer == "rock":
            print(f' Your {self.weapon_of_choice} is the same as  {self.weapon_of_computer}, IT\'S A TIE')

    # checks choices if user choice is "sissors" 
    #print(f"check 2 computer {self.weapon_of_computer} you {self.weapon_of_choice}")         
    if self.weapon_of_choice == "sissors" and self.weapon_of_computer == "paper":
       print(f' Your {self.weapon_of_choice} beats {self.weapon_of_computer}, YOU WIN')
    elif self.weapon_of_choice == "sissors" and self.weapon_of_computer == "rock":
        print(f' Your {self.weapon_of_choice} is beaten by  {self.weapon_of_computer}, YOU LOSE')
    else:
        if self.weapon_of_choice == "sissors" and self.weapon_of_computer == "sissor":
            print(f' Your {self.weapon_of_choice} is the same as  {self.weapon_of_computer}, IT\'S A TIE')
    
    # checks choices if user choice is "paper"
    #print(f"check 3 computer {self.weapon_of_computer} you {self.weapon_of_choice}")
    if self.weapon_of_choice == "paper" and self.weapon_of_computer == "rock":
       print(f' Your {self.weapon_of_choice} beats {self.weapon_of_computer}, YOU WIN')
    elif self.weapon_of_choice == "paper" and self.weapon_of_computer == "sissors":
        print(f' Your {self.weapon_of_choice} is beaten by  {self.weapon_of_computer}, YOU LOSE')
    else:
        if self.weapon_of_choice == "paper" and self.weapon_of_computer == "paper":
            print(f' Your {self.weapon_of_choice} is the same as  {self.weapon_of_computer}, IT\'S A TIE')

def play():
    weapon_list = ["rock","paper","sissors"]
    weapon_of_choice = str()
    weapon_of_computer = str()
    game = man_rps()

    get_computer_choice(game, weapon_list)
    #print(f'computer {weapon_of_computer}')

    get_user_choice(game, weapon_list)
    #print(f'computer {weapon_of_choice}')

    get_winner(game, weapon_of_choice, weapon_of_computer)

play()