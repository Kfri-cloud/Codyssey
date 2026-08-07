from quiz import Quiz
from untils import get_number

class QuizGame:
    def __init__(self):
        self.quizzes =[]
        self.score = 0
        self.sloved_count =0

    def register_default_quizzes(self):
        quiz1 = Quiz(
              "북두칠성은 몇 개의 별로 이루어져 있을까요?",
            ["5개", "6개", "7개", "8개"],
            3
        ) 
        quiz2 = Quiz(
            "밤하늘에서 가장 밝은 별은 무엇일까요?",
            ["시리우스", "북극성", "태양", "베가"],
            1
        )

        self.quizzes.append(quiz1)
        self.quizzes.append(quiz2)

    def play_quiz(self):
        if len(self.quizzes)==0:
            print("퀴즈가 없습니다")
            return

        print("\n========= 별 퀴즈 게임 시작 =========")

        for quiz in self.quizzes:
            quiz.display()

            user_answer=get_number(
                "정답 번호를 입력하세요.",
                0,
                len(quiz.choces)

            )
            self.solved_count +=1

            if quiz.check_answer(user_answer):
                print("정답입니다!")
                self.score +=1
            else:
                print(f"오답입니다.정답은{quiz.answer}번입니다.")
     
    def add_quiz(self):
        print("\n =============문제추가===========")

        question = input("문제 내용을 입력하세요.").strip()
        choices = []
   
        for number in range(1,5):   
            choice =input(f"{number}번 보기 입력: ").strip()
            choices.append(choice)
        
        answer =get_number("정답을 입력해주세요.",1,4)
        new_quiz=Quiz(question,choices,answer)
        self.quizzes.append(new_quiz)

        print ("문제 새로 등록")

    def show_quize_list(self):
        print("\n ======퀴즈목록========")

        if len(self.quizzes) ==0:
            print ("등록된 퀴즈가 없습니다.") 
            return

        for number,quiz in enumerate(self.quizzes,start=1):
            print(f"\n문제{number}:{quiz.question}") 
            
    def show_score(self):
        print("\n=======점수확인========= ")
        print (f"푼 문제:{self.solved_count}개")
        print (f"맞힌 문제:{self.score}개")

        if self.solved_dount==0:
            print("아직 푼 문제가 없습니다.")
        else:
            accuracy =self.socre /self.solved_clount*100
            print(f"접답률 :{accuracy:.1f}%")

    def shoow_menu(self):
        print("\n"+"="*25)
        print("   밤하늘 별 퀴즈")
        print("=" * 25)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        
    def show_exit_screen(self):
        print("\n===== 게임 종료 =====")
        print(f"최종 점수: {self.score}점")
        print(f"푼 문제: {self.solved_count}개")
        print("밤하늘 별 퀴즈를 이용해 주셔서 감사합니다.")