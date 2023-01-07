from ast import main
import unittest
import Program
from Logic import Calc

class Test_Program(unittest.TestCase):
    
    #region Square
    def test_DefaultParametersinAreaofSquare(self):
        result = Calc.areaofSquare(self, 12.2)
        self.assertIsNotNone(result)
        self.assertEqual(result, 148.83999999999997)

    def test_DefaultParametersinPerimeterofSquare(self):
        result = Calc.perimeterofSquare(self, 12.2)
        self.assertIsNotNone(result)
        self.assertEqual(result, 48.8)

    #endregion
    
    #region Triangle
    def test_DefaultParametersinAreaofTriangle(self):
        result = Calc.areaofTriangle(self, 12.2, 13.3)
        self.assertIsNotNone(result)
        self.assertEqual(result, 81.13)

    def test_DefaultParametersinPerimeterofTriangle(self):
        result = Calc.perimeterofTriangle(self, 12.2, 13.3, 14.4)
        self.assertIsNotNone(result)
        self.assertEqual(result, 39.9)
    #endregion

     #region Rectangle
    def test_DefaultParametersinAreaofRectangle(self):
        result = Calc.areaofRectangle(self, 12.2, 13.3)
        self.assertIsNotNone(result)
        self.assertEqual(result, 162.26)

    def test_DefaultParametersinPerimeterofRectangle(self):
        result = Calc.perimeterofRectangle(self, 12.2, 13.3)
        self.assertIsNotNone(result)
        self.assertEqual(result, 324.52)
    #endregion
if __name__ == '__main__':
    unittest.main()
