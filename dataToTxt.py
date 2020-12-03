#!/usr/bin/python3

##Main Method
def main():
    print("Would you like to enter data to a new file(1) or an existing file(2)\n")
    switcher = input()
    print("Enter a file name for writing\n")
    fileName = input()

    checker = False
    while(checker == False):
        if(switcher == "1"):
            file = open(fileName, "w")
            checker = True
        elif(switcher == "2"):
            file = open(fileName, "a")
            checker = True
        else:
            print("Enter a valid input\n")
            checker = input()

    
    endflag = False
    print("Enter q (Q) for last weight to exit\n")
    while(endflag == False):
        print("Enter the ID followed by a comma\n")
        idNum = input()
        print("Enter the fresh weight, followed by a comma\n")
        fweight = input()
        print("Enter the dry weight, or Q to quit\n")
        dweight = input()
        if(dweight == "q" or dweight == "Q"):
            endflag = True
            break
        else:
            information = idNum + fweight + dweight
            file.write(information)
            file.write("\n")
    file.close()
        



##RUN MAIN
if __name__ == "__main__":
    main()
