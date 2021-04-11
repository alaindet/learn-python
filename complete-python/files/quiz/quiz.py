def quiz():
    quizzes_content = ''
    with open('questions.txt', 'r') as file:
        quizzes_content = file.read()

    correct_answers = 0
    answers = 0

    for line in quizzes_content.split('\n')[:-1]:
        question, answer = line.split('=')
        user_answer = input(f'{question}=')
        answers += 1
        if user_answer == answer:
            correct_answers += 1
    
    score = 100 * (float(correct_answers) / float(answers))
    print(f'Your final score is {correct_answers}/{answers} ({score}%)')

quiz()
