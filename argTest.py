import argparse

from img_to_mc import image



parser = argparse.ArgumentParser(description="User img-to-mc (without GUI) in command line")

# Define command ligne options
parser.add_argument('--image_width', type=int, help='In-game image width (in block)')

# Get the arguments
args = parser.parse_args()

print(args)