from question_bank import questions
ques = questions["results"]

score = 0
for i in ques:
    print(i["question"], end="True/False? : ")
    verify_inputs = True
    while verify_inputs:
        ans = input().lower()
        if ans == i["correct_answer"].lower():
            score += 1
            print(f"You got it right. \nyour current score is : {score}")
            verify_inputs = False
        elif ans == i["incorrect_answers"].lower():
            print(f"that's wrong. \nyour current score is : {score}")
            verify_inputs = False
        else:
            print("please enter either True or False : ", end="")

print(f"your final score is {score}")

