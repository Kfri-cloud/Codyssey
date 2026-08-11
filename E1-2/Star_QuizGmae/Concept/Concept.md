// ...existing code...

# Python과 Git 개념 북

## 1. Python 기초

### 1-1. 변수(Variable)란?

변수는 데이터를 저장하는 이름 붙은 공간입니다. 프로그램은 변수를 사용해서 값을 기억하고, 계산하고, 출력할 수 있습니다.

예시:

```python
name = "철수"
age = 20
is_student = True
```

- `name`은 문자열 값을 저장합니다.
- `age`는 정수 값을 저장합니다.
- `is_student`는 참/거짓 값을 저장합니다.

변수를 사용하는 이유:

- 값을 재사용할 수 있다.
- 코드를 더 이해하기 쉽게 만든다.
- 사용자 입력, 계산 결과, 상태값 등을 저장할 수 있다.

---

### 1-2. 기본 자료형

Python은 여러 자료형을 가지고 있으며, 각각 다른 종류의 데이터를 저장합니다.

#### 1) int: 정수

정수는 소수점이 없는 숫자입니다.

```python
score = 100
count = 5
```

#### 2) str: 문자열

문자열은 텍스트 데이터를 의미합니다.

```python
message = "안녕하세요"
name = "민지"
```

문자열은 연결, 길이 확인, 자르기 등이 가능합니다.

```python
print(message + "!")
print(len(name))
```

#### 3) bool: 불리언

불리언은 참(`True`) 또는 거짓(`False`)을 표현합니다.

```python
is_active = True
is_logged_in = False
```

불리언은 조건문에서 매우 자주 사용됩니다.

#### 4) list: 리스트

리스트는 여러 값을 순서대로 저장하는 자료형입니다.

```python
numbers = [1, 2, 3, 4]
fruits = ["사과", "바나나", "오렌지"]
```

리스트는 값 추가, 삭제, 변경이 가능합니다.

```python
numbers.append(5)
print(numbers)
```

#### 5) dict: 딕셔너리

딕셔너리는 key와 value 쌍으로 데이터를 저장합니다.

```python
student = {
    "name": "철수",
    "age": 20,
    "grade": "A"
}
```

딕셔너리는 이름으로 값을 찾는 데 매우 적합합니다.

```python
print(student["name"])
```

---

### 1-3. int, str, bool, list, dict 차이

자료형을 이해할 때 중요한 것은 “어떤 종류의 데이터를 저장하는지”입니다.

- `int`: 정수, 숫자
- `str`: 문자열, 텍스트
- `bool`: True/False
- `list`: 여러 값을 순서대로 저장
- `dict`: 이름(key)과 값(value) 쌍으로 저장

예시:

- 학생의 나이: `int`
- 학생의 이름: `str`
- 출석 여부: `bool`
- 수강 과목 목록: `list`
- 학생 전체 정보: `dict`

---

### 1-4. 조건문: if / elif / else

조건문은 특정 조건에 따라 다른 동작을 실행하도록 합니다.

```python
score = 85

if score >= 90:
    print("우수")
elif score >= 70:
    print("보통")
else:
    print("노력 필요")
```

- `if`: 조건이 참이면 실행
- `elif`: 앞 조건이 거짓일 때 추가 조건 검사
- `else`: 앞의 모든 조건이 거짓일 때 실행

조건문은 프로그램에서 매우 중요합니다. 예를 들어 로그인 여부, 점수 판정, 재고 확인 등에 사용됩니다.

---

### 1-5. 반복문: for와 while

#### for 문

`for`는 정해진 범위나 목록을 순회할 때 사용합니다.

```python
for i in range(3):
    print(i)
```

출력:

```python
0
1
2
```

또는 리스트 순회:

```python
fruits = ["사과", "바나나", "딸기"]
for fruit in fruits:
    print(fruit)
```

#### while 문

`while`은 조건이 참인 동안 반복합니다.

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

차이점:

- `for`: 반복 횟수가 정해져 있거나 목록을 순회할 때 적합
- `while`: 조건이 중요하고 계속 실행 여부를 결정할 때 적합

---

### 1-6. 함수(Function)

함수는 특정 작업을 수행하는 코드 블록입니다. 같은 코드를 반복해서 작성하지 않고 재사용할 수 있게 해줍니다.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
```

- `a`, `b`는 매개변수(parameter)
- `return`은 결과를 함수 밖으로 반환
- 함수는 여러 번 호출할 수 있음

함수의 장점:

- 코드를 재사용할 수 있다.
- 논리를 구조적으로 나눌 수 있다.
- 큰 프로그램을 관리하기 쉬워진다.

---

## 2. 클래스와 객체

### 2-1. 클래스(Class)란?

클래스는 객체를 만들기 위한 설계도입니다. 같은 종류의 데이터를 묶고, 그에 맞는 동작을 정의할 때 사용합니다.

예시:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"안녕하세요, 제 이름은 {self.name}이고, 나이는 {self.age}살입니다.")
```

클래스를 사용하는 이유:

- 관련된 데이터를 한 곳에 묶을 수 있다.
- 코드 구조를 더 깔끔하게 관리할 수 있다.
- 현실 세계의 개념을 모델링하기 좋다.

---

### 2-2. 객체(Object)란?

객체는 클래스에서 만들어진 실제 인스턴스입니다.

```python
student1 = Student("민수", 20)
student1.introduce()
```

`student1`은 `Student` 클래스의 객체입니다.

---

### 2-3. __init__ 메서드와 self

`__init__` 메서드는 객체가 생성될 때 자동으로 실행됩니다. 객체의 속성을 초기화하는 역할을 합니다.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

여기서:

- `self`는 현재 객체 자신을 의미
- `self.name = name`은 객체의 이름 속성을 저장
- `self.age = age`는 객체의 나이 속성을 저장

`self`는 객체마다 다른 데이터를 관리할 수 있게 합니다.

---

### 2-4. 속성(Attribute)과 메서드(Method)

클래스에는 두 가지 중요한 구성 요소가 있습니다.

#### 속성(Attribute)

속성은 객체가 가지고 있는 데이터입니다.

```python
self.name
self.age
```

#### 메서드(Method)

메서드는 객체가 수행할 수 있는 행동입니다.

```python
def introduce(self):
    print("학생 소개")
```

예를 들어 학생 객체는:

- 속성: 이름, 나이, 학년
- 메서드: 소개하기, 점수 계산하기

이런 식으로 클래스는 데이터를 다루는 구조를 만듭니다.

---

## 3. 파일 입출력

### 3-1. 파일을 열고, 읽고, 쓰는 기본 과정

#### 파일 쓰기

```python
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("hello world")
```

- `"w"`: 쓰기 모드
- 파일이 없으면 생성됨

#### 파일 읽기

```python
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```

- `"r"`: 읽기 모드
- 파일 내용을 문자열로 읽어옴

#### 파일에 이어쓰기

```python
with open("example.txt", "a", encoding="utf-8") as file:
    file.write("\n추가 내용")
```

- `"a"`: 이어쓰기 모드

`with`를 사용하면 파일이 자동으로 닫히므로 안전합니다.

---

### 3-2. JSON이란?

JSON은 JavaScript Object Notation의 약자이며, 데이터를 구조적으로 저장하는 표준 형식입니다.

예시:

```json
{
  "name": "철수",
  "age": 20,
  "grade": "A"
}
```

Python에서는 `json` 모듈을 사용합니다.

```python
import json

student = {
    "name": "철수",
    "age": 20,
    "grade": "A"
}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, ensure_ascii=False)
```

JSON을 읽는 예시:

```python
with open("student.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data)
```

왜 JSON을 사용할까?

- 사람도 읽기 쉽다.
- Python에서 처리하기 쉽다.
- 웹, 서버, 앱 데이터 교환에 자주 사용된다.

---

### 3-3. try / except로 오류 처리하기

프로그램은 예외 상황이 발생할 수 있습니다. 예를 들어 숫자로 변환할 수 없는 문자열이 들어오면 문제가 생길 수 있습니다.

```python
try:
    number = int("abc")
except ValueError:
    print("숫자로 변환할 수 없는 값입니다.")
```

`try/except`는 오류가 발생해도 프로그램이 강제로 종료되지 않도록 처리합니다.

오류 처리의 중요성:

- 사용자 입력이 잘못되더라도 프로그램이 죽지 않는다.
- 파일이 없거나 형식이 잘못돼도 안전하게 처리할 수 있다.
- 프로그램을 더 안정적으로 만들 수 있다.

---

## 4. Git 기초

### 4-1. Git이란?

Git은 파일의 변경 이력을 관리하는 버전 관리 도구입니다. 여러 사람이 같은 프로젝트를 함께 작업할 때 매우 중요합니다.

Git의 목적:

- 변경 기록을 남긴다.
- 이전 상태로 되돌릴 수 있다.
- 팀 협업을 쉽게 만든다.
- 브랜치로 기능별 개발을 진행할 수 있다.

---

### 4-2. 주요 Git 명령어

#### git init

현재 폴더를 Git 저장소로 초기화합니다.

```bash
git init
```

#### git add

변경된 파일을 스테이징 영역에 올립니다.

```bash
git add file.py
```

#### git commit

스테이징된 변화를 저장합니다.

```bash
git commit -m "초기 커밋"
```

#### git push

로컬 저장소에 있는 변경 사항을 원격 저장소에 업로드합니다.

```bash
git push origin main
```

#### git pull

원격 저장소의 최신 변경 사항을 로컬로 가져옵니다.

```bash
git pull origin main
```

#### git checkout

브랜치 이동이나 특정 상태 복원을 할 때 사용합니다.

```bash
git checkout feature-branch
```

#### git clone

원격 저장소를 로컬 컴퓨터에 복사합니다.

```bash
git clone https://github.com/user/repo.git
```

---

### 4-3. 브랜치와 병합

브랜치는 프로젝트를 여러 갈래로 나누어 개발할 수 있게 해줍니다. 보통 기능 개발이나 수정 작업을 별도 브랜치에서 진행하고, 완료 후 메인 브랜치에 합칩니다.

브랜치 생성:

```bash
git branch feature-login
```

브랜치 이동:

```bash
git checkout feature-login
```

병합:

```bash
git checkout main
git merge feature-login
```

브랜치는 협업 시 매우 중요합니다. 여러 사람이 동시에 작업하더라도 기능별로 나누어 개발할 수 있습니다.

---

### 4-4. 커밋 규칙 (Commit Rules)

커밋은 단순히 코드를 저장하는 것이 아니라, 어떤 변경을 왜 했는지를 기록하는 작업입니다. 좋은 커밋 규칙을 지키면 협업과 추적이 쉬워집니다.

#### 1) 커밋은 의미 단위로 하기
하나의 커밋에는 하나의 목적만 담는 것이 좋습니다.

좋은 예:
- 기능 추가
- 버그 수정
- 문서 수정
- 스타일 정리

나쁜 예:
- 기능 추가 + 문서 수정 + 주석 삭제를 한 번에 넣기

#### 2) 커밋 메시지는 명확하게 작성하기
커밋 메시지는 “무엇을 변경했는지”가 보여야 합니다.

권장 형식:

```bash
git commit -m "feat: 로그인 기능 추가"
git commit -m "fix: 사용자 입력 검증 오류 수정"
git commit -m "docs: README 내용 보완"
```

- `feat`: 새로운 기능 추가
- `fix`: 버그 수정
- `docs`: 문서 작업
- `refactor`: 코드 구조 개선
- `style`: 포맷팅, 코드 스타일 수정
- `test`: 테스트 추가/수정

#### 3) 커밋 전 확인 사항
커밋하기 전에 다음을 확인하는 습관을 들이세요.

- 변경 내용이 의도한 것인지 확인
- 불필요한 파일이 포함되지 않았는지 확인
- 오타나 디버깅 코드가 남아있지 않은지 확인
- 실행해 보고 테스트가 필요한 경우 확인

예시:

```bash
git status
git diff
```

#### 4) 작은 단위로 자주 커밋하기
큰 변경을 한 번에 올리면 나중에 원인을 찾기 어렵습니다. 기능 단위나 작업 단위로 나누어 커밋하는 것이 좋습니다.

예시:
- 로그인 화면 UI 추가
- 로그인 로직 구현
- 에러 메시지 처리

이렇게 나누면 문제가 생겼을 때 어디를 수정해야 하는지 쉽게 찾을 수 있습니다.

#### 5) 커밋 메시지는 너무 길지 않게
커밋 메시지는 한 줄로 간단하게 작성하는 것이 좋습니다. 자세한 내용은 필요하면 PR 설명이나 문서에 적으면 됩니다.

좋은 예:

```bash
git commit -m "feat: 사용자 회원가입 기능 추가"
```

나쁜 예:

```bash
git commit -m "오늘 이것저것 수정했다"
```

#### 6) 브랜치별로 작업하고 병합하기
기능 개발은 메인 브랜치에 직접 수정하기보다 별도 브랜치를 만들어 작업하는 것이 안전합니다.

예시:

```bash
git checkout -b feature/login
# 작업 수행
git add .
git commit -m "feat: 로그인 기능 추가"
git push origin feature/login
```

작업이 끝나면 메인 브랜치에 병합합니다.

#### 7) 커밋 규칙의 핵심
좋은 커밋은 다음 조건을 만족해야 합니다.

- 한 번에 하나의 목적만 다룬다.
- 어떤 변경인지 이해할 수 있다.
- 다른 사람이 내용을 빠르게 파악할 수 있다.
- 나중에 되돌리기 쉬운 단위로 나뉜다.

즉, 커밋은 “기록”이며 “협업의 도구”입니다. 단순 저장이 아니라 프로젝트를 이해하기 위한 설명서 역할을 합니다.

---
