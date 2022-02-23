from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# for i in range(0,len(question_data)):
#     new_question = Question(question_data[i]["text"], question_data[i]["answer"])
#     question_bank.append(new_question)
#
# for list in question_data:
#     question = list["text"]
#     answer = list["answer"]
#     new_list = Question(question, answer)
#     question_bank.append(new_list)

for list in question_data:
    new_list = Question(list["question"], list["correct_answer"])
    question_bank.append(new_list)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    quiz.check_answer()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")

