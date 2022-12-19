import os

def main():
    # Using readlines()
    file1 = open('/home/komputer/programmen/AdventOfCode2022/Day3/input.txt', 'r')
    Lines = file1.readlines()
    char_dict = dict()
    priority_sum = 0
    for line in Lines:
        first_half = str(line[0:int(len(line)/2)])
        second_half = str(line[int(len(line)/2):int(len(line))])
        common_char = ''.join(set(first_half).intersection(second_half))
        
        # First get the ASCII number (in order to preserve the incremental order)
        priority_num = int(ord(common_char))
        if(str(common_char).isupper()):
            # Capital A is 65 so to get to 27, subtract 38
            priority_num -= 38
        else:
            # lowercase a is 97 so to get to 1, subtract 96
            priority_num -= 96
        priority_sum += priority_num
    print(priority_sum)

if __name__=="__main__":
    main()
