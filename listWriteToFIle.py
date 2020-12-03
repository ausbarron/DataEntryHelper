#!/usr/bin/python3

import sys
##MAIN
def main():
    fileName = sys.argv[1]
    writer_list = ["1","2","3"]
    f = open(fileName, "w")
    for item in writer_list:
        f.write("%s," % item)
    f.write("\n")

    f.close()


    ##RUN MAIN
if __name__ == "__main__":
    main()
    
