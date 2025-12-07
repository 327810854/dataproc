print("filter.py loaded")

import re
from typing import List, Set, Optional
from pathlib import Path

class ProfanityFilter:
    """脏话过滤器核心类"""

    def __init__(self, 
                 languages: List[str] = ['zh', 'en'],
                 censor_char: str = '*',
                 custom_words: Optional[List[str]] = None):
        """
        初始化过滤器
        Args:
            languages: 支持的语言列表 ['zh', 'en', 'ko']
            censor_char: 替换字符，默认为 *
            custom_words: 自定义脏话列表
        """
        self.censor_char = censor_char
        self.bad_words: Set[str] = set()
        self.patterns: List[re.Pattern] = []

        # 加载词库
        self._load_wordlists(languages)

        # 添加自定义词汇
        if custom_words:
            self.add_words(custom_words)

        # 编译正则模式
        self._compile_patterns()

    def _load_wordlists(self, languages: List[str]) -> None:
        """加载指定语言的词库"""
        wordlist_dir = Path(__file__).parent / 'wordlists'

        for lang in languages:
            wordlist_file = wordlist_dir / f'{lang}.txt'
            if wordlist_file.exists():
                with open(wordlist_file, 'r', encoding='utf-8') as f:
                    words = [line.strip() for line in f if line.strip()]
                    self.bad_words.update(words)

    def _compile_patterns(self) -> None:
        """编译正则表达式模式，支持变体检测"""
        self.patterns = []
        for word in self.bad_words:
            # 基础匹配
            pattern = re.escape(word)
            # 支持中间插入空格、特殊字符等变体
            spaced_pattern = r'[\s\*\.\-_]*'.join(list(word))
            # 编译为不区分大小写的正则
            self.patterns.append(re.compile(spaced_pattern, re.IGNORECASE))

    def censor(self, text: str) -> str:
        """
        屏蔽文本中的脏话
        """
        result = text
        for pattern in self.patterns:
            def replace_func(match):
                matched_text = match.group(0)
                return self.censor_char * len(matched_text)
            result = pattern.sub(replace_func, result)
        return result

    def is_profane(self, text: str) -> bool:
        """检测文本是否包含脏话"""
        for pattern in self.patterns:
            if pattern.search(text):
                return True
        return False

    def is_clean(self, text: str) -> bool:
        """检测文本是否干净（不包含脏话）"""
        return not self.is_profane(text)

    def add_words(self, words: List[str]) -> None:
        """添加自定义脏话词汇"""
        self.bad_words.update(words)
        self._compile_patterns()

    def remove_words(self, words: List[str]) -> None:
        """从词库中移除词汇"""
        self.bad_words.difference_update(words)
        self._compile_patterns()

    def get_profane_words(self, text: str) -> List[str]:
        """获取文本中的所有脏话词汇"""
        found_words = []
        for pattern in self.patterns:
            matches = pattern.findall(text)
            found_words.extend(matches)
        return list(set(found_words))
