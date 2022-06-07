import database


MENU_PROMPT = """ _-_-_- WELCOME -_-_-_
Please choose an option:

1) Let's test your knowledge!
2) All questions.
3) Exit.


Your select:"""

# MENU
def menu():
    connection = database.connect()
    database.create_table(connection)

    while (user_input := int(input(MENU_PROMPT))) != 3:
        try:
            user_input = int(user_input)
        except ValueError:
            print("Invalid input!")
            continue
        if user_input == 1:
            prompt_random_questions(connection)
        elif user_input == 2:
            print("\n\n")
            prompt_show_all(connection)
            print("\n\n")


# Function for show all questions in Database
def prompt_show_all(connection):
    questions = database.show_all(connection)

    for question in questions:
        print(f"{question[0]})  {question[1]}")


# Takes questions from database and gives to each user one by one, calculates average ball, count of correct and wrong answers
def prompt_random_questions(connection):
    sum = 0
    wrong_answers = 0
    correct_answers = 0
    questions = database.random(connection)

    for question in questions:
        print(f"{question[0]})  {question[1]}")
        print()
        print(f"A) {question[2]}, B) {question[3]}, C) {question[4]}")
        print()

        answer = input(f"Your choice for {question[0]}th question: ")
        try:
            if answer == "a" or answer == "b" or answer == "c":
                continue
            else:
                print("\n\nInvalid input!")
                break
        except ValueError:
            print("Invalid input!")
        res = " ".join(question[5].split())
        if answer == res:
            correct_answers += 1
            sum += 20
        else:
            wrong_answers += 1

    print(f"\n[Correct answers] - {correct_answers}")
    print(f"\n[Wrong answers] - {wrong_answers}")
    if sum >= 80:
        print(f"\nYour ball is: {sum}. You passed the exam!")
        print("\n\n")
    else:
        print(f"\nYour ball is {sum}.You failed the exam!")
        print("\n\n")


menu()
