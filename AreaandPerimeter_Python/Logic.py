import math

class Calc():
    def areaofSquare(length):
        if length < 0:
            return -1
        return length * length

    def perimeterofSquare(length):
        if length < 0:
            return -1
        return 4 * length