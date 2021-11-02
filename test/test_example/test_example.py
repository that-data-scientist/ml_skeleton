import unittest

from src.example.run_example import Example


class TestExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.instance = Example()

    def test_example_result(self):
        self.assertEqual(self.instance.get_result(), 30)
