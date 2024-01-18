import os, sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 

# Add the project root directory to the system path
sys.path.append(ROOT_DIR)

DATASET_DIR = os.path.join(ROOT_DIR, 'resources/dataset/')
SRC_DIR = os.path.join(ROOT_DIR, 'src/')
IMG_DIR = os.path.join(ROOT_DIR, 'resources/images/')

# print(SRC_DIR, DATASET_DIR)
