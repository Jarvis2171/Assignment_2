
import unittest
from math_operations import MathOperations

class TestMathIntegration(unittest.TestCase):

    def test_addition_and_subtraction(self):

        math_ops = MathOperations()


        result_add = math_ops.add(5, 3)
        result_subtract = math_ops.subtract(9, 4)


        self.assertEqual(result_add, 8, "Addition failed")
        self.assertEqual(result_subtract, 4, "Subtraction failed")

    def test_multiply_and_divide(self):

        math_ops = MathOperations()


        result_multiply = math_ops.multiply(3, 4)
        result_divide = math_ops.divide(8, 2)

        # Assert
        self.assertEqual(result_multiply, 12, "Multiplication failed")
        self.assertEqual(result_divide, 4, "Division failed")

    def test_divide_by_zero(self):

        math_ops = MathOperations()


        with self.assertRaises(ValueError):
            math_ops.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
