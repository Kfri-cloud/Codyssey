# Python과 Git 개념 북

이 문서는 콘솔 퀴즈 게임을 만들기 전에 알아야 할 Python과 Git의 핵심 개념을 정리한다. 각 개념은 실제 프로젝트에서 어떻게 사용하는지 퀴즈 게임 예시와 함께 설명한다.

## 1. Python 기초

### 1-1. 변수

변수는 프로그램이 사용할 값에 이름을 붙여 저장하는 공간이다. 저장된 값을 다시 사용하거나 변경할 수 있으므로 입력값, 점수, 게임 상태 등을 관리할 때 필요하다.

```python
quiz_title = "별자리 퀴즈"
score = 0
is_running = True
```

- `quiz_title`: 게임 제목을 저장한다.
- `score`: 현재 점수를 저장한다.
- `is_running`: 게임 실행 여부를 저장한다.

### 1-2. 기본 자료형

| 자료형 | 의미 | 퀴즈 게임 사용 예시 |
|---|---|---|
| `int` | 정수 | 점수, 정답 번호, 메뉴 번호 |
| `str` | 문자열 | 문제, 선택지, 안내 메시지 |
| `bool` | 참 또는 거짓 | 정답 여부, 실행 여부 |
| `list` | 여러 값을 순서대로 저장 | 선택지 목록, 퀴즈 목록 |
| `dict` | 키와 값의 쌍으로 저장 | JSON으로 변환할 퀴즈 데이터 |

```python
score = 3
question = "사자자리의 영어 이름은?"
is_correct = True
choices = ["Leo", "Gemini", "Pisces", "Aries"]
quiz_data = {
    "question": question,
    "choices": choices,
    "answer": 1,
}
```

`list`는 같은 성격의 여러 값을 순서대로 다룰 때 적합하고, `dict`는 `question`, `choices`, `answer`처럼 각 값의 의미를 이름으로 구분할 때 적합하다.

### 1-3. 조건문: if / elif / else

조건문은 조건에 따라 다른 코드를 실행한다. 퀴즈 게임에서는 메뉴 선택, 정답 판정, 최고 점수 갱신에 사용한다.

```python
if selected_answer == quiz.answer:
    print("정답입니다!")
    score += 1
else:
    print("오답입니다.")
```

```python
if menu == 1:
    game.play()
elif menu == 2:
    game.add_quiz()
else:
    print("지원하지 않는 메뉴입니다.")
```

### 1-4. 반복문: for와 while

`for`는 목록처럼 반복할 대상이 있을 때 사용한다. 저장된 퀴즈를 한 문제씩 출제할 때 적합하다.

```python
for quiz in quizzes:
    quiz.display()
```

`while`은 특정 조건이 참인 동안 반복한다. 종료 메뉴를 선택하기 전까지 메뉴를 계속 출력하거나 올바른 입력을 받을 때까지 재입력받는 데 적합하다.

```python
while is_running:
    show_menu()
    menu = input("메뉴를 선택하세요: ")
```

정리하면 다음과 같다.

- `for`: 퀴즈 목록처럼 정해진 대상을 순회할 때 사용한다.
- `while`: 종료 여부나 입력 성공 여부처럼 조건에 따라 반복할 때 사용한다.

### 1-5. 함수, 매개변수와 반환값

함수는 하나의 작업을 수행하는 코드 묶음이다. 반복되는 로직을 재사용하고 기능별로 코드를 나누기 위해 사용한다.

```python
def is_valid_answer(answer: int, choice_count: int) -> bool:
    return 1 <= answer <= choice_count
```

- `answer`, `choice_count`: 함수가 전달받는 매개변수이다.
- `bool`: 반환값의 자료형이다.
- `return`: 계산 결과를 호출한 곳으로 돌려준다.

입력, 검증, 출력, 저장을 각각 함수나 메서드로 분리하면 코드를 이해하고 테스트하기 쉬워진다.

## 2. 클래스와 객체

### 2-1. 클래스와 객체

클래스는 관련된 데이터와 동작을 하나로 묶는 설계도이고, 객체는 클래스로 만든 실제 값이다. 이 프로젝트에서는 문제 한 개를 `Quiz` 클래스로 표현한다.

```python
class Quiz:
    def __init__(self, question: str, choices: list[str], answer: int):
        self.question = question
        self.choices = choices
        self.answer = answer

    def is_correct(self, selected_answer: int) -> bool:
        return selected_answer == self.answer
```

```python
quiz = Quiz(
    "사자자리의 영어 이름은?",
    ["Leo", "Gemini", "Pisces", "Aries"],
    1,
)
```

여기서 `quiz`는 `Quiz` 클래스의 인스턴스, 즉 객체이다.

### 2-2. `__init__`과 `self`

`__init__`은 객체가 생성될 때 자동으로 호출되어 객체의 초기 상태를 만든다. `self`는 현재 메서드를 실행하고 있는 객체 자신을 뜻한다.

```python
self.question = question
```

이 코드는 매개변수로 받은 `question`을 현재 퀴즈 객체의 `question` 속성에 저장한다. 각 객체는 자신의 `self.question` 값을 따로 가진다.

### 2-3. 속성과 메서드

- 속성(attribute): 객체가 보관하는 데이터이다.
- 메서드(method): 객체가 수행하는 동작이다.

`Quiz` 객체의 속성은 `question`, `choices`, `answer`이고, 메서드는 문제 출력과 정답 확인 등이 될 수 있다. `QuizGame` 객체는 퀴즈 목록과 최고 점수를 속성으로 가지며, 게임 실행·퀴즈 추가·목록 출력 등을 메서드로 가진다.

### 2-4. 클래스를 사용하는 이유

- 문제 데이터와 문제에 관련된 동작을 한곳에 묶을 수 있다.
- 여러 문제를 같은 형식으로 생성할 수 있다.
- 게임 진행과 파일 저장 등 서로 다른 책임을 분리할 수 있다.
- 기능을 수정하거나 테스트할 범위가 명확해진다.

## 3. 파일 입출력과 JSON

### 3-1. 파일 읽기와 쓰기

`with open(...)`을 사용하면 작업이 끝난 뒤 파일이 자동으로 닫힌다. 한글이 깨지지 않도록 `encoding="utf-8"`을 지정한다.

```python
with open("state.json", "r", encoding="utf-8") as file:
    content = file.read()
```

```python
with open("state.json", "w", encoding="utf-8") as file:
    file.write(content)
```

파일 모드는 다음과 같다.

- `"r"`: 읽기
- `"w"`: 새로 쓰기. 기존 내용이 있으면 덮어쓴다.
- `"a"`: 기존 내용 뒤에 이어 쓰기

### 3-2. JSON

JSON은 데이터를 키와 값의 구조로 저장하는 형식이다. 사람이 읽기 쉽고 Python의 `dict`, `list`와 변환하기 쉬워 퀴즈와 최고 점수를 저장하기에 적합하다.

```json
{
  "quizzes": [
    {
      "question": "사자자리의 영어 이름은?",
      "choices": ["Leo", "Gemini", "Pisces", "Aries"],
      "answer": 1
    }
  ],
  "best_score": null
}
```

Python에서는 표준 라이브러리인 `json` 모듈을 사용한다.

```python
import json

with open("state.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

with open("state.json", "r", encoding="utf-8") as file:
    data = json.load(file)
```

- `ensure_ascii=False`: 한글을 그대로 저장한다.
- `indent=2`: 사람이 읽기 쉽게 들여쓰기한다.

### 3-3. 예외 처리: try / except

예외 처리는 잘못된 입력이나 파일 오류가 발생해도 프로그램이 비정상 종료되지 않게 한다.

```python
try:
    selected_answer = int(input("정답 번호: ").strip())
except ValueError:
    print("숫자를 입력해 주세요.")
```

파일을 불러올 때는 상황별 예외를 구분한다.

```python
import json

try:
    with open("state.json", "r", encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError:
    print("저장 파일이 없어 기본 퀴즈를 사용합니다.")
except (json.JSONDecodeError, OSError):
    print("저장 파일을 읽을 수 없어 기본 퀴즈로 복구합니다.")
```

프로그램 전체에서는 `KeyboardInterrupt`와 `EOFError`도 처리하여 `Ctrl+C`나 입력 스트림 종료가 발생했을 때 안내 메시지를 출력하고 안전하게 종료한다.

## 4. 입력 검증

사용자 입력은 그대로 신뢰하면 안 된다. 이 프로젝트에서는 다음 순서로 검증한다.

1. `strip()`으로 앞뒤 공백을 제거한다.
2. 빈 문자열인지 확인한다.
3. 숫자가 필요한 입력은 `int()`로 변환한다.
4. 메뉴 번호나 정답 번호가 허용 범위에 있는지 확인한다.
5. 잘못된 경우 안내 메시지를 보여주고 다시 입력받는다.

```python
def read_number(prompt: str, minimum: int, maximum: int) -> int:
    while True:
        raw_value = input(prompt).strip()

        if not raw_value:
            print("값을 입력해 주세요.")
            continue

        try:
            value = int(raw_value)
        except ValueError:
            print("숫자를 입력해 주세요.")
            continue

        if minimum <= value <= maximum:
            return value

        print(f"{minimum}부터 {maximum} 사이의 숫자를 입력해 주세요.")
```

공통 입력 함수를 사용하면 메뉴, 정답, 퀴즈 등록 입력에 같은 검증 규칙을 적용할 수 있다.

## 5. Git 기초

### 5-1. Git을 사용하는 이유

Git은 파일의 변경 이력을 기록하는 버전 관리 도구이다. 이전 상태를 확인하거나 되돌릴 수 있고, 브랜치를 이용해 기능별로 안전하게 작업할 수 있다.

### 5-2. 주요 명령어

| 명령어 | 역할 |
|---|---|
| `git init` | 현재 디렉터리를 Git 저장소로 만든다. |
| `git add` | 커밋할 변경 내용을 스테이징한다. |
| `git commit` | 스테이징한 변경 내용을 이력으로 기록한다. |
| `git push` | 로컬 커밋을 원격 저장소에 업로드한다. |
| `git pull` | 원격 저장소의 변경 내용을 가져와 현재 브랜치에 반영한다. |
| `git checkout` | 브랜치를 이동하거나 파일의 특정 상태를 가져온다. |
| `git clone` | 원격 저장소를 새로운 로컬 디렉터리로 복제한다. |

```bash
git clone https://github.com/user/star-quiz-game.git
git checkout -b feature/quiz-play
git add .
git commit -m "feat: 퀴즈 풀이 기능 추가"
git push origin feature/quiz-play
```

### 5-3. 브랜치와 병합

브랜치는 기존 코드에 영향을 적게 주면서 기능을 따로 개발하기 위한 작업 공간이다. 기능 구현이 끝나면 해당 브랜치를 `main`에 병합한다.

```bash
git checkout main
git merge feature/quiz-play
```

이 프로젝트에서는 미션 요구사항에 따라 최소 한 번 이상 별도 브랜치를 만들고 병합 기록을 남긴다.

### 5-4. 커밋 규칙

커밋은 하나의 목적을 가진 작은 단위로 작성한다. 메시지에는 무엇을 변경했는지 명확하게 기록한다.

```text
feat: Quiz 클래스와 기본 문제 추가
feat: 퀴즈 풀이 기능 추가
feat: 퀴즈 등록과 목록 기능 추가
feat: 최고 점수 저장 기능 추가
fix: 숫자가 아닌 입력의 예외 처리
docs: 실행 방법과 데이터 구조 설명
```

대표적인 접두어는 다음과 같다.

- `feat`: 기능 추가
- `fix`: 오류 수정
- `docs`: 문서 수정
- `refactor`: 동작을 유지하면서 구조 개선
- `test`: 테스트 추가 또는 수정
- `style`: 코드 동작과 무관한 형식 수정

커밋 전에는 `git status`와 `git diff`로 변경 범위, 불필요한 파일, 디버깅 코드와 민감한 정보가 포함되지 않았는지 확인한다.

## 6. 프로젝트 적용 요약

| 학습 개념 | 프로젝트 적용 위치 |
|---|---|
| 변수와 자료형 | 점수, 메뉴 번호, 문제와 선택지 저장 |
| 조건문 | 메뉴 분기, 정답 판정, 최고 점수 비교 |
| 반복문 | 메뉴 반복, 퀴즈 출제, 입력 재시도 |
| 함수와 메서드 | 입력, 게임 진행, 저장 기능 분리 |
| 클래스와 객체 | `Quiz`, `QuizGame`, `Storage` 구성 |
| 파일과 JSON | 퀴즈 목록과 최고 점수 영속화 |
| 예외 처리 | 잘못된 입력, 파일 없음·손상, 안전 종료 |
| Git | 기능별 커밋, 브랜치 생성·병합, 원격 저장소 동기화 |
