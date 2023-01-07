import sys
import math
from Logic import Calc
from decimal import Decimal

def DisplayValues(heading, results):
                print("-----------------------------")
                print(heading)
                print("-----------------------------")
                for result in results:
                    print(result)
def main():
    args = sys.argv[1:]
    
    try:
        if (len(args)) != 4:
           print("error: Enter 4 values")
           print("usage:Enter S, R or T for Square, Rectangle and Triangle then Enter length, bredth and height")
        
        else:
            length, bredth, height = args[2,3,4]
            logic = Calc(Decimal(length), Decimal(bredth), Decimal(height))
              
            if args[1].casefold == "s":
                DisplayValues("Area of Sqaure is:",logic.areaofSquare(length))
                DisplayValues("Perimeter of Sqaure is:",logic.perimeterofSquare(length))

            elif args[1].casefold == "t":
                DisplayValues("Area of Triangle is:",logic.areaofTriangle(length, bredth))
                DisplayValues("Perimeter of Triangle is:",logic.perimeterofTriangle(length, bredth, height))
            
            elif args[1].casefold == "r":
                DisplayValues("Area of Rectangle is:",logic.areaofRectangle(length, bredth))
                DisplayValues("Perimeter of Rectangle is:",logic.perimeterofRectangle(length, bredth))

            else:
                print("Invalid Choice")
                
    except ValueError:
        for a in args[1]:
            if (a.isalpha()) == False:
                print("Enter S, R or T for Square, Rectangle and Triangle")
        for a in args[2,3,4]:
            if not(a.isnumeric()) == False:
                print("Enter numeric values for length, bredth, height")


if __name__ == '__main__':
    main()


