import os

def main():
    # Using readlines()
    file1 = open('/home/ludakoreo182/programmen/advent/AdventOfCode2022/Day1/input', 'r')
    Lines = file1.readlines()

    running_total = 0
    current_max = 0
    
    for line in Lines:
        # if we get to a newline, i.e. end of a single Elf's count, evaluate if we have a new max:
        if(line=="\n"):
            if(running_total > current_max): current_max = running_total
            running_total = 0
            continue
        else:
            running_total += int(line)
    print("Maximum is: "+str(current_max))

if __name__=="__main__":
    main()