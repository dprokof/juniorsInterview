import unittest

from task1.solution import sum_two


class TestStrict(unittest.TestCase):

    def test_with_correct_types(self) -> None:
        result = sum_two(1, 2)
        self.assertEqual(result, 3)


    def test_with_incorrect_types(self) -> None:
        with self.assertRaises(TypeError):
            sum_two(1, 2.4)