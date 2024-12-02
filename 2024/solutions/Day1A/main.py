import sys
import os

# Go up two levels to reach the 2024 directory
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

# Now you can import utils
from utils.file_utils import FileUtils

def main():

    global lines 
    lines = FileUtils.read_file_as_lines("/home/sam/Desktop/AdventOfCode/2024/input/Day1_Test")

    PartA()
    PartB()

def PartA():  
    list1 = []
    list2 = []
    total = 0

    for line in lines:
        values = line.split("   ")
        list1.append(values[0])
        # print(str(line[0]))
        list2.append(values[1])
        # print(str(line[1]))

    list1.sort()
    list2.sort()

    # print(list1)
    # print(list2)

    for i in range(len(list1)):
        diff = abs(int(list1[i]) - int(list2[i]))
        # print(f"The diff between {list1[i]} and {list2[i]} is {diff}")
        total += diff

        i += 1
    print("++++++++++++++++++++++++++++++++++++")
    print(f"PART A: The answer is {total}")
    print("++++++++++++++++++++++++++++++++++++")

def PartB():

    # Need to count the number of instances in order to process
    # Use a hashmap (dict) of value : occurences
    count_map1 = {}
    count_map2 = {}

    total = 0

    for line in lines:
        values = line.split()
        count_map1[values[0]] = count_map1.get(values[0], 0) + 1
        count_map2[values[1]] = count_map2.get(values[1], 0) + 1

    for key, val in count_map1.items():
        # print(f"key: {key} value: {val}")
        if key in count_map2.keys():
            print(f"the value {key} is in both maps")
            common = min(count_map1[key], count_map2[key])
            total += common * int(key)  

    print("++++++++++++++++++++++++++++++++++++")
    print(f"PART B: The total is {total}")
    print("++++++++++++++++++++++++++++++++++++")
      

if __name__ == "__main__":
    main()