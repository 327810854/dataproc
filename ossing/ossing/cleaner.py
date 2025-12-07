import re
import string
import unicodedata

class TextCleaner:
    """
    텍스트 정리 및 정규화 도구 클래스
    
    기능:
    - 소문자 변환
    - 불필요한 공백 제거
    - 구두점 제거
    - Unicode 정규화
    - 특수 문자 및 숫자 제거
    """
    
    def __init__(self, lowercase=True, remove_punctuation=True, 
                 remove_numbers=False, remove_extra_spaces=True):
        """
        정리기 초기화
        
        Args:
            lowercase: 소문자로 변환할지 여부
            remove_punctuation: 구두점 제거할지 여부
            remove_numbers: 숫자 제거할지 여부
            remove_extra_spaces: 불필요한 공백 제거할지 여부
        """
        self.lowercase = lowercase
        self.remove_punctuation = remove_punctuation
        self.remove_numbers = remove_numbers
        self.remove_extra_spaces = remove_extra_spaces
    
    def clean(self, text):
        """
        정리 작업 실행
        
        Args:
            text: 입력 텍스트
        
        Returns:
            정리된 텍스트
        """
        if not isinstance(text, str):
            return ""
        
        # 1. Unicode 정규화 (한글 및 기타 문자 처리)
        text = unicodedata.normalize('NFKC', text)
        
        # 2. 소문자로 변환
        if self.lowercase:
            text = text.lower()
        
        # 3. 숫자 제거 (필요시)
        if self.remove_numbers:
            text = re.sub(r'\d+', '', text)
        
        # 4. 구두점 제거 (필요시)
        if self.remove_punctuation:
            # 영문 및 한글 구두점 모두 제거
            punct = string.punctuation + "，。！？；：‘’“”【】（）、…·"
            text = ''.join(c for c in text if c not in punct)
        
        # 5. 불필요한 공백 제거
        if self.remove_extra_spaces:
            text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def batch_clean(self, texts):
        """
        텍스트 목록 일괄 정리
        
        Args:
            texts: 텍스트 목록
        
        Returns:
            정리된 텍스트 목록
        """
        return [self.clean(text) for text in texts]


# 사용 예시:
if __name__ == '__main__':
    cleaner = TextCleaner(lowercase=True, remove_punctuation=True)
    
    raw_text = "  안녕하세요!!!  이것은   테스트 문본입니다。"
    cleaned = cleaner.clean(raw_text)
    print(f"원본: {raw_text}")
    print(f"정리됨: {cleaned}")
    # 출력: 안녕하세요 이것은 테스트 문본입니다
