print("detector.py loaded")

from typing import Dict, List

class ProfanityDetector:
    """高级脏话检测器，支持更复杂的检测策略"""

    def __init__(self, filter_instance):
        self.filter = filter_instance

    def detect_with_positions(self, text: str) -> List[Dict]:
        """
        检测脏话并返回位置信息
        Returns:
            [{'word': '脏话', 'start': 0, 'end': 2, 'type': 'profanity'}]
        """
        results = []
        for pattern in self.filter.patterns:
            for match in pattern.finditer(text):
                results.append({
                    'word': match.group(0),
                    'start': match.start(),
                    'end': match.end(),
                    'type': 'profanity'
                })
        return results

    def get_severity_score(self, text: str) -> float:
        """计算文本的严重程度分数 (0-1)"""
        profane_words = self.filter.get_profane_words(text)
        if not profane_words:
            return 0.0
        total_words = len(text.split())
        if total_words == 0:
            return 0.0
        score = min(len(profane_words) / total_words, 1.0)
        return score

    def censor_with_context(self, text: str, context_length: int = 10) -> str:
        """
        屏蔽脏话并保留上下文
        Returns:
            处理后的文本，格式：...上下文[***]上下文...
        """
        detections = self.detect_with_positions(text)
        if not detections:
            return text
        result = text
        offset = 0
        for detection in sorted(detections, key=lambda x: x['start']):
            start = detection['start'] + offset
            end = detection['end'] + offset
            word_length = end - start
            censored = self.filter.censor_char * word_length
            result = result[:start] + censored + result[end:]
        return result
