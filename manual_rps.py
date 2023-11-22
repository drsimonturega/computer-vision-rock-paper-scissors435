import random
weapon_list = ["rock","paper","sissors"]
def get_computer_choice():
    weapon_of_computer = random.choice(weapon_list)
    #print(f'Computer chosse {weapon_of_computer}')
    return weapon_of_computer

def get_user_choice():
    while True:
        weapon_of_choice = input('Choose rock, paper or sissors, ')
        weapon_of_choice = weapon_of_choice.lower()
        if weapon_of_choice in weapon_list:
            break
        else:
            print('Try again!')
            continue
    return weapon_of_choice

get_computer_choice()
get_user_choice()