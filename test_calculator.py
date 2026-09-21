
# test_calculator.py 
import unittest 
from calculator import Calculator 
 
class TestCalculator(unittest.TestCase): 
    def setUp(self): 
        self.calc = Calculator() 
     
    def test_add(self): 
        self.assertEqual(self.calc.add(2, 3), 5) 
     
    def test_subtract(self): 
        self.assertEqual(self.calc.subtract(5, 3), 2) 
     
    def test_multiply(self): 
        self.assertEqual(self.calc.multiply(2, 3), 6) 
     
    def test_divide(self): 
        self.assertEqual(self.calc.divide(6, 3), 2) 
     
    def test_divide_by_zero(self): 
        self.assertEqual(self.calc.divide(5, 0), "Error: Division by zero") 

    def test_mod(self): 
        self.assertEqual(self.calc.mod(10, 3), 1) 
        self.assertEqual(self.calc.mod(10, 5), 0) 

    def test_mod_by_zero(self): 
        self.assertEqual(self.calc.mod(5, 0), "Error: Division by zero") 
 
if __name__ == '__main__': 
    unittest.main()