#!/bin/sh

import sys

if __name__ == "__main__":

    print ("Number of arguments:", len(sys.argv), "arguments")
    print(type(sys.argv))
    print ("Argument List:", str(sys.argv))
    for argv in sys.argv:
        print(argv)
    arg1 = sys.argv[1]
    print(arg1,"!!!",type(arg1))
    #return 0
