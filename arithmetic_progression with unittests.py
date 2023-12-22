import unittest

def arithmetic_progression(a_1, d, n):
    progression = [a_1 + i * d for i in range(n)]
    return progression

class TestArithmeticProgression(unittest.TestCase):

    def test_arithmetic_progression(self):
        expected_sequence = [2, 5, 8, 11, 14]
        result = arithmetic_progression(2, 3, 5)
        self.assertEqual(result, expected_sequence)

    def test_different_progression(self):
        progression_1 = arithmetic_progression(1, 2, 5)
        progression_2 = arithmetic_progression(3, 5, 5)
        self.assertNotEqual(progression_1, progression_2)

if __name__ == '__main__':
    unittest.main()
