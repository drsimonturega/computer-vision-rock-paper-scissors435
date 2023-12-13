import random
import cv2
from keras.models import load_model
import numpy as np
import time

class man_rps():

    def __init__(self):
        """Inintailises the class varibles bound to an instance of the class"""
        weapon_list = ["rock","paper","sissors","nothing"]
        self.weapon_list = weapon_list
        weapon_of_choice = str()
        weapon_of_computer = str()
        self.weapon_of_computer = weapon_of_computer
        self.weapon_of_choice = weapon_of_choice
        self.computer_wins = 0
        self.user_wins = 0
       



def get_computer_choice(self, weapon_list):
    """
    Selects the computers weapon from the list weapon_list using the random.choice() method
    
    Keyword arguments:
    weapon_list -- list of weapons used in the game

    Varibles:
    weapon_of_computer -- weapon chosen by computer
    """
    self.weapon_of_computer = random.choice(self.weapon_list)
    return self.weapon_of_computer

def get_prediction(self, weapon_list):
    """
    The get_prediction function reads the users choice of weapon from the camera using the keras_model.h5

    Keyword arguments:
    weapon_list -- list of weapons used in the game

    Varibles:
    weapon_of_choice -- weapon chosen by user
    """
    model = load_model('keras_model.h5', compile=False)
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    self.weapon_list = ["rock","paper","sissors","nothing"]
    start_time = time.time()

    while True:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        if (time.time() - start_time) >= 3 or cv2.waitKey(1) & 0xFF == ord('c'):
            prediction = np.ndarray.tolist(prediction)
            #print(prediction)
            prediction = prediction[0]
            rps_test = np.array(prediction)
            self.weapon_of_choice= self.weapon_list[np.argmax(rps_test)]
            print(f'You chose {self.weapon_of_choice}')
            break
            
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    
    return self.weapon_of_choice

def get_winner(self, weapon_of_choice, weapon_of_computer, user_wins, computer_wins):
    """
    Function that takes the user choice and computer choice to determin the winner using a serise of if-elif-else statements
    
    Keyword arguments:
    weapon_of_choice -- weapon  chosen by user
    weapon_of_computer -- weapon chosen by computer
    user_wins -- counter for number of times user has won a round of RPS
    computer_wins -- counter for number of times computer has won a round of RPS
    """
    # checks choices if user choice is "rock"
    if self.weapon_of_choice == "rock" and self.weapon_of_computer == "sissors":
        print(f' Your {self.weapon_of_choice} beats {self.weapon_of_computer}, YOU WIN')
        self.user_wins = self.user_wins + 1
    elif self.weapon_of_choice == "rock" and self.weapon_of_computer == "paper":
        print(f' Your {self.weapon_of_choice} is beaten by  {self.weapon_of_computer}, YOU LOSE')
        self.computer_wins = self.computer_wins + 1
    else:
        if self.weapon_of_choice == "rock" and self.weapon_of_computer == "rock":
            print(f' Your {self.weapon_of_choice} is the same as  {self.weapon_of_computer}, IT\'S A TIE')

    # checks choices if user choice is "sissors"        
    if self.weapon_of_choice == "sissors" and self.weapon_of_computer == "paper":
       print(f' Your {self.weapon_of_choice} beats {self.weapon_of_computer}, YOU WIN')
       self.user_wins = self.user_wins + 1
    elif self.weapon_of_choice == "sissors" and self.weapon_of_computer == "rock":
        print(f' Your {self.weapon_of_choice} is beaten by  {self.weapon_of_computer}, YOU LOSE')
        self.computer_wins = self.computer_wins + 1
    else:
        if self.weapon_of_choice == "sissors" and self.weapon_of_computer == "sissor":
            print(f' Your {self.weapon_of_choice} is the same as  {self.weapon_of_computer}, IT\'S A TIE')
    
    # checks choices if user choice is "paper"
    if self.weapon_of_choice == "paper" and self.weapon_of_computer == "rock":
       print(f' Your {self.weapon_of_choice} beats {self.weapon_of_computer}, YOU WIN')
       self.user_wins = self.user_wins + 1
    elif self.weapon_of_choice == "paper" and self.weapon_of_computer == "sissors":
        print(f' Your {self.weapon_of_choice} is beaten by  {self.weapon_of_computer}, YOU LOSE')
        self.computer_wins = self.computer_wins + 1
    else:
        if self.weapon_of_choice == "paper" and self.weapon_of_computer == "paper":
            print(f' Your {self.weapon_of_choice} is the same as  {self.weapon_of_computer}, IT\'S A TIE')
    return self.computer_wins, self.user_wins

def play():
    """
    This is the function that runs the game and determins the winner based upon three rounds of the RPS game
    
    Varibles:
    weapon_of_choice -- weapon  chosen by user
    weapon_of_computer -- weapon chosen by computer
    user_wins -- counter for number of times user has won a round of RPS
    computer_wins -- counter for number of times computer has won a round of RPS
    weapon_list -- list of weapons used in the game
    """
    weapon_list = ["rock","paper","sissors","nothing"]
    weapon_of_choice = str()
    weapon_of_computer = str()
    computer_wins = 0
    user_wins = 0
    game = man_rps()

    # game loop
    while True:
        get_computer_choice(game, weapon_list)
        #print(f'computer {game.weapon_of_computer}')

        get_prediction(game, weapon_list)
        #print(f'computer {weapon_of_choice}')
        if get_prediction == "nothing":
            continue

        get_winner(game, weapon_of_choice, weapon_of_computer, computer_wins, user_wins)
        print(f'computer {game.computer_wins}, user {game.user_wins}')

        # determination of best out of three winner
        if game.computer_wins == 3:
            print(f'you lose this game, {game.user_wins}:{game.computer_wins}')
            break 
        elif game.user_wins == 3:
            print(f'you win this game, {game.user_wins}:{game.computer_wins}')  
            break

play()