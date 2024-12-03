import sys
import os

# Go up two levels to reach the 2024 directory
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

# Now you can import utils
from utils.file_utils import FileUtils

def main():

    global lines 
    lines = FileUtils.read_file_as_lines(f"{project_root}/input/Day1")

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
    
    list1 = []
    list2 = []
    list2_count ={}
    total = 0

    for line in lines:
        values = line.split("   ")
        list1.append(values[0])
        # print(str(line[0]))
        list2.append(values[1])
        # print(str(line[1]))

        if not (values[1] in list2_count):
            list2_count[values[1]] = 1
        else:
            list2_count[values[1]] += 1
    
    for num in list1:
        if num in list2:
            total += int(num) * list2_count[num]
    
    print("++++++++++++++++++++++++++++++++++++")
    print(f"PART B: The total is {total}")
    print("++++++++++++++++++++++++++++++++++++")
      

if __name__ == "__main__":
    main()