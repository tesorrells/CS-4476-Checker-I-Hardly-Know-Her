from detectBoard import detectBoard
from detectCircles import detectCirclesImages
import cv2
import argparse
import sys
import os.path
import imutils
import matplotlib.pyplot as plt


# FILE INPUT AND VALIDATION FOR ORIGINAL IMAGE
# Check if file passed in command line by user is valid
def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist. Try again." % arg)
    else:
        return arg

# Construct the argument parse and parse the argumentsa
parser = argparse.ArgumentParser()
requiredNamed = parser.add_argument_group('required arguments')
requiredNamed.add_argument("-i", "--image", required = True, help = "path to the image file like checkers/board1/IMG_4073.JPG", type = lambda x: is_valid_file(parser, x))
args = vars(parser.parse_args(args=None if sys.argv[1:] else ['--help']))

# Open input image with board
image = cv2.imread(args["image"])

# Detect board in input image and obtain bird's eye view of it
normalized_board = detectBoard(image)
# cv2.imshow("Original Board", imutils.resize(image, 500))
# cv2.imshow("Warped Board", normalized_board)
# cv2.waitKey(0)

_, _ = detectCirclesImages(normalized_board, True, False)
