import os

class StopwordsManager:
    """
    불용어 관리 도구
    
    기능:
    - 사전 정의된 불용어표 로드
    - 사용자 정의 불용어 추가/삭제
    - 여러 불용어표 병합
    """
    
    def __init__(self):
        self.stopwords = set()
    
    @staticmethod
    def load_default_korean():
        """기본 한글 불용어표 로드"""
        default = {
            '이', '그', '저', '것', '수', '등', '들', '및',
            '있', '없', '되', '아니', '이다', '하', '되다',
            '있다', '없다', '나', '우리', '저희', '따르', '의해',
            '에', '에서', '에게', '을', '를', '이', '가', '은', '는',
            '과', '와', '도', '도록', '하기', '위해', '마다', '다시',
        }
        return default
    
    @staticmethod
    def load_default_english():
        """기본 영문 불용어표 로드"""
        default = {
            'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by',
            'for', 'from', 'has', 'he', 'in', 'is', 'it',
            'its', 'of', 'on', 'or', 'that', 'the', 'to',
            'was', 'will', 'with'
        }
        return default
    
    def load_from_file(self, filepath):
        """
        파일에서 불용어표 로드
        
        Args:
            filepath: 파일 경로, 한 줄에 한 불용어
        """
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                self.stopwords.update(line.strip() for line in f if line.strip())
    
    def add(self, words):
        """불용어 추가"""
        if isinstance(words, (list, set)):
            self.stopwords.update(words)
        else:
            self.stopwords.add(words)
    
    def remove(self, words):
        """불용어 삭제"""
        if isinstance(words, (list, set)):
            self.stopwords.difference_update(words)
        else:
            self.stopwords.discard(words)
    
    def get_stopwords(self):
        """모든 불용어 가져오기"""
        return self.stopwords.copy()
    
    def size(self):
        """불용어 수 가져오기"""
        return len(self.stopwords)
    
    def is_stopword(self, word):
        """불용어 여부 확인"""
        return word in self.stopwords
