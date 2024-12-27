class quizBrain:

    @staticmethod
    def is_correct(user_answer, answer, score):
        while user_answer != "true" and user_answer != "false":
            print("invalid input, please enter either true or false. : ", end="")
            user_answer = input()
        if user_answer == answer:
            score += 1
            print(f"correct answer, your current score is {score}.")
        else:
            print(f"oops that's wrong, your current score is {score}.")
        return score


