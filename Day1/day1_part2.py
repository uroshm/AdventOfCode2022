import os

def main():
    # Using readlines()
    file1 = open('/home/ludakoreo182/programmen/advent/AdventOfCode2022/Day1/input', 'r')
    Lines = file1.readlines()

    running_total = 0
    current_max_list = [0,0,0]
    
    for line in Lines:
        # if we get to a newline, i.e. end of a single Elf's count, evaluate if we have a new max:
        if(line=="\n"):
            current_max_list = updateList(running_total, current_max_list)
            running_total = 0
            continue
        else:
            running_total += int(line)
    grand_total = 0
    for value in current_max_list:
        grand_total += value
    print("Grand total is: "+str(grand_total))

def updateList(new_value, current_max_list):
    current_max_list.sort()
    for i in range(len(current_max_list)):
        if(int(new_value) > int(current_max_list[i])):
            current_max_list[i] = int(new_value)
            break
    return current_max_list        
    
if __name__=="__main__":
    main()