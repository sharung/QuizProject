from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    #perulangan untuk mengambil tiap data dictionary
    question_text = question["text"]
    # mengambil data "text" dictionary
    question_answer = question["answer"]
    # mengambil data "answer" dictionary
    new_question = Question(text=question_text, answer=question_answer)
    # membuat text dan answer
    question_bank.append(new_question)
    # menyimpan pada data set question_bank
    # untuk memudahkan pemanggilan data

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You'ce completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")