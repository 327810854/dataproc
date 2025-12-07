import unittest
from ossing.tokenizer import Tokenizer

class TestTokenizer(unittest.TestCase):
    
    def setUp(self):
        self.tokenizer = Tokenizer()
    
    def test_tokenize_basic(self):
        text = "오늘 날씨가 정말 좋습니다"
        tokens = self.tokenizer.tokenize(text, remove_stopwords=False)
        self.assertGreater(len(tokens), 0)
        self.assertIn('오늘', tokens)
    
    def test_tokenize_remove_stopwords(self):
        text = "이것은 테스트 문장입니다"
        tokens_with_stop = self.tokenizer.tokenize(text, remove_stopwords=False)
        tokens_without_stop = self.tokenizer.tokenize(text, remove_stopwords=True)
        self.assertGreaterEqual(len(tokens_with_stop), len(tokens_without_stop))
    
    def test_word_frequency(self):
        text = "좋은 날씨 정말 좋은 하루"
        freq = self.tokenizer.get_word_frequency(text, remove_stopwords=True)
        self.assertGreater(len(freq), 0)
    
    def test_top_n_frequency(self):
        text = "좋은 날씨 정말 좋은 하루 좋은 시간"
        freq = self.tokenizer.get_word_frequency(text, remove_stopwords=True, top_n=2)
        self.assertEqual(len(freq), 2)
    
    def test_vocabulary_size(self):
        text = "좋은 날씨 정말 좋은 하루"
        vocab_size = self.tokenizer.get_vocabulary_size(text, remove_stopwords=True)
        self.assertGreater(vocab_size, 0)
    
    def test_batch_tokenize(self):
        texts = ["좋은 날씨입니다", "행복한 하루입니다"]
        results = self.tokenizer.batch_tokenize(texts)
        self.assertEqual(len(results), 2)

if __name__ == '__main__':
    unittest.main()
