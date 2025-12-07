import os
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_PKG = os.path.join(_ROOT, "ossing")
for _p in (_ROOT, _PKG):
    if _p not in sys.path:
        sys.path.insert(0, _p)


from ossing import TextCleaner, SensitiveWordFilter, Tokenizer

def example_cleaner():
    """텍스트 정리 예시"""
    print("=" * 50)
    print("1. 텍스트 정리 예시")
    print("=" * 50)
    
    cleaner = TextCleaner(
        lowercase=True,
        remove_punctuation=True,
        remove_numbers=False,
        remove_extra_spaces=True
    )
    
    raw_text = "  안녕 세계!!!  이것은   테스트 문본입니다。"
    cleaned = cleaner.clean(raw_text)
    
    print(f"원본: {repr(raw_text)}")
    print(f"정리됨: {repr(cleaned)}")
    print()

def example_filter():
    """민감한 단어 필터링 예시"""
    print("=" * 50)
    print("2. 민감한 단어 필터링 예시")
    print("=" * 50)
    
    filter_obj = SensitiveWordFilter(replacement_char='*')
    filter_obj.load_from_list(['욕설', '부적절한', 'badword'])
    
    text = "이것은 욕설과 부적절한 내용입니다, badword도 있습니다"
    
    print(f"원본: {text}")
    print(f"민감한 단어 포함: {filter_obj.has_sensitive_words(text)}")
    print(f"민감한 단어 목록: {filter_obj.get_sensitive_words(text)}")
    print(f"필터링됨: {filter_obj.filter(text)}")
    print()

def example_tokenizer():
    """토크나이징 및 단어 빈도 통계 예시"""
    print("=" * 50)
    print("3. 토크나이징 및 단어 빈도 통계 예시")
    print("=" * 50)
    
    tokenizer = Tokenizer()
    
    text = "오늘 날씨가 정말 좋습니다. 공원에 가서 놀겠습니다. 정말 좋은 날씨입니다."
    
    print(f"원본: {text}")
    
    # 토크나이징 (불용어 제거 안 함)
    tokens_with_stop = tokenizer.tokenize(text, remove_stopwords=False)
    print(f"토크나이징 (불용어 포함): {tokens_with_stop}")
    
    # 토크나이징 (불용어 제거)
    tokens = tokenizer.tokenize(text, remove_stopwords=True)
    print(f"토크나이징 (불용어 제거): {tokens}")
    
    # 단어 빈도 통계
    freq = tokenizer.get_word_frequency(text, remove_stopwords=True, top_n=5)
    print(f"단어 빈도 (상위 5개): {freq}")
    
    # 어휘량
    vocab_size = tokenizer.get_vocabulary_size(text, remove_stopwords=True)
    print(f"어휘량: {vocab_size}")
    print()

def example_pipeline():
    """완전한 처리 파이프라인 예시"""
    print("=" * 50)
    print("4. 완전한 처리 파이프라인 예시")
    print("=" * 50)
    
    # 1단계: 텍스트 정리
    cleaner = TextCleaner(lowercase=True, remove_punctuation=True)
    raw_text = "  사용자: 안녕 세계!!!  이것은   테스트입니다。"
    cleaned = cleaner.clean(raw_text)
    
    # 2단계: 민감한 단어 필터링
    filter_obj = SensitiveWordFilter()
    filter_obj.load_from_list(['테스트'])
    filtered = filter_obj.filter(cleaned)
    
    # 3단계: 토크나이징 및 통계
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(filtered, remove_stopwords=True)
    freq = tokenizer.get_word_frequency(filtered, remove_stopwords=True)
    
    print(f"원본: {raw_text}")
    print(f"정리: {cleaned}")
    print(f"필터링: {filtered}")
    print(f"토크나이징: {tokens}")
    print(f"단어 빈도: {freq}")
    print()

if __name__ == '__main__':
    example_cleaner()
    example_filter()
    example_tokenizer()
    example_pipeline()
