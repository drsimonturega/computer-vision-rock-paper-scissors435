# Computer Vision RPS

## Contents
* Introduction
* Milestone
* Functions
* Classes
* Running instructions

### Introduction


### Milesones

#### Milestone 1

The first milestone involeved setting up the github repo using an AiCore github bot.This mean the working environment, git hub and development folder are set up. The git hub will be used to help with version control through out the project.

#### Milestone 2

Made acess token for github and activated it using 
```
git remote set-url origin https://TOKENHERE@github.com/drsimonturega/computer-vision-rock-paper-scissors435
```
The image recogniton model was prodeuced using https://teachablemachine.withgoogle.com/ to create a model with four classes Rock, Paper, Sissor and nothing. This gave a keras_model.h5 and index.txt files for use with python code later in the project.

#### Milestone 3

Set up a conda environment com_vis_rps using the comand ```conda create -n com_vis_rps python=3.8```

The conda enviroment was activated using ```conda activate com_vis_rps``` and deactivated using ```conda deactivate```. The despendances opencv-python, tensorflow, and ipykernel. A dependancy requirements file "requirements.txt"  was made using the ```pip list > requirements.txt``` comand this can be used to install the required depandances in futhure using the ```pip install requirements.txt``` I suspect this file will need updating.

#### Milestone 4

A python script was written that selects a weapon; rock paper or sissors for the computer and weapon weapon; rock paper or sissors for the user. The winner is then dermined using three if elif else statements. The game was written as a class including a __init__ method to initialse the class varibles bound an the instance of the game.
![Alt](/classinit.png "get_computer_choice()")
A working version of the game was written that used text input to get the user choice.

#### Milestone 5
A version of the game that uses the camera to select the players choice of weapon. The game was expanded to make it best out of three rounds of RPS. It was complicated covert the out put of the model into a list that the inital verson was quite verbose but I shortend it down in code opitimisation.
```
if (time.time() - start_time) >= 3 or cv2.waitKey(1) & 0xFF == ord('c'):
            prediction = np.ndarray.tolist(prediction)
            self.weapon_of_choice= self.weapon_list[np.argmax(np.array(prediction[0]))]
            print(f'You chose {self.weapon_of_choice}')
```
The python function ```play()``` runs the game.

### Functions

Functions have been coded for user and computer input for for the RPS game these are ```get_user_choice()``` and ```get_computer_choice()```. In the ```get_user_choice()``` I made use of a while lood the gets exited with a break statment, this is something I struggled with when it was first suggested but now it looks rather neat.

![Alt](/woc_001.png "get_computer_choice()")

The ```get_prediction()``` replaced the ```get_user_choice()``` in the camera version of the game. The function get_winner() was written to determin the winner using the computer choice and the player choice. This function also conatined varibles that help calculate the best out of three winner.


### Running instructions
python3 camera_rps.py
