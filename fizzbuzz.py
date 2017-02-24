import sys

# Sample input
'''
3 5 10
2 7 15
'''

with open("data.txt", 'r') as test_cases:
    data = [x.strip() for x in test_cases.readlines()]
    content = data

    for line in data:
        # splitting file data AND casting data from file to integer
        t = [int(x.strip()) for x in line.split(' ')]
        final = ""

        for x in range(1, t[2] + 1):
            if ((x % t[0]) == 0 and (x % t[1]) == 0):
                final += "FB "
            elif ((x % t[0]) == 0):
                final += "F "
            elif ((x % t[1]) == 0):
                final += "B "
            else:
                final += str(x) + " "
        final.strip() #removing trailing spaces
        print(final)

# Output
#1 2 F 4 B F 7 8 F B
#1 F 3 F 5 F B F 9 F 11 F 13 FB 15


