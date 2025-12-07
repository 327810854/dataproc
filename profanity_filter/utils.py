import re
from typing import List

def normalize_text(text: str) -> str:
    """
    标准化文本，移除多余空格、特殊字符
    
    Args:
        text: 输入文本
        
    Returns:
        标准化后的文本
    """
    # 移除多余空格
    text = re.sub(r'\s+', ' ', text)
    
    # 去除首尾空格
    text = text.strip()
    
    return text

def generate_variations(word: str) -> List[str]:
    """
    生成词汇的常见变体
    
    例如: "fuck" -> ["f*ck", "f**k", "f u c k", "fvck"]
    
    Args:
        word: 原始词汇
        
    Returns:
        变体列表
    """
    variations = [word]
    
    # 星号替换
    for i in range(1, len(word) - 1):
        var = word[:i] + '*' + word[i+1:]
        variations.append(var)
    
    # 空格插入
    spaced = ' '.join(list(word))
    variations.append(spaced)
    
    # 常见字母替换
    replacements = {
        'a': ['@', '4'],
        'e': ['3'],
        'i': ['1', '!'],
        'o': ['0'],
        's': ['$', '5'],
        'u': ['v']
    }
    
    for original, subs in replacements.items():
        if original in word.lower():
            for sub in subs:
                variations.append(word.lower().replace(original, sub))
    
    return list(set(variations))

def load_custom_wordlist(file_path: str) -> List[str]:
    """
    从文件加载自定义词库
    
    Args:
        file_path: 词库文件路径
        
    Returns:
        词汇列表
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            words = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        return words
    except FileNotFoundError:
        print(f"警告: 未找到词库文件 {file_path}")
        return []
