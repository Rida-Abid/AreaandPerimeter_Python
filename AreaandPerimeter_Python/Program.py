import sys
import math
from Logic import Calc
from decimal import Decimal

def DisplayValues(heading, results):
                print("-----------------------------")
                print(heading)
                
                print(results)
def main():
    args = sys.argv[1:]
    
    try:
        if (len(args)) != 4:
           print("error: Enter 4 values")
           print("usage:Enter S, R or T for Square, Rectangle and Triangle then Enter length, bredth and height")
        
        else:
            shape, length, bredth, height = args
            length, bredth, height = Decimal(length), Decimal(bredth), Decimal(height)
            logic = Calc

            if (length < 0) or (bredth < 0) or (height < 0):
                print("Enter all values greater than 0")
            
            else:
                if shape.isalpha() == False:
                    print("Enter S, R or T for Square, Rectangle and Triangle")

                elif shape.casefold() == "s":
                    DisplayValues("Area of Sqaure is:",logic.areaofSquare(length))
                    DisplayValues("Perimeter of Sqaure is:",logic.perimeterofSquare(length))

                elif shape.casefold() == "t":
                    DisplayValues("Area of Triangle is:",logic.areaofTriangle(length, bredth))
                    DisplayValues("Perimeter of Triangle is:",logic.perimeterofTriangle(length, bredth, height))
            
                elif shape.casefold() == "r":
                    DisplayValues("Area of Rectangle is:",logic.areaofRectangle(length, bredth))
                    DisplayValues("Perimeter of Rectangle is:",logic.perimeterofRectangle(length, bredth))

                else:
                    print("Invalid Choice for Shape")
                
    except :
        if (length.isdecimal()) or (bredth.isdecimal()) or (height.isdecimal()) == False:
            print("Enter numeric values for length, bredth, height")


if __name__ == '__main__':
    main()


