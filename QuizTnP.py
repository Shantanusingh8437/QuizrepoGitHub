import random
python_questions = [
    {"question": "What is the output of print(5*4)?", "options": ["20", "45", "52"], "answer": "20"},
    {"question": "Which keyword is used for function in Python?", "options": ["func", "define", "def"],
     "answer": "def"},
    {"question": "What is the correct way to declare a variable?", "options": ["int x = 10", "x = 10", "var x = 10"],
     "answer": "x = 10"},
    {"question": "Who developed Python Programming Language?", "options": ["Bjarne Stroustrup", "Rasmus Lerdorf", "Guido van Rossum"],
     "answer": "Guido van Rossum"},
    {"question": "Which type of Programming does Python support?", "options": ["structured programming", "Dynamic programming"],
     "answer": "structured programming"},
    {"question": "Which of the following is the correct extension of the Python file?", "options": [" .python", ".py", ".p"], "answer": ".py"},
    {"question": "Is Python code compiled or interpreted?", "options": ["Python code is both compiled and interpreted", "Python code is neither compiled nor interpreted", "Python code is only compiled"], "answer": "Python code is both compiled and interpreted"},
    {"question": "All keywords in Python are in ___", "options": ["Capitalized", "UPPER CASE", "none"], "answer": "none"},
    {"question": "Which of the following is used to define a block of code in Python language?", "options": ["Indentation", "key", "brackets"], "answer": "Indentation"},
    {"question": "Which of the following character is used to give single-line comments in Python?", "options": ["//", "/*", "#"], "answer": "#"},
    {"question": "What does pip stand for python?", "options": ["Pip Installs Python", "Pip Installs Packages", "Preferred Installer Program"], "answer": "Preferred Installer Program"},
    {"question": "Which of the following is not a core data type in Python programming?", "options": ["Tuples", "Lists", "Class"], "answer": "Class"},
]

java_questions = [
    {"question": "Which of the following is NOT a keyword in Java?", "options": ["try","finally","final","throws","None of the above"],
     "answer": "None of the above"},
    {"question": "Which of the following correctly describes the Java Memory Model?", "options": ["The memory is divided into heap and stack only", "The memory includes heap, stack, method area, and garbage collection", "The memory is managed manually by the programmer"], "answer": "The memory includes heap, stack, method area, and garbage collection"},
    {"question": "What is used to compile Java code?", "options": ["gcc", "javac", "python"], "answer": "javac"},
    {"question": "Which keyword is used for inheritance in Java?", "options": ["extends", "inherits", "implements"], "answer": "extends"},
    {"question": "Which package is automatically imported in all Java programs?", "options": ["java.io", "java.util", "java.lang"], "answer": "java.lang"},
    {"question": "Which data type is used to create a variable that stores text?", "options": ["String", "char", "int"], "answer": "String"},
    {"question": "How do you create an object of a class in Java?", "options": ["new Object()", "Object obj = new Object()", "create Object()"], "answer": "Object obj = new Object()"},
    {"question": "Which of these is not a Java access modifier?", "options": ["private", "public", "internal"], "answer": "internal"},

]

aptitude_questions = [
    {"question": "The angle of elevation of a ladder leaning against a wall is 60° and the foot of the ladder is 4.6 m away from the wall. The length of the ladder is:", "options": ["2.3", "4.6", "9.8"], "answer": "9.8"},
    {"question": "Find the next number in the sequence: 2, 4, 8, 16, ?", "options": ["35", "32", "40"], "answer": "32"},
    {"question": "If a car travels at 60 km/h, how long will it take to travel 180 km?",
     "options": ["5 hours", "3 hours", "7 hours"], "answer": "3 hours"},
    {"question": "What is 15% of 200?", "options": ["50", "30", "60"], "answer": "30"},
    {"question": "Find the next number in the sequence: 2, 4, 8, 16, ?", "options": ["34", "32", "39"], "answer": "32"},
    {"question": "If a car travels at 60 km/h, how long will it take to travel 180 km?",
     "options": ["4 hours", "3 hours", "6 hours"], "answer": "3 hours"},
    {"question": "If 12 men can complete a task in 8 days, how many days will 6 men take to complete the same task?",
     "options": ["16 days", "18 days", "19 days"], "answer": "16 days"},
    {"question": "What is the average of the first five prime numbers?", "options": ["5.6", "8.6", "7.6"],
     "answer": "5.6"},
      
]

users_db = {}
def register():
    print("\n--- Registration ---")
    username = input("Enter a new username: ")
    if username in users_db:
        print("Username already exists. Try logging in or choose another username.")
    else:
        password = input("Enter a new password: ")
        users_db[username] = password
        print("Registration successful!")
def login():
    print("\n--- Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users_db and users_db[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False
def choose_quiz():
    print("\n--- Choose Quiz ---")
    print("1. Python")
    print("2. Java")
    print("3. Aptitude")

    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        return python_questions
    elif choice == '2':
        return java_questions
    elif choice == '3':
        return aptitude_questions
    else:
        print("Invalid choice. Please select again.")
        return choose_quiz()
def conduct_quiz(questions):
    print("\n--- Quiz Started ---")
    selected_questions = random.sample(questions, 10)
    score = 0

    index = 1
    for i in selected_questions:
        print(f"\nQ{index}. {i['question']}")

        option_index = 1
        for option in i['options']:
            print(f"{option_index}. {option}")
            option_index += 1

        answer = input("Enter your answer (1/2/3): ")
        if i['options'][int(answer) - 1] == i['answer']:
            score += 1
        index += 1

    print(f"\nQuiz Completed! Your score is {score}/10.")
    return score
def main():
    while True:
        print("\n--- Welcome to the Quiz App ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        option = input("Enter your choice: ")

        if option == '1':
            register()
        elif option == '2':
            if login():
                while True:
                    questions = choose_quiz()
                    conduct_quiz(questions)
                    again = input("\nDo you want to attempt again? (yes/no): ")
                    if again.lower() != 'yes':
                        break
            else:
                print("Login failed. Try again.")
        elif option == '3':
            print("Exiting the quiz app. Goodbye!")
            break
        else:
            print("Invalid option. Please select again.")
if __name__ == "__main__":
    main()