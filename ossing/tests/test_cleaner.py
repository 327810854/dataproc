import unittest
from ossing.cleaner import TextCleaner

class TestTextCleaner(unittest.TestCase):
    
    def setUp(self):
        self.cleaner = TextCleaner()
    
    def test_lowercase(self):
        text = "Hello WORLD"
        result = self.cleaner.clean(text)
        self.assertEqual(result, "hello world")
    
    def test_remove_punctuation(self):
        text = "Hello, world! 안녕하세요。"
        result = self.cleaner.clean(text)
        self.assertEqual(result, "hello world 안녕하세요")
    
    def test_remove_extra_spaces(self):
        text = "  hello   world  "
        result = self.cleaner.clean(text)
        self.assertEqual(result, "hello world")
    
    def test_batch_clean(self):
        texts = ["  HELLO  ", "WORLD!!!"]
        results = self.cleaner.batch_clean(texts)
        self.assertEqual(results, ["hello", "world"])
    
    def test_remove_numbers(self):
        cleaner = TextCleaner(remove_numbers=True)
        text = "hello 123 world"
        result = cleaner.clean(text)
        self.assertEqual(result, "hello world")

if __name__ == '__main__':
    unittest.main()
