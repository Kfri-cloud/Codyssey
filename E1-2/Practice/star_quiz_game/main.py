from quiz_game import QuizGame
from untils import get_number

def main():
    game = QuizGame()
    game.register_default_quizzes()

    while True:
        game.show_menu()
        choice = get_number("메뉴를 선택하세요.",1,5)

        if choice == 1:
            game.play_quiz()
        elif choice == 2:
            game.add_quiz()
        elif choice == 3:
            game.show_quiz_list()
        elif choice == 4:
            game.show_score()
        elif choice == 5:
            game.show_exit_screen()
            break

if __name__ == "__main__":
    main()
