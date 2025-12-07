import re
from collections import Counter


class Tokenizer:
    """
    텍스트 분리 및 단어 빈도 통계 도구 (순수 Python, Java/konlpy 불필요)
    """

    def __init__(self, stopwords_set=None):
        """
        토크나이저 초기화

        Args:
            stopwords_set: 불용어 집합 (set), None 이면 기본 집합 사용
        """
        self.stopwords = stopwords_set or self._load_default_stopwords()
        self.word_freq = Counter()

    def _load_default_stopwords(self):
        """기본 한글/영문 불용어 로드"""
        default_stopwords = {
            # 한글 불용어
            '이', '그', '저', '것', '수', '등', '들', '및',
            '있', '없', '되', '아니', '이다', '하', '되다',
            '있다', '없다', '나', '우리', '저희', '따르', '의해',
            '에', '에서', '에게', '을', '를', '이', '가', '은', '는',
            '과', '와', '도', '도록', '하기', '위해', '마다', '다시',
            '또', '또한', '또는', '혹은', '만', '그리고', '대해',
            '의', '입니다', '됩니다', '있습니다', '없습니다',
            # 영문 불용어
            'a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at',
            'to', 'for', 'of', 'is', 'are', 'was', 'were', 'be',
            'have', 'has', 'do', 'does', 'did', 'will', 'would',
            'could', 'should', 'may', 'might', 'must', 'can'
        }
        return default_stopwords

    def add_stopwords(self, words):
        """사용자 정의 불용어 추가"""
        if isinstance(words, (list, set)):
            self.stopwords.update(words)

    def tokenize(self, text, remove_stopwords=False):
        """
        텍스트 분리 (간단한 정규식 기반)

        Args:
            text: 입력 텍스트
            remove_stopwords: 불용어 제거 여부
        """
        # 한글(가-힣), 호환 자모, 영문, 숫자
        pattern = r'[\uac00-\ud7af]+|[\u1100-\u11ff]+|[a-zA-Z]+|[0-9]+'
        tokens = re.findall(pattern, text)

        # 영문은 소문자로 통일
        tokens = [t.lower() if t.isascii() else t for t in tokens]

        # 공백 제거
        tokens = [t for t in tokens if t.strip()]

        # 불용어 제거
        if remove_stopwords:
            tokens = [t for t in tokens if t not in self.stopwords]

        return tokens

    def get_word_frequency(self, text, remove_stopwords=True, top_n=None):
        """
        단일 텍스트에 대한 단어 빈도 통계

        Returns:
            dict 또는 [(단어, 빈도), ...]
        """
        tokens = self.tokenize(text, remove_stopwords=remove_stopwords)
        word_freq = Counter(tokens)

        if top_n:
            return word_freq.most_common(top_n)
        return dict(word_freq)

    def batch_tokenize(self, texts, remove_stopwords=False):
        """텍스트 목록 일괄 분리"""
        return [self.tokenize(t, remove_stopwords=remove_stopwords) for t in texts]

    def get_vocabulary_size(self, text, remove_stopwords=True):
        """어휘량(중복 제거된 단어 수)"""
        tokens = self.tokenize(text, remove_stopwords=remove_stopwords)
        return len(set(tokens))
