import unittest
import tasks.Lesson_1

class TestLesson1(unittest.TestCase):

    def test_generate_random_numbers_length(self):
        numbers = tasks.Lesson_1.generate_random_numbers(count=50, min_value=10, max_value=20)
        self.assertEqual(len(numbers), 50)
        self.assertTrue(all(10 <= num <= 20 for num in numbers))

    def test_bubble_sort(self):
        arr = [5, 1, 0.9999999999999999999, 0.0, 8, 4, -2]
        tasks.Lesson_1.bubble_sort(arr)
        self.assertEqual(arr, [-2, 0, 0.9999999999999999999, 1, 4, 5, 8])