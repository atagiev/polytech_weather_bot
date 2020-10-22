import unittest
from src.yandex_parser import Yandex_parser

class TestYandexParser(unittest.TestCase):
    def setUp(self):
        self.yandexParser = Yandex_parser()
        self.str = self.yandexParser.parse("60", "30")

    def test_StartWith(self):
        self.assertEqual(self.str.startswith('Яндекс'), True)

    def test_ContainFirstTemp(self):
        start = self.str.index('погода:')
        start += 9
        end = self.str.index('°')
        self.assertEqual(self.str[start:end].isdigit(), True)

    def test_ContainSecondTemp(self):
        start = self.str.index('ощущается')
        start += 15
        end = self.str.index('°', start, start + 10)
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