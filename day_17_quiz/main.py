from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question.get("question"), question.get("correct_answer")))

print(len(question_bank))

quiz = QuizBrain(question_bank)


def ask_questions():
    while quiz.still_has_questions():
        quiz.next_question()
    retake_quiz = input("\n\nThe quiz is over. Do you want to restart it? (Yes/No): ")
    if retake_quiz == "Yes":
        quiz.score = 0
        quiz.question_number = 0
        ask_questions()
    else:
        print("\nBuh bye!")


ask_questions()
