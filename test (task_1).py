import unittest
import task_1

class TestMain(unittest.TestCase):
    def test_first(self):
        test_param_1 = 512
        result = task_1.reverse_number(test_param_1)
        self.assertEqual(result, 215)

    def test_second(self):
        test_param_2 = -415
        result = task_1.reverse_number(test_param_2)
        self.assertEqual(result, -514)

    def test_third(self):
        test_param_3 = 5241.234
        with self.assertRaises(AssertionError):
            task_1.reverse_number(test_param_3)

    def test_fourth(self):
        test_param_4 = 'dsgsdgs'
        with self.assertRaises(ValueError):
            task_1.reverse_number(test_param_4)


unittest.main()
