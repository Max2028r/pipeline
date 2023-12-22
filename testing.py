import unittest

def sum_of_arithmetic_progression(a_1, d, n):
    sum_n = (n / 2) * (2 * a_1 + (n - 1) * d)
    return sum_n

class TestSumOfArithmeticProgression(unittest.TestCase):

    def test_sum_of_arithmetic_progression(self):
        self.assertEqual(sum_of_arithmetic_progression(5, 3, 7), 98) 
        self.assertEqual(sum_of_arithmetic_progression(0, 1, 10), 45)  
        self.assertEqual(sum_of_arithmetic_progression(100, 0, 3), 150) 
        self.assertEqual(sum_of_arithmetic_progression(1, 2, 5), 35)  

if __name__ == '__main__':
    unittest.main()
