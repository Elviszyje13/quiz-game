from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

qb = QuizBrain(question_bank)

while qb.still_has_question():
    user_answer = qb.next_question()
    qb.check_answer(user_answer)

print(f"Your score is {qb.score}")
