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

### Functions

Functions have been coded for user and computer input for for the RPS game these are ```get_user_choice()``` and ```get_computer_choice()```. In the ```get_user_choice()``` I made use of a while lood the gets exited with a break statment, this is something I struggled with when it was first suggested but now it looks rather neat.

### Classes

#### Teachable machine

##### Rock

##### Paper

##### Sissor

##### Nothing


### Running instructions
