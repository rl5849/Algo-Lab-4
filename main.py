#Algo HW 4
#Robert Liedka, Bryan Quinn, Brendan Jones
import sys
M = 90 ## Max number of chars per line


#If a given line contains words i through j and leave exactly one space between words
# the number of extra space chars at the eol is: M - j + i - sum(j, k=i)lk
def DoPrettyPrint(fromFileName, toFile):
    with open(fromFileName) as fromFile:
        content = fromFile.read()
    newString = ""
    charOffset=0

    while True:
        spaces = 0
        if charOffset + M < len(content):
            currentLine = content[charOffset : charOffset + M]
            while currentLine[len(currentLine) - spaces - 1] != " ": #walk back
                spaces += 1
            newString += currentLine[0:M-spaces-1] + (" " * spaces) + "\n"
            charOffset += M-spaces
        else:
            currentLine = content[charOffset:]
            spaces = M - len(currentLine)
            newString += currentLine + (" " * spaces) + "\n"
            break

    print(newString)






if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print("Invalid number of args provided, please provide, read file & write file")
    else:
        DoPrettyPrint(sys.argv[1], sys.argv[2])