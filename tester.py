#!/usr/bin/python3

##function to write a list to file
def writer_to_file(arg):
    writer_list = arg
    for item in writer_list: 
        f.write("%s," % item)
    f.write("\n")

##function that checks whether the user entered the correct input for file opening
def file_checker(fName, switch):
    checker = False
    if(switch == "1"):
        file = open(fName, "w")
        checker = True
    elif(switch == "2"):
        file = open(fName, "a")
        checker = True
    else:
        print("Enter a valid input")
        switch2 = input()
        file_checker(fName, switch2)
    return file

##Main Method
def main():
    print("Would you like to enter data to a new file(1) or an existing file(2)")
    switcher = input()
    print("Enter a file name for writing")
    fileName = input()

    checkedFile = file_checker(fileName, switcher)
            
    print("How many fields for data?")
    fields = input()
    fieldNum = int(fields)
    fields_list = []
    for i in fields_list:
        
        print("Enter Field Name:")
        field_name = input()
        fields_list.append(field_name)
        
        if(switcher == "1"):  
            file.write(field_name)
            file.write(",")

    information_list = []
    print("Enter Q for any value to quit")
    for i in fields_list:
        if(i < fieldNum):
            
            print("Enter the " + fields_list[i] + " followed by a comma.")
            information_list.append(input())
            
            if(information_list[i] == 'q' or information_list[i] == 'Q'):
                break
            
            writer_to_file(information_list)
            
        else:
            print("Enter the " + fields_list[i])
            information_list.append(input())
            if(information_list[i] == 'q' or information_list[i] == 'Q'):
                break
            writer_to_file(information_list)
##    print("Enter q (Q) for last weight to exit\n")
##    while(endflag == False):
##        print("Enter the" , followed by a comma\n")
##        idNum = input()
##        print("Enter the fresh weight, followed by a comma\n")
##        fweight = input()
##        print("Enter the dry weight, or Q to quit\n")
##        dweight = input()
##        if(dweight == "q" or dweight == "Q"):
##            endflag = True
##            break
##        else:
##            information = idNum + fweight + dweight
##            file.write(information)
##            file.write("\n")
    file.close()
        



##RUN MAIN
if __name__ == "__main__":
    main()
