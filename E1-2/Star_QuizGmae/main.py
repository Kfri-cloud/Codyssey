"""별자리 퀴즈 게임."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class Quiz:
    """객관식 퀴즈 한 문제를 표현한다."""

    def __init__(self, question: str, choices: list[str], answer: int) -> None:
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self) -> None:
        """문제와 네 개의 선택지를 출력한다."""
        print(self.question)
        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def is_correct(self, selected_answer: int) -> bool:
        """사용자가 고른 번호가 정답인지 반환한다."""
        return selected_answer == self.answer

    def to_dict(self) -> dict[str, Any]:
        """Quiz 객체를 JSON으로 저장할 수 있는 딕셔너리로 변환한다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Quiz:
        """딕셔너리를 검증하고 Quiz 객체로 변환한다."""
        if not isinstance(data, dict):
            raise ValueError("퀴즈 데이터가 객체가 아닙니다.")

        question = data.get("question")
        choices = data.get("choices")
        answer = data.get("answer")

        if not isinstance(question, str) or not question.strip():
            raise ValueError("문제가 올바르지 않습니다.")
        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지가 정확히 네 개가 아닙니다.")
        if not all(isinstance(choice, str) and choice.strip() for choice in choices):
            raise ValueError("선택지가 올바르지 않습니다.")
        if (
            not isinstance(answer, int)
            or isinstance(answer, bool)
            or not 1 <= answer <= 4
        ):
            raise ValueError("정답 번호가 1~4 범위가 아닙니다.")

        return cls(question, choices, answer)


class Storage:
    """퀴즈 목록과 최고 점수의 파일 저장을 담당한다."""

    def __init__(self, path: Path) -> None:
        self.path = path

    def load(self) -> tuple[list[Quiz], int | None]:
        """state.json을 읽어 퀴즈 목록과 최고 점수를 반환한다."""
        try:
            with self.path.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict) or not isinstance(data.get("quizzes"), list):
                raise ValueError("저장 데이터의 구조가 올바르지 않습니다.")

            quizzes = [Quiz.from_dict(item) for item in data["quizzes"]]
            best_score = data.get("best_score")
            if best_score is not None and (
                not isinstance(best_score, int)
                or isinstance(best_score, bool)
                or best_score < 0
            ):
                raise ValueError("최고 점수가 올바르지 않습니다.")
            return quizzes, best_score
        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈를 사용합니다.")
        except (json.JSONDecodeError, ValueError, TypeError, OSError) as error:
            print(f"저장 파일을 읽을 수 없어 기본 퀴즈를 사용합니다: {error}")

        return self.create_default_quizzes(), None

    def save(self, quizzes: list[Quiz], best_score: int | None) -> None:
        """현재 퀴즈 목록과 최고 점수를 state.json에 저장한다."""
        data = {
            "quizzes": [quiz.to_dict() for quiz in quizzes],
            "best_score": best_score,
        }
        try:
            with self.path.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
        except OSError as error:
            print(f"저장에 실패했습니다: {error}")

    def create_default_quizzes(self) -> list[Quiz]:
        """최초 실행과 파일 복구에 사용할 기본 퀴즈를 만든다."""
        return [
            Quiz(
                "사자자리의 영어 이름은 무엇일까요?",
                ["Leo", "Gemini", "Pisces", "Aries"],
                1,
            ),
            Quiz(
                "쌍둥이자리의 영어 이름은 무엇일까요?",
                ["Gemini", "Taurus", "Virgo", "Libra"],
                1,
            ),
            Quiz(
                "물고기자리의 영어 이름은 무엇일까요?",
                ["Pisces", "Cancer", "Scorpio", "Aquarius"],
                1,
            ),
            Quiz(
                "황도 12궁에서 양을 상징하는 별자리는 무엇일까요?",
                ["양자리", "염소자리", "황소자리", "천칭자리"],
                1,
            ),
            Quiz(
                "물병자리의 영어 이름은 무엇일까요?",
                ["Aquarius", "Capricorn", "Sagittarius", "Cancer"],
                1,
            ),
        ]


class QuizGame:
    """메뉴, 게임 진행과 점수 등 전체 흐름을 관리한다."""

    def __init__(
        self,
        quizzes: list[Quiz],
        best_score: int | None,
        storage: Storage,
    ) -> None:
        self.quizzes = quizzes
        self.best_score = best_score
        self.storage = storage

    def run(self) -> None:
        """종료를 선택할 때까지 메인 메뉴를 반복한다."""
        try:
            while True:
                self.show_menu()
                menu = self.read_number("메뉴를 선택하세요: ", 1, 5)
                if menu == 1:
                    self.play()
                elif menu == 2:
                    self.add_quiz()
                elif menu == 3:
                    self.show_quizzes()
                elif menu == 4:
                    self.show_best_score()
                else:
                    self.save_state()
                    print("게임을 종료합니다.")
                    break
        except (KeyboardInterrupt, EOFError):
            print("\n입력이 종료되어 게임을 종료합니다.")
            self.save_state()

    def show_menu(self) -> None:
        """사용 가능한 메뉴를 출력한다."""
        print("\n=== 별자리 퀴즈 게임 ===")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 보기")
        print("4. 최고 점수 확인")
        print("5. 종료")

    def read_number(self, prompt: str, minimum: int, maximum: int) -> int:
        """지정된 범위의 숫자가 입력될 때까지 반복한다."""
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

    def read_non_empty(self, prompt: str) -> str:
        """빈 문자열이 아닌 값이 입력될 때까지 반복한다."""
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("값을 입력해 주세요.")

    def play(self) -> None:
        """저장된 퀴즈를 차례로 출제하고 점수를 계산한다."""
        if not self.quizzes:
            print("저장된 퀴즈가 없습니다.")
            return

        score = 0
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n문제 {number}")
            quiz.display()
            selected = self.read_number("정답 번호: ", 1, 4)
            if quiz.is_correct(selected):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print(f"\n최종 점수: {score}/{len(self.quizzes)}")
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            self.save_state()
            print("최고 점수를 갱신했습니다!")

    def add_quiz(self) -> None:
        """새로운 퀴즈 한 문제를 입력받아 저장한다."""
        question = self.read_non_empty("문제를 입력하세요: ")
        choices = [
            self.read_non_empty(f"선택지 {number}: ") for number in range(1, 5)
        ]
        answer = self.read_number("정답 번호(1~4): ", 1, 4)
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_state()
        print("퀴즈가 추가되었습니다.")

    def show_quizzes(self) -> None:
        """저장된 모든 퀴즈를 보여준다."""
        if not self.quizzes:
            print("저장된 퀴즈가 없습니다.")
            return
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n{number}. {quiz.question}")
            for choice_number, choice in enumerate(quiz.choices, start=1):
                print(f"   {choice_number}. {choice}")

    def show_best_score(self) -> None:
        """현재 최고 점수를 보여준다."""
        if self.best_score is None:
            print("아직 게임을 하지 않았습니다.")
        else:
            print(f"최고 점수: {self.best_score}점")

    def save_state(self) -> None:
        """현재 게임 상태의 저장을 Storage에 요청한다."""
        self.storage.save(self.quizzes, self.best_score)


def main() -> None:
    """필요한 객체를 만들고 게임을 시작한다."""
    state_path = Path(__file__).resolve().parent / "state.json"
    storage = Storage(state_path)
    quizzes, best_score = storage.load()
    game = QuizGame(quizzes, best_score, storage)
    game.run()


if __name__ == "__main__":
    main()
