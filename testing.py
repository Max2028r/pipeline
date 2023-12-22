def sum_of_arithmetic_progression(a_1, d, n):
    sum_n = (n / 2) * (2 * a_1 + (n - 1) * d)
    return sum_n



def test_sum_of_arithmetic_progression():
   
    assert sum_of_arithmetic_progression(1, 2, 5) == 35

   
    assert sum_of_arithmetic_progression(5, 3, 7) == 119

   
    assert sum_of_arithmetic_progression(0, 1, 10) == 45

   
    assert sum_of_arithmetic_progression(100, 0, 3) == 300





test_sum_of_arithmetic_progression()
