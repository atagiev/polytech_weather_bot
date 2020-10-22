import unittest
from src.yr_parser import Yr_parser


class TestYrParser(unittest.TestCase):
    def setUp(self):
        self.yrParser = Yr_parser()
        self.str = self.yrParser.parse("60", "30")

    def test_StartWith(self):
        self.assertEqual(self.str.startswith('Yr'), True)

    def test_ContainFirstTemp(self):
        start = 4
        end = self.str.index('°')
        end -= 2
        self.assertEqual(self.str[start:end].isdigit(), True)

    def test_ContainRainfall(self):
        start = self.str.index('ожидается')
        start += 10
        end = self.str.index('мм', start, start + 10)
        end -= 3
        self.assertEqual(self.str[start:end].isdigit(), True)

    def test_ContainWind(self):
        self.assertEqual('ветер' in self.str, True)

    def test_WindSpeed(self):
        start = self.str.index('ветер')
        start += 7
        end = -8
        self.assertEqual(self.str[start:end].isdigit(), True)


if __name__ == "__main__":
    unittest.main()
