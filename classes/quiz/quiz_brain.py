class QuizBrain:
    """Manages the functionality of the entire name"""

    def __init__(self, q_bank) -> None:
        self.question_number = 0
        self.question_list = q_bank
        self.points = 0

    def check_answer(self, u_answer):
        correct_answer = self.question_list[self.question_number].answer.lower(
        )
        if u_answer == correct_answer:
            print("You're right!")
            self.question_number += 1
            self.points += 1
        else:
            print("That's wrong.")
            self.question_number += 1

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.points}/{self.question_number}")

    def play(self):
        is_on = True
        while is_on:
            if self.question_number == len(self.question_list):
                print(f"Game ended, your score is: {self.points}/{self.question_number}")
                is_on = False
            else:
                answer = input(f"Q.{self.question_number + 1}  {
                               self.question_list[self.question_number].text} (True/False): ").lower()
                self.check_answer(answer)
