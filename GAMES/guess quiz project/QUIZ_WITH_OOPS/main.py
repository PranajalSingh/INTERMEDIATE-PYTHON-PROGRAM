from quiz_brain import quizBrain
from questions_model import Questions

question_bank = Questions.question_bank

score = 0
question_number = 1

for i in question_bank:
    ques = i["question"]
    ans = i["answer"].lower()

    print(f"\n Q.{question_number} {ques} True or False? : ", end="")
    user_ans = input().lower()

    score = quizBrain.is_correct(user_ans, ans, score)
    question_number += 1

print(f"""
you have completed the quiz.
your final score is {score} out of {len(question_bank)}.""")