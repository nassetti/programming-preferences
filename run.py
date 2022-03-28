# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDENTIALS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDENTIALS = CREDENTIALS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDENTIALS)
SHEET = GSPREAD_CLIENT.open("programming_preferences")
CHOICES_INDUSTRY = [
    "Technology / Development", "Healthcare",
    "Operations / Logistics", "Human Resources",
    "Financial Services / Banking", "Academia", "Law", "Other"
    ]
CHOICES_LANGUAGE = [
    "I do not know any", "Python", "JavaScript",
    "C", "Java", "VBA", "SQL", "Swift", "Ruby", "Other"
    ]
CHOICES_LENGTH = [
    "0 Years - I don't program", "0-1 Years",
    "1-2 Years", "2-5 Years", "5-10 Years", "10+ Years"
]
CHOICES_LANGUAGE_NUM = [
    "0 Languages", "1 Language", "2 Languages",
    "3 Languages", "4 Languages",
    "5 Languages", "6+ Languages"
]
responses_sheet = SHEET.worksheet("responses")

all_data = responses_sheet.get_all_values()

# print(all_data)


def user_input():
    """Allows user to input survey answers"""
    print("Hello, welcome to the 'Programming Preferences' Survey")
    # q1
    question_one()
    # q2
    question_two()
    # q3
    question_three()
    # q4
    question_four()
    # q5
    question_five()
    # q6
    question_six()
    # print results
    results()
    # check if the user is happy with responses.
    answer_check()
    # assemble correct answers into array
    user_responses = [
        name,
        email,
        CHOICES_INDUSTRY[int(industry_choice) - 1],
        CHOICES_LANGUAGE[int(favourite_language) - 1],
        CHOICES_LENGTH[int(years_programming) - 1],
        CHOICES_LANGUAGE_NUM[int(num_languages) - 1]
    ]
    # add responses to datasheet
    add_to_sheet(user_responses)


def question_one():
    """Code for question one."""
    global name
    name = str(input("1. Please input your name: \n"))
    print(f"\t'{name}' - Is that correct? \n")
    correct_name = str(input("\tType 'Y' for yes or 'N' for no \n")).upper()
    while correct_name != "Y":
        if correct_name == "Y":
            print("\tGreat! Next question... \n")
        elif correct_name == "N":
            print("\tPlease input your name again: \n")
            name = str(input("\n"))
            print(f"\t'{name}' - Is that correct? \n")
            correct_name = str(input("\t Type 'Y' for yes or 'N' for no: \n"))
            correct_name = correct_name.upper()
        else:
            print("\tDid you type 'Y' for yes and 'N' for no? \n")
            print(f"{name} \n")
            correct_name = str(input("\tIs the name above correct? \n"))
            correct_name = correct_name.upper()


def question_two():
    """Code for question two."""
    global email
    email = str(input("2. Please input your email: \n"))
    print(f"\tYou have entered '{email}'. Is that correct? \n")
    correct_email = str(input("\tType 'Y' for yes or 'N' for no: \n")).upper()
    while correct_email != "Y":
        if correct_email == "Y":
            print("\tGreat! Next question. \n")
        elif correct_email == "N":
            print("\tPlease input your email again: \n")
            email = str(input("\n"))
            print(f"\t'{email}' - Is that correct? \n")
            correct_email = str(input("\tType 'Y' for yes or 'N' for no: \n"))
            correct_email = correct_email.upper()
        else:
            print("\tAre you sure you typed 'Y for yes and 'N' for no? \n")
            print(email)
            correct_email = str(input("\n \tIs the email above correct? \n"))
            correct_email = correct_email.upper()


def question_three():
    """Code for question three."""
    print("3. What industry do you work in?")
    print("\tPlease select from the choices below.")
    print("\tTo make a selection, please type the number of your selection.\n")
    for i in range(len(CHOICES_INDUSTRY)):
        print(f"\t{i + 1}: {CHOICES_INDUSTRY[i]}")
    global industry_choice
    industry_choice = str(input("\n"))
    print(f"\tYou have selected '{CHOICES_INDUSTRY[int(industry_choice)-1]}'. Is that correct? \n")
    correct_industry = str(input("\tType 'Y' for yes or 'N' for no: \n"))
    correct_industry = correct_industry.upper()
    while correct_industry != "Y":
        if correct_industry == "Y":
            print("\tGreat! Next question. \n")
        elif correct_industry == "N":
            print("\tPlease input your selection again: \n")
            industry_choice = str(input("\n"))
            print(f"\t'{CHOICES_INDUSTRY[int(industry_choice)-1]}' - Is that correct? \n")
            correct_industry = str(input("\tType 'Y' for yes or 'N' for no: \n")).upper()
        else:
            print("\tAre you sure you typed 'Y for yes and 'N' for no? \n")
            print(CHOICES_INDUSTRY[int(industry_choice)-1])
            correct_industry = str(input("\n \tIs the selection above correct? \n")).upper()


def question_four():
    """Code for question four."""
    print("4. What is your favourite programming language?")
    print("\tPlease select from the choices below.")
    print("\tTo make a selection, please type the number of your selection. \n")
    for i in range(len(CHOICES_LANGUAGE)):
        print(f"\t{i + 1}: {CHOICES_LANGUAGE[i]}")
    global favourite_language
    favourite_language = str(input("\n"))
    print(f"\tYou have selected '{CHOICES_LANGUAGE[int(favourite_language)-1]}'. Is that correct? \n")
    correct_language = str(input("\tType 'Y' for yes or 'N' for no: \n")).upper()
    while correct_language != "Y":
        if correct_language == "Y":
            print("\tGreat! Next question. \n")
        elif correct_language == "N":
            print("\tPlease input your selection again: \n")
            favourite_language = str(input("\n"))
            print(f"\t'{CHOICES_LANGUAGE[int(favourite_language)-1]}' - Is that correct? \n")
            correct_language = str(input("\tType 'Y' for yes or 'N' for no: \n")).upper()
        else:
            print("\tAre you sure you typed 'Y for yes and 'N' for no? \n")
            print(CHOICES_LANGUAGE[int(favourite_language)-1])
            correct_language = str(input("\n \tIs the selection above correct? \n")).upper()


def question_five():
    """Code for question five."""
    print("5. How long have you been programming?")
    print("\tPlease select from the choices below.")
    print("\tTo make a selection, please type the number of your selection. \n")
    for i in range(len(CHOICES_LENGTH)):
        print(f"\t{i + 1}: {CHOICES_LENGTH[i]}")
    global years_programming
    years_programming = str(input("\n"))
    print(f"\tYou have selected '{CHOICES_LENGTH[int(years_programming)-1]}'. Is that correct? \n")
    correct_years = str(input("\tType 'Y' for yes or 'N' for no: \n")).upper()
    while correct_years != "Y":
        if correct_years == "Y":
            print("\tGreat! Next question. \n")
        elif correct_years == "N":
            print("\tPlease input your selection again: \n")
            years_programming = str(input("\n"))
            print(f"\t'{CHOICES_LENGTH[int(years_programming)-1]}' - Is that correct? \n")
            correct_years = str(input("\tType 'Y' for yes or 'N' for no: \n")).upper()
        else:
            print("\tAre you sure you typed 'Y for yes and 'N' for no? \n")
            print(CHOICES_LENGTH[int(years_programming)-1])
            correct_years = str(input("\n \tIs the selection above correct? \n")).upper()


def question_six():
    """Code for question six."""
    print("6. How many programming languages do you know?")
    print("\tPlease select from the choices below.")
    print("\tTo make a selection, please type the number of your selection. \n")
    for i in range(len(CHOICES_LANGUAGE_NUM)):
        print(f"\t{i + 1}: {CHOICES_LANGUAGE_NUM[i]}")
    global num_languages
    num_languages = str(input("\n"))
    print(f"\tYou have selected '{CHOICES_LANGUAGE_NUM[int(num_languages)-1]}'. Is that correct? \n")
    correct_num = str(input("\tType 'Y' for yes or 'N' for no: \n")).upper()
    while correct_num != "Y":
        if correct_num == "Y":
            print("\tGreat! Next question. \n")
        elif correct_num == "N":
            print("\tPlease input your selection again: \n")
            num_languages = str(input("\n"))
            print(f"\t'{CHOICES_LANGUAGE_NUM[int(num_languages)-1]}' - Is that correct? \n")
            correct_num = str(input("\tType 'Y' for yes or 'N' for no: \n")).upper()
        else:
            print("\tAre you sure you typed 'Y for yes and 'N' for no? \n")
            print(CHOICES_LANGUAGE_NUM[int(num_languages)-1])
            correct_num = str(input("\n \tIs the selection above correct? \n")).upper()


def results():
    """Prints survey responses."""
    print("Please find your responses below:")
    print("1. What is your name?\n")
    print(f"\t {name} \n")
    print("2. What is your email?\n")
    print(f"\t {email}")
    print("3. What industry do you work in?\n")
    print(f"\t {CHOICES_INDUSTRY[int(industry_choice) - 1]}")
    print("4. What is your favourite programming language?\n")
    print(f"\t {CHOICES_LANGUAGE[int(favourite_language) - 1]}")
    print("5. How long have you been programming?\n")
    print(f"\t {CHOICES_LENGTH[int(years_programming) - 1]}")
    print("6. How many programming languages do you know?\n")
    print(f"\t {CHOICES_LANGUAGE_NUM[int(num_languages) - 1]}")


def answer_check():
    """Checks if user responses are correct"""
    print("Are all answers correct?")
    global correct_answers
    correct_answers = str(input("\tType 'Y' for yes or 'N' for no \n")).upper()
    while correct_answers != "Y":
        if correct_answers == "Y":
            print("\tThank you for responding to this survey.")
            print("\tYour responses will now be added to our server.")
            print("\tHave a nice day!")
        elif correct_answers == "N":
            results()
            global wrong_question
            wrong_question = str(input("\tPlease enter the question number to answer again: \n"))
            if wrong_question == "1":
                question_one()
                results()
                print("Are all answers correct?")
                correct_answers = str(input("\tType 'Y' for yes or 'N' for no \n")).upper()
                if correct_answers == "N":
                    wrong_question = str(input("\tPlease enter the question number to answer again: \n"))
                elif correct_answers == "Y":
                    print("\tThank you for your corrections.")
                    print("\tYour responses will now be recorded on our server.")
                else: 
                    print("\tDid you type 'Y' for yes and 'N' for no? \n")
                    print("\tWere all the responses above correct? \n")
                    correct_answers = str(input("\tType 'Y' for yes or 'N' for no \n")).upper()
            elif wrong_question == "2":
                question_two()
                results()
                print("Are all answers correct?")
                correct_answers = str(input("\tType 'Y' for yes or 'N' for no \n")).upper()
                if correct_answers == "N":
                    wrong_question = str(input("\tPlease enter the question number to answer again: \n"))
                elif correct_answers == "Y":
                    print("\tThank you for your corrections.")
                    print("\tYour responses will now be recorded on our server.")
                else: 
                    print("\tDid you type 'Y' for yes and 'N' for no? \n")
                    print("\tWere all the responses above correct? \n")
                    correct_answers = str(input("\tType 'Y' for yes or 'N' for no \n")).upper()
            elif wrong_question == "3":
                question_three()
                results()
                print("Are all answers correct?")
                correct_answers = str(input("\tType 'Y' for yes or 'N' for no \n")).upper()
                if correct_answers == "N":
                    wrong_question = str(input("\tPlease enter the question number to answer again: \n"))
                elif correct_answers == "Y":
                    print("\tThank you for your corrections.")
                    print("\tYour responses will now be recorded on our server.")
                else: 
                    print("\tDid you type 'Y' for yes and 'N' for no? \n")
                    print("\tWere all the responses above correct? \n")
                    correct_answers = str(input("\tType 'Y' for yes or 'N' for no \n")).upper()
            elif wrong_question == "4":
                question_four()
                results()
                print("Are all answers correct?")
                correct_answers = str(input("\tType 'Y' for yes or 'N' for no \n")).upper()
                if correct_answers == "N":
                    wrong_question = str(input("\tPlease enter the question number to answer again: \n"))
                elif correct_answers == "Y":
                    print("\tThank you for your corrections.")
                    print("\tYour responses will now be recorded on our server.")
                else: 
                    print("\tDid you type 'Y' for yes and 'N' for no? \n")
                    print("\tWere all the responses above correct? \n")
                    correct_answers = str(input("\tType 'Y' for yes or 'N' for no \n")).upper()
            elif wrong_question == "5":
                question_five()
                results()
                print("Are all answers correct?")
                correct_answers = str(input("\tType 'Y' for yes or 'N' for no \n")).upper()
                if correct_answers == "N":
                    wrong_question = str(input("\tPlease enter the question number to answer again: \n"))
                elif correct_answers == "Y":
                    print("\tThank you for your corrections.")
                    print("\tYour responses will now be recorded on our server.")
                else: 
                    print("\tDid you type 'Y' for yes and 'N' for no? \n")
                    print("\tWere all the responses above correct? \n")
                    correct_answers = str(input("\tType 'Y' for yes or 'N' for no \n")).upper()
            elif wrong_question == "6":
                question_six()
                results()
                print("Are all answers correct?")
                correct_answers = str(input("\tType 'Y' for yes or 'N' for no \n")).upper()
                if correct_answers == "N":
                    wrong_question = str(input("\tPlease enter the question number to answer again: \n"))
                elif correct_answers == "Y":
                    print("\tThank you for your corrections.")
                    print("\tYour responses will now be recorded on our server.")
                else: 
                    print("\tDid you type 'Y' for yes and 'N' for no? \n")
                    print("\tWere all the responses above correct? \n")
                    correct_answers = str(input("\tType 'Y' for yes or 'N' for no \n")).upper()
            else:
                print("\tPlease select from questions '1 - 6' \n")
                wrong_question = str(input("\tPlease enter the incorrect question number: \n"))
        else:
            print("\tDid you type 'Y' for yes and 'N' for no? \n")
            print("\tWere all the responses above correct? \n")
            correct_answers = str(input("\tType 'Y' for yes or 'N' for no \n")).upper()


def add_to_sheet(data):
    """Adding user responses to sheet"""
    responses_sheet.append_row(data)
    print("Responses recorded successfully.")

def print_averages():
    return

user_input()

# test_answers = ["Test", "test@email.com", "Python", "1-2 Years", "Dog", "Test"]
# add_to_sheet(test_answers)