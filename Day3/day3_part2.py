import os

def main():
    # Using readlines()
    file1 = open('/home/komputer/programmen/AdventOfCode2022/Day3/input_2.txt', 'r')
    Lines = file1.readlines()
    line_count=0
    line_list=["","",""]
    badge_list=['']
    for line in Lines:
        # reached end of group
        if(line_count == 2):
            line_list[line_count] = str(line).strip()
            line_count = 0
            common_char = ''.join(set(str(line_list[0])).intersection(str(line_list[1])))
            for char in str(common_char):
                if(char in str(line_list[2]) and char != " "):
                    badge_list.append(char)
                    line_list = ["","",""]
                    break
                else:
                    continue
        else:
            line_list[line_count] = str(line).strip()
            line_count += 1
    priority_num = 0
    priority_sum = 0
    badge_list = ''.join(badge_list)
    for ch in badge_list:
        ch = str(ch)
        if(ch.isupper()):
            priority_num = int(ord(ch))-38
        else:
            priority_num = int(ord(ch))-96
        priority_sum+=priority_num
    print('final: '+str(priority_sum))

if __name__=="__main__":
    main()
