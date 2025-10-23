def quiz():
    questions=[
        {
            "question":"Which language is known as the mother of all programming language",
            "options":["A.Python","B.C","C:java","D:R"],
            "answer":"B"
        },
        {   "question": "What does CPU stands for?",
            "options":["A.Central Process Unit","B.Central personal Unit","C:Control Processing Unit","D:Central Processing unit"],
            "answer":"D"
        },
        {
            "question":"What data structure uses LIFO",
            "options":["A:Queue","B:Linked List","C:Stack","D:Tree"],
            "answer":"C"
        },
        {
            "question":"Which company developed Python",
            "options":["A:python Software Foundation","B:Google","C:Microsoft","D:Bell Labs"],
            "answer":"A"
        },
        {
            "question":"Which of the following is a valid variable name in Python?",
            "options":["A:1variable","B:variable_1","C:variable-1","D:variable_1"],
            "answer":"B"
        }
    ]
    score=0
    print("Welcome to the QuizMaster")
    print("Answer the questions by just typing A,B,C or D")
    for i,q in enumerate(questions,start=1):
        print(f'{i}:{q['question']}')
        for option in q['options']:
             print(option)
        answer=input("Your Answer").strip().upper() #here strip() can remove all the spaces
        if answer==q["answer"]:
                print("Correct")
                score+=1
        else:
             print(f"Wrong!Correct Answer:{q["answer"]}")
    total=len(questions)
    print(f'Quiz Over!You Scored:{score}/{total}')
    percentage=(score/total)*100
    print(f'your Percentage:{percentage:.2f}%')
    if percentage==100:
         print("Excellent")
    elif percentage>=60:
         print("Good Job")
    else:
        print("Keep practicing!")
        retry=input("Do you want to play again?(yes/no)").lower()
    if retry == 'yes':
                quiz()
quiz()

