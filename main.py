from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for questions in question_data:
    question_text = questions["text"]
    question_answer = questions["answer"]
    question = Question(question_text, question_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
