# Python Project: Student Counselling for Further Studies

def get_user_name():
    name = input("Please enter your name: ").strip()
    return name.capitalize()

def greet_user(name):
    print(f"Hello, {name}! Welcome to the Student Counselling System.")

def get_age():
    age = int(input("Please enter your age: ").strip())
    return age

def get_education():
    print("\nWhat is your highest level of education?")
    print("1. Matriculation")
    print("2. College")
    print("3. University")
    education = int(input("Please enter the number corresponding to your education level: ").strip())
    return education

def suggest_college():
    print("\nSince you've completed Matriculation, you might want to consider enrolling in a college.")
    subject = input("Have you completed Computer Science in Matric? (yes/no): ").strip().lower()
    if subject == "yes":
        suggest_computer_subjects()
    else:
        print("You can explore various subjects like Pre-Medical, Pre-Engineering, Arts, and Commerce.")

def suggest_computer_subjects():
    print("\nGreat! Here are some computer-related subjects you can pursue in college:")
    print("1. ICS (Physics)")
    print("2. ICS (Statistics)")
    print("3. ICS (Economics)")
    print("4. DAE (Computer Technology)")
    choice = int(input("Please enter the number corresponding to the subject you're interested in: ").strip())

    if choice == 1:
        print("\nICS (Physics) focuses on computer programming, mathematics, and physics.")
        suggest_institutes("ICS (Physics)")
    elif choice == 2:
        print("\nICS (Statistics) emphasizes computer science, statistics, and mathematics.")
        suggest_institutes("ICS (Statistics)")
    elif choice == 3:
        print("\nICS (Economics) involves computer science, economics, and mathematics.")
        suggest_institutes("ICS (Economics)")
    elif choice == 4:
        print("\nDAE (Computer Technology) is a diploma focused on practical skills in computer technology.")
        suggest_institutes("DAE (Computer Technology)")

def suggest_university():
    print("\nSince you've completed College, you might want to consider enrolling in a university.")
    subject = input("Did you study a specific field in college (e.g., Computer Science, Pre-Medical, etc.)? (yes/no): ").strip().lower()
    if subject == "yes":
        field = input("Please enter the field you studied in college: ").strip().lower()
        if field == "computer science":
            suggest_university_subjects()
        else:
            print(f"You can explore various university programs related to {field}.")
    else:
        print("You can explore various university programs in fields like Engineering, Medicine, Business, Arts, and Sciences.")

def suggest_university_subjects():
    print("\nGreat! Here are some computer-related programs you can pursue in university:")
    print("1. BS Computer Science")
    print("2. BS Software Engineering")
    print("3. BS Information Technology")
    print("4. BS Artificial Intelligence")
    choice = int(input("Please enter the number corresponding to the program you're interested in: ").strip())

    if choice == 1:
        print("\nBS Computer Science focuses on programming, data structures, algorithms, and software development.")
        suggest_university_institutes("BS Computer Science")
    elif choice == 2:
        print("\nBS Software Engineering emphasizes software design, project management, and quality assurance.")
        suggest_university_institutes("BS Software Engineering")
    elif choice == 3:
        print("\nBS Information Technology involves networking, databases, and IT management.")
        suggest_university_institutes("BS Information Technology")
    elif choice == 4:
        print("\nBS Artificial Intelligence is centered on AI technologies, machine learning, and data science.")
        suggest_university_institutes("BS Artificial Intelligence")

def suggest_institutes(subject):
    print(f"\nFor {subject}, here are some institutes you might consider:")
    institutes = {
        "ICS (Physics)": ["Government College", "Superior College", "Punjab College"],
        "ICS (Statistics)": ["City College", "Beaconhouse College", "The Educators College"],
        "ICS (Economics)": ["Lahore College", "Allama Iqbal College", "KIPS College"],
        "DAE (Computer Technology)": ["Polytechnic Institute", "Technical College", "Vocational Training Institute"]
    }
    
    for index, institute in enumerate(institutes[subject], start=1):
        print(f"{index}. {institute}")

    institute_choice = int(input("Please select an institute by entering the corresponding number: ").strip())
    selected_institute = institutes[subject][institute_choice - 1]
    
    show_institute_details(selected_institute)

def suggest_university_institutes(program):
    print(f"\nFor {program}, here are some universities you might consider:")
    universities = {
        "BS Computer Science": ["National University of Computer and Emerging Sciences (FAST)", "Punjab University", "Lahore University of Management Sciences (LUMS)"],
        "BS Software Engineering": ["COMSATS University", "University of Central Punjab (UCP)", "National University of Science and Technology (NUST)"],
        "BS Information Technology": ["Information Technology University (ITU)", "University of the Punjab", "Virtual University"],
        "BS Artificial Intelligence": ["FAST", "ITU", "NUST"]
    }

    for index, university in enumerate(universities[program], start=1):
        print(f"{index}. {university}")

    university_choice = int(input("Please select a university by entering the corresponding number: ").strip())
    selected_university = universities[program][university_choice - 1]
    
    show_institute_details(selected_university)

def show_institute_details(institute):
    details = {
        "Government College": "Government College offers a variety of programs with a focus on discipline and academic excellence.",
        "Superior College": "Superior College is known for its modern facilities and student-centered teaching methods.",
        "Punjab College": "Punjab College is a top choice for students seeking quality education with a strong focus on results.",
        "City College": "City College has a robust curriculum with a variety of extracurricular activities.",
        "Beaconhouse College": "Beaconhouse College provides a progressive education with an emphasis on individual growth.",
        "The Educators College": "The Educators College is well-regarded for its strong academic programs and professional faculty.",
        "Lahore College": "Lahore College offers a diverse range of courses and a vibrant campus life.",
        "Allama Iqbal College": "Allama Iqbal College focuses on holistic education with a blend of academics and values.",
        "KIPS College": "KIPS College is known for its excellent coaching and preparation for higher studies.",
        "Polytechnic Institute": "Polytechnic Institute specializes in technical education with hands-on training.",
        "Technical College": "Technical College provides practical knowledge and skills for a successful career in technology.",
        "Vocational Training Institute": "Vocational Training Institute offers specialized courses with industry-relevant training.",
        "National University of Computer and Emerging Sciences (FAST)": "FAST is a premier university for computer science with a focus on innovation and research.",
        "Punjab University": "Punjab University is one of the oldest and most prestigious universities offering a wide range of programs.",
        "Lahore University of Management Sciences (LUMS)": "LUMS is a top-ranked university known for its strong academic programs and research opportunities.",
        "COMSATS University": "COMSATS is known for its strong emphasis on science and technology education with a focus on research.",
        "University of Central Punjab (UCP)": "UCP offers a wide range of programs with a focus on student success and industry collaboration.",
        "National University of Science and Technology (NUST)": "NUST is a leading university in engineering and technology with a strong research focus.",
        "Information Technology University (ITU)": "ITU is known for its cutting-edge programs in information technology and innovation.",
        "Virtual University": "Virtual University provides flexible online education programs in various fields."
    }
    
    print(f"\n{institute} Details:")
    print(details[institute])

def say_goodbye(name):
    print(f"\nThank you, {name}, for using the Student Counselling System.")
    print("We hope you found this guidance helpful. Best of luck in your future endeavors!")
    print("Goodbye and take care!")

def main():
    name = get_user_name()
    greet_user(name)
    age = get_age()
    education = get_education()

    if education == 1:
        suggest_college()
    elif education == 2:
        suggest_university()
    elif education == 3:
        print("\nIt looks like you've already completed university! You might consider looking into professional certifications or starting your career.")
    else:
        print("\nInvalid choice. Please restart the program and select a valid education level.")

    say_goodbye(name)

if __name__ == "__main__":
    main()
