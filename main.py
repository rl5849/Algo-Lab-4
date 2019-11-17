#Algo HW 4
#Robert Liedka, Bryan Quinn, Brendan Jones
import sys
M = 90 ## Max number of chars per line


#If a given line contains words i through j and leave exactly one space between words
# the number of extra space chars at the eol is: M - j + i - sum(j, k=i)lk
def DoPrettyPrint(fromFile, toFile):
    return 0



if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print("Invalid number of args provided, please provide, read file & write file")
    else:
        DoPrettyPrint(sys.argv[1], sys.argv[2])