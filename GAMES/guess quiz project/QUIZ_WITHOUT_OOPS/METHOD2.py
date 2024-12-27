import random
from question_bank import questions

ques = questions["results"]
score = 0

shuffle_ques = []
for i in range(0,len(ques)):
    shuffle_ques.append(i)
print(shuffle_ques)

while shuffle_ques:
    current_ques_index = random.choice(shuffle_ques)
    shuffle_ques.remove(current_ques_index)

    print(f"Q.{10-len(shuffle_ques)}: {ques[current_ques_index]["question"]}", end=" True/False? : ")
    ans = input().lower()

    if ans == ques[current_ques_index]["correct_answer"].lower():
        score += 1
        print(f"You got it right. \nyour current score is : {score}")
        verify_inputs = False
    elif ans == ques[current_ques_index]["incorrect_answers"].lower():
        print(f"that's wrong. \nyour current score is : {score}")
        verify_inputs = False
    else:
        print("please enter either True or False : ", end="")

print(f"your final score is {score}")
