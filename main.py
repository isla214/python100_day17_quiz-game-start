from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
     queation_text = question["question"]
     question_answer = question["correct_answer"]
     new_q = Question(queation_text, question_answer)
     question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
     quiz.next_question()

