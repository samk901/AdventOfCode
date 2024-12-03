import sys
import os

# Go up two levels to reach the 2024 directory
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

# Now you can import utils
from utils.file_utils import FileUtils

def main():
    global lines 
    lines = FileUtils.read_file_as_lines(f"{project_root}/input/Day2_Test")

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
    error_count = 0 
    for i in range(len(num_list)):
        if ((i > 0 and num_list[i] < num_list[i - 1]) or (i > 0 and num_list[i] == num_list[i - 1])):
            error_count += 1
            print(f"Number list {num_list} is invalid not increasing at index {i} and index {i-1}")
            return False, error_count
    return True, error_count

def validate_decreasing(num_list):
    error_count = 0 
    for i in range(len(num_list)):
        if ((i > 0 and num_list[i] > num_list[i - 1]) or (i > 0 and num_list[i] == num_list[i - 1])):
            error_count += 1
            print(f"Number list {num_list} is invalid not decreasing  at index {i} and index {i-1}")
            return False, error_count
    return True, error_count

def validate_intervals(num_list):
    error_count = 0 
    for i in range(len(num_list)):
        if i > 0 and abs(num_list[i] - num_list[i - 1]) > 3:
            print(f"Number list {num_list} is invalid not valid intervals  at index {i} and index {i-1}")
            error_count += 1
            return False, error_count
    return True, error_count

def convert_list_to_int_list(num_list):
    result_list = []
    for num in num_list:
        result_list.append(int(num))
    
    return result_list

def PartB():
    result = 0
    global error
    for line in lines:
        error = 0
        count = []
        char_list = line.split()
        num_list = convert_list_to_int_list(char_list)
    
        decrease_result, d_count = validate_decreasing(num_list)
        increase_result, i_count = validate_increasing(num_list)
        interval_result, interval_count = validate_intervals(num_list)

        count.append(decrease_result)
        count.append(increase_result)
        count.append(interval_result)
        
        print(f"decrease result is {decrease_result} with count {d_count}")
        print(f"increase result is {increase_result} with count {i_count}")
        print(f"interval result is {interval_result} with count {interval_count}")

        print(count)

        if (min(d_count, i_count) + interval_count < 2 and (d_count < 2 or i_count < 2)):
            print(f"adding to result for line {num_list}")
            result += 1
    
    print("++++++++++++++++++++++++++++++++++++")
    print(f"PART B: The result is {result}")
    print("++++++++++++++++++++++++++++++++++++")




if __name__ == "__main__":
    main()