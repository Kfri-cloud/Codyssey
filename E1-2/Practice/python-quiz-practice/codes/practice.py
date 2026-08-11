
for number, choice in enumerate(choices, start=1):
    print(f"{number}. {choice}")

user_input = input("정답 번호를 입력하세요: ").strip()

class Quiz:
    def __init__(self,question,choices,answer):
        self.question = question
        self.choices =choices
        self.answer =answer

    def display(self):
        print()
        print(self.question)

        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")
def check_answer(self,user_answer):
    quiz =Quiz(
    "Python 파일의 확장자는 무엇일까요?"
    [".html", ".py", ".jpg", ".txt"],
     2
)

    quiz.display()
user_answer=get_number("정답 번호: ",1,4)
if quit.check_answer(user_answer):
    print("정답입니다.")
else :
    print("오답입니다.")