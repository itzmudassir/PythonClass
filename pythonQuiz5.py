import random
import time

# List of 30 tricky Python questions and answers
questions = [
    {
        "question": """What is the output of the following code?
        x = [1, 2, 3]
        y = x
        y.append(4)
        print(x)""",
        "options": ["[1, 2, 3]", "[1, 2, 3, 4]", "None", "Error"],
        "answer": "[1, 2, 3, 4]"
    },
    {
        "question": """What does this code output?
        def func(x=[]):
            x.append(1)
            return x
        print(func())
        print(func())""",
        "options": ["[1] [1]", "[1] [1, 1]", "[1, 1] [1, 1]", "Error"],
        "answer": "[1] [1, 1]"
    },
    {
        "question": """What is the output of the following code?
        def func(a, b=[]):
            b.append(a)
            return b
        print(func(1))
        print(func(2))""",
        "options": ["[1] [2]", "[1] [1, 2]", "[2] [1, 2]", "None"],
        "answer": "[1] [1, 2]"
    },
    {
        "question": """What does this code print?
        print([i for i in range(5) if i % 2 == 0])""",
        "options": ["[0, 2, 4]", "[1, 3]", "Error", "None"],
        "answer": "[0, 2, 4]"
    },
    {
        "question": """What will be the output?
        x = {1, 2, 3}
        y = {3, 4, 5}
        print(x & y)""",
        "options": ["{3}", "{1, 2, 3, 4, 5}", "Error", "None"],
        "answer": "{3}"
    },
    {
        "question": """What does the following code return?
        def add(x, y=[]):
            y.append(x)
            return y
        print(add(1))
        print(add(2))""",
        "options": ["[1] [2]", "[1] [1, 2]", "[2] [1, 2]", "None"],
        "answer": "[1] [1, 2]"
    },
    {
        "question": """Which method is used to create an iterator object in Python?""",
        "options": ["__iter__", "__next__", "__init__", "None of these"],
        "answer": "__iter__"
    },
    {
        "question": """What is the output of the following code?
        a = (1, 2, 3)
        b = (4, 5)
        c = a + b
        print(c)""",
        "options": ["(1, 2, 3, 4, 5)", "TypeError", "(4, 5, 1, 2, 3)", "None"],
        "answer": "(1, 2, 3, 4, 5)"
    },
    {
        "question": """What is the output of this code?
        d = {'a': 1, 'b': 2}
        d['c'] = d.get('a') + d.get('b')
        print(d)""",
        "options": ["{'a': 1, 'b': 2, 'c': 3}", "{'a': 1, 'b': 2, 'c': None}", "Error", "None"],
        "answer": "{'a': 1, 'b': 2, 'c': 3}"
    },
    {
        "question": """What is the output of this code?
        nums = [1, 2, 3]
        print(nums[::-1])""",
        "options": ["[3, 2, 1]", "[1, 2, 3]", "None", "Error"],
        "answer": "[3, 2, 1]"
    },
    {
        "question": """Which of these is a correct syntax for list comprehension?
        """,
        "options": ["[x for x in range(10)]", "for x in range(10) yield x", "map(x for x in range(10))", "None"],
        "answer": "[x for x in range(10)]"
    },
    {
        "question": """What does the following code print?
        a = 10
        b = 5
        print(a // b)""",
        "options": ["2", "2.0", "None", "Error"],
        "answer": "2"
    },
    {
        "question": """Which of these will throw an error?
        """,
        "options": ["float('inf')", "int('10')", "float('abc')", "str(10)"],
        "answer": "float('abc')"
    },
    {
        "question": """What is the output?
        def foo(bar, baz=[]):
            baz.append(bar)
            return baz
        print(foo(10))
        print(foo(20))""",
        "options": ["[10] [20]", "[10] [10, 20]", "[20] [10, 20]", "None"],
        "answer": "[10] [10, 20]"
    },
    {
        "question": """What is the output of the following code?
        def factorial(n):
            return 1 if n == 0 else n * factorial(n - 1)
        print(factorial(5))""",
        "options": ["120", "24", "5", "None"],
        "answer": "120"
    },
    {
        "question": """What is the output of this code?
        x = [i for i in range(5)]
        print(x)""",
        "options": ["[0, 1, 2, 3, 4]", "[1, 2, 3, 4]", "None", "Error"],
        "answer": "[0, 1, 2, 3, 4]"
    },
    {
        "question": """What is the output of the following code?
        x = ['a', 'b', 'c']
        y = ''.join(x)
        print(y)""",
        "options": ["abc", "['a', 'b', 'c']", "a, b, c", "Error"],
        "answer": "abc"
    },
    {
        "question": """What is the result of the following code?
        a = [1, 2, 3]
        a.insert(1, 4)
        print(a)""",
        "options": ["[1, 4, 2, 3]", "[1, 2, 3]", "Error", "[1, 2, 3, 4]"],
        "answer": "[1, 4, 2, 3]"
    },
    {
        "question": """Which of these is a mutable data type in Python?""",
        "options": ["List", "Tuple", "String", "None"],
        "answer": "List"
    },
    {
        "question": """What is the output of this code?
        a = [1, 2, 3]
        b = a[:]
        b[0] = 4
        print(a)""",
        "options": ["[1, 2, 3]", "[4, 2, 3]", "None", "Error"],
        "answer": "[1, 2, 3]"
    },
    {
        "question": """What is the result of the following expression?
        10**2""",
        "options": ["100", "20", "2", "None"],
        "answer": "100"
    },
    {
        "question": """What is the result of this code?
        print((2, 3) * 2)""",
        "options": ["(2, 3, 2, 3)", "(2, 3)", "(4, 6)", "Error"],
        "answer": "(2, 3, 2, 3)"
    },
    {
        "question": """What is the output of this code?
        def foo(x):
            return x ** x
        print(foo(3))""",
        "options": ["27", "9", "81", "None"],
        "answer": "27"
    },
    {
        "question": """What is the output of the following code?
        print(check()(5))""",
        "options": ["15", "10", "5", "None"],
        "answer": "15"
    },
    {
        "question": """What is the output of this code?
        print(sorted([3, 1, 4, 1, 5, 9], reverse=True))""",
        "options": ["[9, 5, 4, 3, 1, 1]", "[1, 1, 3, 4, 5, 9]", "Error", "None"],
        "answer": "[9, 5, 4, 3, 1, 1]"
    },
    {
        "question": """What will be the output of the following code?
        x = 'hello'
        print(x[1:4])""",
        "options": ["'ell'", "'ell'", "'he'", "Error"],
        "answer": "'ell'"
    },
    {
        "question": """What is the result of the following code?
        a = {'a': 1, 'b': 2}
        b = a.get('c', 3)
        print(b)""",
        "options": ["3", "None", "Error", "2"],
        "answer": "3"
    },
    {
        "question": """What will the following code output?
        s = 'hello world'
        print(s.upper())""",
        "options": ["'HELLO WORLD'", "'hello world'", "Error", "None"],
        "answer": "'HELLO WORLD'"
    },
    {
        "question": """What is the output of this code?
        lst = [i ** 2 for i in range(3)]
        print(lst)""",
        "options": ["[0, 1, 4]", "[1, 4, 9]", "[0, 1, 9]", "None"],
        "answer": "[0, 1, 4]"
    },
    {
        "question": """What does this code output?
        x = [1, 2, 3]
        y = x.copy()
        y.append(4)
        print(x)""",
        "options": ["[1, 2, 3]", "[1, 2, 3, 4]", "Error", "None"],
        "answer": "[1, 2, 3]"
    },
    {
        "question": """What is the output of this code?
        def func(x, y=1):
            return x + y
        print(func(2))""",
        "options": ["3", "2", "1", "Error"],
        "answer": "3"
    },
    {
        "question": """What does this code print?
        a = 'Python'
        print(a[::-1])""",
        "options": ["'nohtyP'", "'Python'", "Error", "None"],
        "answer": "'nohtyP'"
    },
    {
        "question": """What is the result of this code?
        x = [i for i in range(3)]
        print(x[1:2])""",
        "options": ["[1]", "[1, 2]", "[0, 1]", "None"],
        "answer": "[1]"
    },
    {
        "question": """What will be the result of this code?
        lst = [1, 2, 3]
        lst.remove(2)
        print(lst)""",
        "options": ["[1, 3]", "[1, 2, 3]", "Error", "None"],
        "answer": "[1, 3]"
    },
    {
        "question": """What is the output of this code?
        def func(a, b=10):
            return a * b
        print(func(5))""",
        "options": ["50", "5", "10", "Error"],
        "answer": "50"
    },
    {
        "question": """What does the following code return?
        x = set([1, 2, 2, 3])
        print(x)""",
        "options": ["{1, 2, 3}", "{1, 2, 2, 3}", "None", "Error"],
        "answer": "{1, 2, 3}"
    },
    {
        "question": """What is the output of this code?
        s = '123'
        print(int(s))""",
        "options": ["123", "'123'", "Error", "None"],
        "answer": "123"
    },
    {
        "question": """What will the following code print?
        def foo(a, b=2):
            return a / b
        print(foo(6))""",
        "options": ["3.0", "6", "2", "Error"],
        "answer": "3.0"
    }
]

# Shuffle the questions to ensure different order each time
random.shuffle(questions)


# Function to conduct the quiz
def conduct_quiz():
    score = 0
    total_questions = len(questions)
    
    for q in questions:
        print(q["question"])
        print("Options:")
        options = q["options"]
        random.shuffle(options)  # Shuffle options so that the correct answer isn't always in the same position
        
        # Print options with numbers
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")
        
        # Validate user input
        while True:
            try:
                user_answer = int(input("Choose the option number: ").strip())
                if 1 <= user_answer <= len(options):
                    break  # Exit loop if valid option is entered
                else:
                    print(f"Invalid option. Please enter a number between 1 and {len(options)}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Determine the correct option
        correct_option = q["options"].index(q["answer"]) + 1
        
        # Check the user's answer
        if user_answer == correct_option:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['answer']}")
        
        print()

    # Save results to a file
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("quiz_results.txt", "a") as file:
        file.write(f"Quiz taken at: {timestamp}\n")
        file.write(f"Score: {score}/{total_questions} ({(score / total_questions) * 100:.2f}%)\n\n")

    print(f"Quiz completed. Your score is: {score}/{total_questions} ({(score / total_questions) * 100:.2f}%)")


# Run the quiz
conduct_quiz()
input("Press Enter to exit...")  # Keep the console open