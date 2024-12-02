import sys
import os

# Go up two levels to reach the 2024 directory
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

# Now you can import utils
from utils.file_utils import FileUtils

def main():
    global lines 
    lines = FileUtils.read_file_as_lines("/home/sam/Desktop/AdventOfCode/2024/input/Day1")

    print(lines)
    PartA()
    PartB()

def PartA():
    result = 0 

    print("++++++++++++++++++++++++++++++++++++")
    print(f"PART A: The result is {result}")
    print("++++++++++++++++++++++++++++++++++++")


def PartB():
    result = 0

    print("++++++++++++++++++++++++++++++++++++")
    print(f"PART B: The result is {result}")
    print("++++++++++++++++++++++++++++++++++++")




if __name__ == "__main__":
    main()