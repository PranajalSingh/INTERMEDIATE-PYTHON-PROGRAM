from data import questions

class Questions:

    question_bank = []
    for i in questions["results"]:
        pairs = {}
        question_text = i["question"]
        answer_text = i["correct_answer"]
        pairs["question"] = question_text
        pairs["answer"] = answer_text
        question_bank.append(pairs)
