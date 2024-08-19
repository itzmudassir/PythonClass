questions = [
    {"question": "What is the output of print(2 ** 3)?", "options": ["6", "8", "9", "7"], "answer": "8"},
    {"question": "Which of these is a mutable data type?", "options": ["tuple", "string", "list", "int"], "answer": "list"},
    {"question": "What does 'PEP' stand for in Python?", "options": ["Python Enhancement Proposal", "Python Execution Process", "Programming Evaluation Plan", "None of the above"], "answer": "Python Enhancement Proposal"},
    {"question": "What is the output of print('Python'[-1])?", "options": ["n", "P", "o", "h"], "answer": "n"},
    {"question": "Which of the following is a Python keyword?", "options": ["function", "while", "else", "var"], "answer": "else"},
    {"question": "What is the result of len([1, 2, 3])?", "options": ["3", "2", "1", "4"], "answer": "3"},
    {"question": "Which of these functions converts a string to an integer?", "options": ["str()", "int()", "float()", "list()"], "answer": "int()"},
    {"question": "What is the output of print(10 // 3)?", "options": ["3", "3.33", "4", "3.0"], "answer": "3"},
    {"question": "Which of these is used to define a function in Python?", "options": ["function", "def", "define", "func"], "answer": "def"},
    {"question": "What does the 'break' statement do?", "options": ["Exits the loop", "Skips the current iteration", "Stops the function", "None of the above"], "answer": "Exits the loop"},
    {"question": "What is the output of print(type([]))?", "options": ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>"], "answer": "<class 'list'>"},
    {"question": "How do you create a dictionary in Python?", "options": ["{}", "[]", "()", "<>"], "answer": "{}"},
    {"question": "Which operator is used to concatenate two strings?", "options": ["&", "+", "*", "%"], "answer": "+"},
    {"question": "What is the output of print('Hello' + ' World')?", "options": ["HelloWorld", "Hello World", "Hello+World", "None of the above"], "answer": "Hello World"},
    {"question": "How do you start a comment in Python?", "options": ["//", "/*", "#", "''"], "answer": "#"},
    {"question": "Which of these data types is not supported in Python?", "options": ["int", "float", "char", "list"], "answer": "char"},
    {"question": "What is the output of print(10 % 3)?", "options": ["1", "3", "0", "10"], "answer": "1"},
    {"question": "Which of these is not a valid variable name in Python?", "options": ["_var", "var1", "1var", "var_"], "answer": "1var"},
    {"question": "How do you create a set in Python?", "options": ["{}", "[]", "set()", "None of the above"], "answer": "set()"},
    {"question": "What is the output of print(5 == 5)?", "options": ["True", "False", "5", "None"], "answer": "True"},
    {"question": "Which of the following is used to handle exceptions in Python?", "options": ["catch", "try-except", "error", "throw"], "answer": "try-except"},
    {"question": "What does the 'continue' statement do?", "options": ["Exits the loop", "Skips the current iteration", "Stops the function", "None of the above"], "answer": "Skips the current iteration"},
    {"question": "Which of the following is a Python built-in function?", "options": ["sqrt()", "print()", "random()", "math()"], "answer": "print()"},
    {"question": "What is the output of print('5' + '3')?", "options": ["8", "53", "Error", "None"], "answer": "53"},
    {"question": "Which of these is used to install Python packages?", "options": ["pip", "npm", "composer", "bundle"], "answer": "pip"},
    {"question": "What is the output of print(len('Python'))?", "options": ["6", "5", "7", "None"], "answer": "6"},
    {"question": "Which keyword is used to define a class in Python?", "options": ["class", "def", "function", "method"], "answer": "class"},
    {"question": "What does the 'pass' statement do?", "options": ["Exits the loop", "Skips the iteration", "Does nothing", "None of the above"], "answer": "Does nothing"},
    {"question": "Which of the following methods is used to remove whitespace from a string?", "options": ["strip()", "trim()", "remove()", "clean()"], "answer": "strip()"},
    {"question": "What is the result of 10 / 2 in Python?", "options": ["5", "5.0", "4", "None"], "answer": "5.0"}
]

# Initialize the score
score = 0

# Ask the questions
for q in questions:
    print("\n" + q["question"])
    for i, option in enumerate(q["options"], start=1):
        print(f"{i}. {option}")
    
    answer = input("Enter the number of your answer: ").strip()
    
    # Check if the answer is correct
    if q["options"][int(answer) - 1] == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {q['answer']}.")

# Display the final score
print(f"\nYour final score is {score} out of {len(questions)}.")
