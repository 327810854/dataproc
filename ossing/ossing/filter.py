import json
import os

class SensitiveWordFilter:
    """
    민감한 단어 필터링 도구
    
    지원 기능:
    - 사용자 정의 민감한 단어 사전 로드
    - 민감한 단어 감지 및 대체
    - 여러 대체 전략 지원 (* 또는 사용자 정의 문자로 대체)
    """
    
    def __init__(self, replacement_char='*'):
        """
        필터 초기화
        
        Args:
            replacement_char: 민감한 단어를 대체할 문자, 기본값은 '*'
        """
        self.replacement_char = replacement_char
        self.sensitive_words = set()
        self.sensitive_dict = {}  # 민감한 단어와 대체 단어 저장
    
    def load_from_list(self, words_list):
        """
        목록에서 민감한 단어 로드
        
        Args:
            words_list: 민감한 단어 목록, 예: ['욕설1', '욕설2']
        """
        self.sensitive_words.update(words_list)
        for word in words_list:
            self.sensitive_dict[word] = self.replacement_char * len(word)
    
    def load_from_file(self, filepath):
        """
        파일에서 민감한 단어 로드 (한 줄에 한 단어)
        
        Args:
            filepath: 민감한 단어 파일 경로
        """
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                words = [line.strip() for line in f if line.strip()]
            self.load_from_list(words)
    
    def load_from_json(self, json_data):
        """
        JSON에서 민감한 단어 및 대체 단어 로드
        
        Args:
            json_data: JSON 문자열 또는 사전, 형식: {"민감한단어1": "대체단어1", ...}
        """
        if isinstance(json_data, str):
            data = json.loads(json_data)
        else:
            data = json_data
        
        self.sensitive_dict.update(data)
        self.sensitive_words.update(data.keys())
    
    def has_sensitive_words(self, text):
        """
        텍스트가 민감한 단어를 포함하는지 확인
        
        Args:
            text: 입력 텍스트
        
        Returns:
            민감한 단어 포함 시 True, 아니면 False
        """
        for word in self.sensitive_words:
            if word in text:
                return True
        return False
    
    def get_sensitive_words(self, text):
        """
        텍스트에서 모든 민감한 단어 가져오기
        
        Args:
            text: 입력 텍스트
        
        Returns:
            민감한 단어 목록
        """
        found = []
        for word in self.sensitive_words:
            if word in text:
                found.append(word)
        return found
    
    def filter(self, text):
        """
        텍스트에서 민감한 단어 필터링
        
        Args:
            text: 입력 텍스트
        
        Returns:
            필터링된 텍스트
        """
        result = text
        for word, replacement in self.sensitive_dict.items():
            result = result.replace(word, replacement)
        return result
    
    def filter_with_strategy(self, text, strategy='asterisk'):
        """
        다양한 전략으로 민감한 단어 필터링
        
        Args:
            text: 입력 텍스트
            strategy: 전략
                - 'asterisk': * 로 대체
                - 'custom': sensitive_dict 에 정의된 대체 단어 사용
                - 'remove': 직접 삭제
        
        Returns:
            필터링된 텍스트
        """
        if strategy == 'asterisk':
            result = text
            for word in self.sensitive_words:
                replacement = self.replacement_char * len(word)
                result = result.replace(word, replacement)
            return result
        elif strategy == 'custom':
            return self.filter(text)
        elif strategy == 'remove':
            result = text
            for word in self.sensitive_words:
                result = result.replace(word, '')
            return result
        else:
            raise ValueError(f"Unknown strategy: {strategy}")


# 사용 예시:
if __name__ == '__main__':
    filter_obj = SensitiveWordFilter(replacement_char='*')
    
    # 방식 1: 목록에서 로드
    filter_obj.load_from_list(['욕설', '부적절한'])
    
    # 방식 2: JSON에서 로드 (사용자 정의 대체 단어 가능)
    filter_obj.load_from_json({
        '나쁜말1': '***',
        '나쁜말2': '[차단됨]'
    })
    
    text = "이것은 욕설과 부적절한 내용입니다"
    filtered = filter_obj.filter(text)
    print(f"원본: {text}")
    print(f"필터링됨: {filtered}")
    # 출력: 이것은 ***과 ***내용입니다
