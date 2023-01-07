import sys
import math

def main():
    args = sys.argv[1:]
    
    try:
        if (len(args)) != 4:
           print("error: Enter 3 values")
           print("usage:Enter S, R or T for Square, Rectangle and Triangle then Enter length, bredth and height")
        
        else:
            length, bredth, height = args
            results = logic.process(double(length), double(bredth), double(height))
            def DisplayValues(heading, results):


                print()
    except ValueError:
        for a in args[1]:
            if (a.isalpha()) == False:
                print("Enter S, R or T for Square, Rectangle and Triangle")
        for a in args[2,3,4]:
            if not(a.isnumeric()) == False:
                print("Enter numeric values for length, bredth, height")
