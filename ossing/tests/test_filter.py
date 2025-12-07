import unittest
from ossing.filter import SensitiveWordFilter

class TestSensitiveWordFilter(unittest.TestCase):
    
    def setUp(self):
        self.filter = SensitiveWordFilter(replacement_char='*')
    
    def test_load_from_list(self):
        self.filter.load_from_list(['나쁜말', '욕설'])
        self.assertTrue(self.filter.has_sensitive_words('이것은 나쁜말입니다'))
    
    def test_has_sensitive_words(self):
        self.filter.load_from_list(['나쁜말'])
        self.assertTrue(self.filter.has_sensitive_words('이것은 나쁜말입니다'))
        self.assertFalse(self.filter.has_sensitive_words('이것은 좋은 말입니다'))
    
    def test_filter(self):
        self.filter.load_from_list(['나쁜말', '욕설'])
        text = "이것은 나쁜말과 욕설입니다"
        result = self.filter.filter(text)
        self.assertEqual(result, "이것은 ***과 **입니다")
    
    def test_get_sensitive_words(self):
        self.filter.load_from_list(['나쁜말', '욕설'])
        text = "이것은 나쁜말과 욕설입니다"
        result = self.filter.get_sensitive_words(text)
        self.assertEqual(set(result), {'나쁜말', '욕설'})

if __name__ == '__main__':
    unittest.main()
