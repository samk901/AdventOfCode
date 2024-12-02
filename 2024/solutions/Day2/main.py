import sys
import os

# Go up two levels to reach the 2024 directory
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

# Now you can import utils
from utils.file_utils import FileUtils

def main():
    global lines 
    lines = FileUtils.read_file_as_lines("/home/sam/Desktop/AdventOfCode/2024/input/Day2")

    PartA()
    PartB()

def PartA():
    result = 0 
    for line in lines:
        char_list = line.split()
        num_list = convert_list_to_int_list(char_list)
        
        
        if ((validate_increasing(num_list) or validate_decreasing(num_list)) 
            and validate_intervals(num_list)):
            print(f"Adding valid num list {num_list}")
            result += 1

    print("++++++++++++++++++++++++++++++++++++")
    print(f"PART A: The result is {result}")
    print("++++++++++++++++++++++++++++++++++++")

def validate_increasing(num_list):
    for i in range(len(num_list)):
        if ((i > 0 and num_list[i] < num_list[i - 1]) or (i > 0 and num_list[i] == num_list[i - 1])):
            print(f"Number list {num_list} is invalid not increasing at index {i} and index {i-1}")
            return False
    
    return True

def validate_decreasing(num_list):
    for i in range(len(num_list)):
        if ((i > 0 and num_list[i] > num_list[i - 1]) or (i > 0 and num_list[i] == num_list[i - 1])):
            print(f"Number list {num_list} is invalid not decreasing  at index {i} and index {i-1}")
            return False
    
    return True

def validate_intervals(num_list):
    for i in range(len(num_list)):
        if i > 0 and abs(num_list[i] - num_list[i - 1]) > 3:
            print(f"Number list {num_list} is invalid not valid intervals  at index {i} and index {i-1}")
            return False
    
    return True

def convert_list_to_int_list(num_list):
    result_list = []
    for num in num_list:
        result_list.append(int(num))
    
    return result_list

def PartB():
    result = 0

    print("++++++++++++++++++++++++++++++++++++")
    print(f"PART B: The result is {result}")
    print("++++++++++++++++++++++++++++++++++++")




if __name__ == "__main__":
    main()