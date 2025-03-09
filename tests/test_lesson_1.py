import unittest
from tasks.Lesson_1 import generate_random_numbers, bubble_sort, calculate_averages


class TestLesson1(unittest.TestCase):

    def test_generate_random_numbers_length(self):
        numbers = generate_random_numbers(count=50, min_value=10, max_value=20)
        self.assertEqual(len(numbers), 50)
        self.assertTrue(all(10 <= num <= 20 for num in numbers))

    def test_bubble_sort(self):
        arr = [5, 1, 0.9999999999999999999, 0.0, 8, 4, -2]
        bubble_sort(arr)
        self.assertEqual(arr, [-2, 0, 0.9999999999999999999, 1, 4, 5, 8])

    def test_calculate_averages(self):
        arr = [5, 1, 0.9999999999999999999, 0.0, 8, 4, -2]
        avg_even, avg_odd = calculate_averages(arr)
        self.assertEqual(avg_even, 2.5)
        self.assertEqual(avg_odd, 2.33)
