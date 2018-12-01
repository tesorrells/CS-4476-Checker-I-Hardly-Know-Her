# CHECKER? I HARDLY KNOW HER!

## Description
The purpose of this project is to apply image processing and computer vision techniques to checkers. The goal is to allow a user to input an image of a checkers board at any point in a game, process the location and color of pieces on the board, and then use an AI model to predict the next move. This project was completed for CS 4476: Computer Vision (Fall 2018) at Georgia Tech. 

## Run
In order to process an image, run the following command:
	python3 NextMove.py -i path/to/image
This will process the image in the background and show two images: a 500x500 representation of the original board state and a 500x500 representation of the best move applied. The best move will also be printed to the command line.

## Install
The following libraries should be installed before running:
* graphics (pip3 install --user http://bit.ly/csc161graphics)
* numpy (pip3 install numpy)
* matplotlib (pip3 install matplotlib)
* opencv (pip3 install opencv-python)
* imutils (pip3 install imutils)
