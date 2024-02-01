class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(
            f"Q.{self.question_number}: {current_q.text} (True/False)?: "
        )
        self.check_answer(user_input, current_q.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong...")
        print(f"The correct answer is {correct_answer}")
        print(f"your score is {self.score}/{self.question_number}")
        print("\n")
