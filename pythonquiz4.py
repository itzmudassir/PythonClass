import time

# Python quiz questions
python_questions = [
    {"question": "What will set([1, 2, 2, 3]) return?", "options": ["{1, 2, 3}", "[1, 2, 2, 3]", "{1, 2, 2, 3}", "[1, 2, 3]"], "answer": "{1, 2, 3}"},
    {"question": "What will happen if you use list.remove(x) and x is not in the list?", "options": ["It will remove the first element.", "It will remove the last element.", "It will raise a ValueError.", "It will do nothing."], "answer": "It will raise a ValueError."},
    {"question": "Which of the following methods creates a shallow copy of a list?", "options": ["list.copy()", "list[:]", "list.copy[]", "list.shallow()"], "answer": "list.copy()"},
    {"question": "What is the output of print(2 ** 3 ** 2)?", "options": ["512", "64", "16", "8"], "answer": "512"},
    {"question": "Which of these is the correct syntax to create a generator in Python?", "options": ["def func(): yield", "def func() return", "def func() next", "def func() generator"], "answer": "def func(): yield"},
    {"question": "Which built-in function returns the length of an object?", "options": ["size()", "count()", "length()", "len()"], "answer": "len()"},
    {"question": "What is the output of 'Hello World'.replace('World', 'Python')?", "options": ["Hello Python", "World Python", "Hello", "Python Hello"], "answer": "Hello Python"},
    {"question": "Which keyword is used to handle exceptions in Python?", "options": ["try", "catch", "throw", "except"], "answer": "try"},
    {"question": "What will be the output of [1, 2, 3] + [4, 5]?", "options": ["[1, 2, 3, 4, 5]", "[5, 6]", "[1, 2, 3]", "[4, 5]"], "answer": "[1, 2, 3, 4, 5]"},
    {"question": "What does the 'in' keyword do in Python?", "options": ["Checks if a value exists in a sequence", "Assigns a value", "Deletes a value", "Inserts a value"], "answer": "Checks if a value exists in a sequence"},
    {"question": "Which method is used to sort elements in Python?", "options": ["sort()", "arrange()", "order()", "sorted()"], "answer": "sorted()"},
    {"question": "What will print(type(10)) return?", "options": ["<class 'integer'>", "<class 'int'>", "<type 'int'>", "<type 'integer'>"], "answer": "<class 'int'>"},
    {"question": "What does the split() method return?", "options": ["List", "Tuple", "String", "Dictionary"], "answer": "List"},
    {"question": "How do you access a dictionary value by its key?", "options": ["dict[key]", "dict.value(key)", "dict.get(value)", "dict.access[key]"], "answer": "dict[key]"},
    {"question": "Which Python module is used to generate random numbers?", "options": ["random", "math", "datetime", "statistics"], "answer": "random"},
    {"question": "What does the 'pass' keyword do in Python?", "options": ["Does nothing", "Terminates the program", "Skips the next line", "Re-raises an exception"], "answer": "Does nothing"},
    {"question": "How do you remove duplicates from a list?", "options": ["Convert to a set", "Use list.remove()", "Use list.filter()", "Use a for loop"], "answer": "Convert to a set"},
    {"question": "Which of these methods converts a string to all lowercase?", "options": ["lower()", "str.lowercase()", "downcase()", "str.down()"], "answer": "lower()"},
    {"question": "What is the output of [x for x in range(3)]?", "options": ["[0, 1, 2]", "[1, 2, 3]", "[3, 2, 1]", "[None]"], "answer": "[0, 1, 2]"},
    {"question": "What is the time complexity of accessing an element in a list by index?", "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"], "answer": "O(1)"},
    {"question": "What function is used to get user input in Python?", "options": ["input()", "get()", "read()", "ask()"], "answer": "input()"},
    {"question": "What is the output of print(10 / 3)?", "options": ["3.333333333", "3", "3.0", "None"], "answer": "3.333333333"},
    {"question": "Which of the following is a valid Python variable name?", "options": ["_myVar", "2ndVar", "class", "-myVar"], "answer": "_myVar"},
    {"question": "What does the range(5) return?", "options": ["range(0, 5)", "[0, 1, 2, 3, 4]", "[5]", "An empty range"], "answer": "range(0, 5)"},
    {"question": "Which data type is immutable in Python?", "options": ["Tuple", "List", "Dictionary", "Set"], "answer": "Tuple"},
    {"question": "What is the output of 'abc' + 'def'?", "options": ["abcdef", "abc def", "abc+def", "None"], "answer": "abcdef"},
    {"question": "How do you check if a file exists in Python?", "options": ["os.path.exists()", "file.check()", "file.exists()", "file.find()"], "answer": "os.path.exists()"},
    {"question": "What will be the result of len([])?", "options": ["0", "None", "Error", "1"], "answer": "0"},
    {"question": "What is the method used to convert an object into a string in Python?", "options": ["str()", "stringify()", "toString()", "convert()"], "answer": "str()"},
    {"question": "How do you catch exceptions in Python?", "options": ["try...except", "catch...try", "if...else", "raise...catch"], "answer": "try...except"}
]

# Python quiz game
def python_quiz():
    score = 0
    for q in python_questions:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")
        while True:
            answer = input("Enter the number of your answer: ").strip()
            if answer.isdigit() and 1 <= int(answer) <= len(q["options"]):
                if q["options"][int(answer) - 1] == q["answer"]:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Incorrect. The correct answer is {q['answer']}.")
                break
            else:
                print("Invalid input, please choose a valid option.")

    print(f"\nYour final score is {score} out of {len(python_questions)}.")
    input("Press Enter to exit...")  # Keep the console open

python_quiz()
