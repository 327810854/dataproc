# ossing - 텍스트 전처리 라이브러리

한글 및 영문 텍스트 정리, 민감한 단어 필터링, 토크나이징 및 단어 빈도 통계를 지원하는 가볍고 효율적인 전처리 라이브러리입니다.

## 기능 특징

- **텍스트 정리**: 소문자 변환, 구두점 제거, 불필요한 공백 제거, Unicode 정규화
- **민감한 단어 필터링**: 다양한 대체 전략 지원, 사용자 정의 민감한 단어 사전
- **토크나이징 및 단어 빈도 통계**: 한글 형태소 분석, 불용어 처리, 고빈도 단어 추출
- **사용하기 쉬운 API**: 간단하고 직관적인 인터페이스 설계

## 설치

```
pip install -e .
```

### 1. 텍스트 정리

```
from ossing import TextCleaner

cleaner = TextCleaner()
text = "  안녕   세계!!!  "
cleaned = cleaner.clean(text)
print(cleaned)  # "안녕 세계"
```

### 2. 민감한 단어 필터링

```
from ossing import SensitiveWordFilter

filter_obj = SensitiveWordFilter()
filter_obj.load_from_list(['나쁜말1', '나쁜말2'])

text = "이것은 나쁜말1과 나쁜말2의 내용"
filtered = filter_obj.filter(text)
print(filtered)  # "이것은 ***과 ***의 내용"
```

### 3. 토크나이징 및 단어 빈도 통계

```
from ossing import Tokenizer

tokenizer = Tokenizer()
text = "오늘 날씨가 정말 좋습니다. 공원에 가겠습니다."

tokens = tokenizer.tokenize(text, remove_stopwords=True)
freq = tokenizer.get_word_frequency(text, remove_stopwords=True, top_n=5)

print(tokens)
print(freq)
```

## 완전한 처리 흐름

```
from ossing import TextCleaner, SensitiveWordFilter, Tokenizer

# 초기화
cleaner = TextCleaner()
filter_obj = SensitiveWordFilter()
filter_obj.load_from_list(['나쁜말'])
tokenizer = Tokenizer()

# 처리
text = "  이것은 나쁜말 예시입니다!!!  "
cleaned = cleaner.clean(text)
filtered = filter_obj.filter(cleaned)
tokens = tokenizer.tokenize(filtered, remove_stopwords=True)

print(f"원본: {text}")
print(f"정리됨: {cleaned}")
print(f"필터링됨: {filtered}")
print(f"토크나이징: {tokens}")
```

## API 문서

### TextCleaner

```
TextCleaner(
    lowercase=True,           # 소문자로 변환
    remove_punctuation=True,  # 구두점 제거
    remove_numbers=False,     # 숫자 제거
    remove_extra_spaces=True  # 불필요한 공백 제거
)

# 메서드
.clean(text)              # 단일 텍스트 정리
.batch_clean(texts)       # 일괄 정리
```

### SensitiveWordFilter

```
filter_obj = SensitiveWordFilter(replacement_char='*')

# 메서드
.load_from_list(words)         # 목록에서 로드
.load_from_file(filepath)      # 파일에서 로드
.load_from_json(json_data)     # JSON에서 로드
.has_sensitive_words(text)     # 민감한 단어 포함 확인
.get_sensitive_words(text)     # 민감한 단어 목록 가져오기
.filter(text)                  # 필터링
.filter_with_strategy(text, strategy)  # 전략을 사용한 필터링
```

### Tokenizer

```
tokenizer = Tokenizer(stopwords_set=None)

# 메서드
.tokenize(text, remove_stopwords=False)              # 토크나이징
.get_word_frequency(text, remove_stopwords=True)    # 단어 빈도 통계
.batch_tokenize(texts)                               # 일괄 토크나이징
.get_vocabulary_size(text)                           # 어휘량
.add_stopwords(words)                                # 불용어 추가
```

## 테스트

```
python -m pytest tests/
```

## 예시

`examples/` 디렉토리의 예시 코드를 참고하세요.

## 기여

Pull Request 및 Issue 제출을 환영합니다!

## 라이선스

MIT License
```

### [mycats/README.md](pplx://action/translate) — 샘플 저장소 설명

````markdown
# mycats - 텍스트 전처리 데모

이것은 `ossing` 텍스트 전처리 라이브러리를 사용한 완전한 데모 프로젝트입니다. 사용자 리뷰 데이터를 처리하고 분석하는 방법을 보여줍니다.

## 기능

- 리뷰 텍스트 정리 및 규범화
- 민감한 단어 필터링
- 토크나이징 및 단어 빈도 통계
- 처리 보고서 생성

## 의존성 설치

```
pip install -r requirements.txt
```

## 데모 실행

```
python demo.py
```

## 출력 결과

데모는 `output/` 디렉토리에 다음을 생성합니다:
- `processed_reviews.txt` - 처리된 리뷰
- `report.txt` - 통계 보고서

## 샘플 데이터

샘플로 5개의 모의 사용자 리뷰 데이터를 사용합니다 (한글과 영문 혼합).

## 민감한 단어 목록 수정

`demo.py`의 `filter.load_from_list()` 부분을 편집하세요:

```
self.filter.load_from_list([
    '당신의 민감한 단어1',
    '당신의 민감한 단어2',
    # ...
])
```

## 확장

`demo.py`를 수정하여 다음을 수행할 수 있습니다:
- 실제 리뷰 데이터 파일 로드
- 데이터베이스에 처리 결과 저장
- 더 많은 분석 기능 추가
- 웹 애플리케이션으로 통합

## 라이선스

MIT License
```


```bash
cd ossing

# 모든 테스트 실행
python -m pytest tests/ -v

# 특정 테스트 실행
python -m pytest tests/test_cleaner.py -v

# 커버리지 확인
pip install pytest-cov
python -m pytest tests/ --cov=ossing
```

### 샘플 사용 테스트

```bash
cd mycats

# 로컬 ossing 라이브러리 설치
pip install -e ../ossing

# 데모 실행
python demo.py
```

***



발표 시 다음 단계를 순서대로 실행하세요:

```bash
# 1. 라이브러리 설치 및 가져오기 확인
python -c "from ossing import TextCleaner, SensitiveWordFilter, Tokenizer; print('✓ 라이브러리 로드 성공')"

# 2. 단위 테스트 실행, 테스트 커버리지 표시
python -m pytest tests/ -v

# 3. 예시 스크립트 실행, 완전한 기능 표시
python examples/basic_usage.py

# 4. 데모 프로젝트 실행, 실제 응용 표시
cd mycats
python demo.py

# 5. 출력 결과 확인
cat output/processed_reviews.txt
cat output/report.txt
```


