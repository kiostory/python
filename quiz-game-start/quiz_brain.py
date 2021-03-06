class QuizBrain:
    def __init__(self,question_bank):
        self.question_number = 0
        self.score = 0
        self.user_answer = ""
        self.question_list = question_bank

    def still_has_questions(self):  #Returin boolian (T/F)
        # if self.question_number < len(self.question_list) :
        #     return True
        # else :
        #     return False
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.question_number += 1
        self.user_answer = input(f"Q.{self.question_number}: {self.question_list[self.question_number-1].text} (True/False): ")

    # def next_question(self):
    #     current_question = self.question_list[self.question_number]
    #     self.question_number += 1
    #     input(f"Q.{self.question_number}: {current_question.text} (True/False): ")

    def check_answer(self):
        if self.question_list[self.question_number-1].answer.lower() == self.user_answer.lower():
            self.score += 1
            print("You got it right!")

        else:
            print("That's wrong!")
        print(f"The correnct correct answer was: {self.question_list[self.question_number-1].answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n\n")






