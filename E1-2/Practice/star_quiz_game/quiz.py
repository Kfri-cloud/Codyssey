class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

        def display(self):
            print()
            print(f"문제: {self.question}")

            for number,choice in enumerate(self.choices, start=1):
                print(f"문제:{number},{choices}")

        def check_answer(self,user_answer):
            
            return self.answer == user_answer