import os

def main():
    # Using readlines()
    file1 = open('/home/ludakoreo182/programmen/advent/AdventOfCode2022/Day2/input.txt', 'r')
    Lines = file1.readlines()
    running_total = 0
    line_count = 0 
    for line in Lines:
        elf_play = str(line[0:1]).strip()
        user_play = str(line[2:3]).strip()

        # portion 1 of score (results of match):
        running_total = int(running_total) + match_results(elf_play, user_play)
        print("Running total now: "+str(running_total))
        #portion 2 of score (user choice):
        running_total = int(running_total) + int(user_choice(user_play))
        
        print("Running total now: "+str(running_total))
        #portion 2 of score (user choice):
        print("Score for this round: "+str(running_total))
    
    print("Final score is: "+str(running_total))

def match_results(opp_play,your_play):
    # The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
    if(your_play=="X"):
        if(opp_play=="A"):
            return int(3)
        if(opp_play=="B"):
            return int(0)
        if(opp_play=="C"):
            return int(6)
    if(your_play=="Y"):
        if(opp_play=="A"):
            return int(6)
        if(opp_play=="B"):
            return int(3)
        if(opp_play=="C"):
            return int(0)
    if(your_play=="Z"):
        if(opp_play=="A"):
            return int(0)
        if(opp_play=="B"):
            return int(6)
        if(opp_play=="C"):
            return int(3)

def user_choice(your_play):
    if(your_play=="X"): return int(1)
    elif(your_play=="Y"): return int(2)
    elif(your_play=="Z"):return int(3)
    else: return int(0)

if __name__=="__main__":
    main()
