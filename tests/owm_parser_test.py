import unittest
from src.owm_parser import Owm_parser


class TestOwmParser(unittest.TestCase):
    def setUp(self):
        self.owmParser = Owm_parser()
        self.str = self.owmParser.parse("51", "0")

    def test_StartWith(self):
        self.assertEqual(self.str.startswith('OpenWeatherMap'), True)

    def test_ContainFirstTemp(self):
        start = 16
        end = self.str.index('°')
        end -= 3
        self.assertEqual(self.str[start:end].isdigit(), True)

    def test_ContainSecondTemp(self):
        start = self.str.index('ощущается')
        start += 14
        end = self.str.index('°', start, start + 10)
        end -= 3
        self.assertEqual(self.str[start:end].isdigit(), True)

    def test_ContainWind(self):
        self.assertEqual('ветер' in self.str, True)

    def test_WindSpeed(self):
        start = self.str.index('ветер')
        start += 7
        end = -9
        self.assertEqual(self.str[start:end].isdigit(), True)


if __name__ == "__main__":
    unittest.main()
