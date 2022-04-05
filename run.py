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
responses_sheet = SHEET.worksheet("responses")
calculations_sheet = SHEET.worksheet("calculations")

# setting up response options arrays
CHOICES_INDUSTRY = [
    "Tech / Development", "Healthcare",
    "Operations / Logistics", "Human Resources",
    "Finance / Banking", "Academia", "Law", "Other"
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

# setting up response calculations for industry question
industry_range = ["A14", "A15", "A16", "A17", "A18", "A19", "A20", "A21"]
industry_range_count = ["B14", "B15", "B16", "B17", "B18", "B19", "B20", "B21"]
industry_range_avg = ["C14", "C15", "C16", "C17", "C18", "C19", "C20", "C21"]

# setting up response calculations for favourite language
fav_lang_range = ["A25", "A26", "A27", "A28", "A29", "A30", "A31", "A32", "A33", "A34"]
fav_lang_range_count = ["B25", "B26", "B27", "B28", "B29", "B30", "B31", "B32", "B33", "B34"]
fav_lang_range_avg = ["C25", "C26", "C27", "C28", "C29", "C30", "C31", "C32", "C33", "C34"]

# setting up response calculations for years coding
years_coding_range = ["A38", "A39", "A40", "A41", "A42", "A43"]
years_coding_range_count = ["B38", "B39", "B40", "B41", "B42", "B43"]
years_coding_range_avg = ["C38", "C39", "C40", "C41", "C42", "C43"]

# setting up response calculations for number of languages known
num_languages_range = ["A47", "A48", "A49", "A50", "A51", "A52", "A53"]
num_languages_range_count = ["B47", "B48", "B49", "B50", "B51", "B52", "B53"]
num_languages_range_avg = ["C47", "C48", "C49", "C50", "C51", "C52", "C53"]



def industry_averages():
    """Prints industry averages to terminal."""
    print("\t____________________________________________________________")
    for (a, b, c) in zip(industry_range, industry_range_count, industry_range_avg):
        print(f"\tIndustry: {calculations_sheet.acell(a).value} | Count: {calculations_sheet.acell(b).value} | Percentage: {calculations_sheet.acell(c).value} \n")
    print("\t____________________________________________________________")


def fav_lang_averages():
    """Prints favourite language averages to terminal."""
    print("\t____________________________________________________________")
    for (a, b, c) in zip(fav_lang_range, fav_lang_range_count, fav_lang_range_avg):
        print(f"\tFavourite Language: {calculations_sheet.acell(a).value} | Count: {calculations_sheet.acell(b).value} | Percentage: {calculations_sheet.acell(c).value} \n")
    print("\t____________________________________________________________")


def years_coding_averages():
    """Prints years coding averages to terminal."""
    print("\t____________________________________________________________")
    for (a, b, c) in zip(years_coding_range, years_coding_range_count, years_coding_range_avg):
        print(f"\tYears Coding: {calculations_sheet.acell(a).value} | Count: {calculations_sheet.acell(b).value} | Percentage: {calculations_sheet.acell(c).value} \n")
    print("\t____________________________________________________________")


def num_languages_averages():
    """Prints number of languages averages to terminal."""
    print("\t____________________________________________________________")
    for (a, b, c) in zip(num_languages_range, num_languages_range_count, num_languages_range_avg):
        print(f"\tNumber of Languages: {calculations_sheet.acell(a).value} | Count: {calculations_sheet.acell(b).value} | Percentage: {calculations_sheet.acell(c).value} \n")
    print("\t____________________________________________________________")




industry_averages()
fav_lang_averages()
years_coding_averages()
num_languages_averages()


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
    print(
        f"\tYou have selected '{CHOICES_INDUSTRY[int(industry_choice)-1]}'. Is that correct? \n")
    correct_industry = str(input("\tType 'Y' for yes or 'N' for no: \n"))
    correct_industry = correct_industry.upper()
    while correct_industry != "Y":
        if correct_industry == "Y":
            print("\tGreat! Next question. \n")
        elif correct_industry == "N":
            print("\tPlease input your selection again: \n")
            industry_choice = str(input("\n"))
            print(
                f"\t'{CHOICES_INDUSTRY[int(industry_choice)-1]}' - Is that correct? \n")
            correct_industry = str(
                input("\tType 'Y' for yes or 'N' for no: \n")).upper()
        else:
            print("\tAre you sure you typed 'Y for yes and 'N' for no? \n")
            print(CHOICES_INDUSTRY[int(industry_choice) - 1])
            correct_industry = str(
                input("\n \tIs the selection above correct? \n")).upper()


def question_four():
    """Code for question four."""
    print("4. What is your favourite programming language?")
    print("\tPlease select from the choices below.")
    print(
        "\tTo make a selection, please type the number of your selection. \n")
    for i in range(len(CHOICES_LANGUAGE)):
        print(f"\t{i + 1}: {CHOICES_LANGUAGE[i]}")
    global favourite_language
    favourite_language = str(input("\n"))
    print(
        f"\tYou have selected '{CHOICES_LANGUAGE[int(favourite_language)-1]}'. Is that correct? \n")
    correct_language = str(
        input("\tType 'Y' for yes or 'N' for no: \n")).upper()
    while correct_language != "Y":
        if correct_language == "Y":
            print("\tGreat! Next question. \n")
        elif correct_language == "N":
            print("\tPlease input your selection again: \n")
            favourite_language = str(input("\n"))
            print(
                f"\t'{CHOICES_LANGUAGE[int(favourite_language)-1]}' - Is that correct? \n")
            correct_language = str(
                input("\tType 'Y' for yes or 'N' for no: \n")).upper()
        else:
            print("\tAre you sure you typed 'Y for yes and 'N' for no? \n")
            print(CHOICES_LANGUAGE[int(favourite_language) - 1])
            correct_language = str(
                input("\n \tIs the selection above correct? \n")).upper()


def question_five():
    """Code for question five."""
    print("5. How long have you been programming?")
    print("\tPlease select from the choices below.")
    print("\tTo make a selection, please type the number of your selection. \n")
    for i in range(len(CHOICES_LENGTH)):
        print(f"\t{i + 1}: {CHOICES_LENGTH[i]}")
    global years_programming
    years_programming = str(input("\n"))
    print(
        f"\tYou have selected '{CHOICES_LENGTH[int(years_programming)-1]}'. Is that correct? \n")
    correct_years = str(input("\tType 'Y' for yes or 'N' for no: \n")).upper()
    while correct_years != "Y":
        if correct_years == "Y":
            print("\tGreat! Next question. \n")
        elif correct_years == "N":
            print("\tPlease input your selection again: \n")
            years_programming = str(input("\n"))
            print(
                f"\t'{CHOICES_LENGTH[int(years_programming)-1]}' - Is that correct? \n")
            correct_years = str(
                input("\tType 'Y' for yes or 'N' for no: \n")).upper()
        else:
            print("\tAre you sure you typed 'Y for yes and 'N' for no? \n")
            print(CHOICES_LENGTH[int(years_programming) - 1])
            correct_years = str(
                input("\n \tIs the selection above correct? \n")).upper()


def question_six():
    """Code for question six."""
    print("6. How many programming languages do you know?")
    print("\tPlease select from the choices below.")
    print("\tTo make a selection, please type the number of your selection. \n")
    for i in range(len(CHOICES_LANGUAGE_NUM)):
        print(f"\t{i + 1}: {CHOICES_LANGUAGE_NUM[i]}")
    global num_languages
    num_languages = str(input("\n"))
    print(
        f"\tYou have selected '{CHOICES_LANGUAGE_NUM[int(num_languages)-1]}'. Is that correct? \n")
    correct_num = str(input("\tType 'Y' for yes or 'N' for no: \n")).upper()
    while correct_num != "Y":
        if correct_num == "Y":
            print("\tGreat! Next question. \n")
        elif correct_num == "N":
            print("\tPlease input your selection again: \n")
            num_languages = str(input("\n"))
            print(
                f"\t'{CHOICES_LANGUAGE_NUM[int(num_languages)-1]}' - Is that correct? \n")
            correct_num = str(
                input("\tType 'Y' for yes or 'N' for no: \n")).upper()
        else:
            print("\tAre you sure you typed 'Y for yes and 'N' for no? \n")
            print(CHOICES_LANGUAGE_NUM[int(num_languages) - 1])
            correct_num = str(
                input("\n \tIs the selection above correct? \n")).upper()


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
            wrong_question = str(
                input("\tPlease enter the question number to answer again: \n"))
            if wrong_question == "1":
                question_one()
                results()
                print("Are all answers correct?")
                correct_answers = str(
                    input("\tType 'Y' for yes or 'N' for no \n")).upper()
                if correct_answers == "N":
                    wrong_question = str(
                        input("\tPlease enter the question number to answer again: \n"))
                elif correct_answers == "Y":
                    print("\tThank you for your corrections.")
                    print("\tYour responses will now be recorded on our server.")
                else:
                    print("\tDid you type 'Y' for yes and 'N' for no? \n")
                    print("\tWere all the responses above correct? \n")
                    correct_answers = str(
                        input("\tType 'Y' for yes or 'N' for no \n")).upper()
            elif wrong_question == "2":
                question_two()
                results()
                print("Are all answers correct?")
                correct_answers = str(
                    input("\tType 'Y' for yes or 'N' for no \n")).upper()
                if correct_answers == "N":
                    wrong_question = str(
                        input("\tPlease enter the question number to answer again: \n"))
                elif correct_answers == "Y":
                    print("\tThank you for your corrections.")
                    print("\tYour responses will now be recorded on our server.")
                else:
                    print("\tDid you type 'Y' for yes and 'N' for no? \n")
                    print("\tWere all the responses above correct? \n")
                    correct_answers = str(
                        input("\tType 'Y' for yes or 'N' for no \n")).upper()
            elif wrong_question == "3":
                question_three()
                results()
                print("Are all answers correct?")
                correct_answers = str(
                    input("\tType 'Y' for yes or 'N' for no \n")).upper()
                if correct_answers == "N":
                    wrong_question = str(
                        input("\tPlease enter the question number to answer again: \n"))
                elif correct_answers == "Y":
                    print("\tThank you for your corrections.")
                    print("\tYour responses will now be recorded on our server.")
                else:
                    print("\tDid you type 'Y' for yes and 'N' for no? \n")
                    print("\tWere all the responses above correct? \n")
                    correct_answers = str(
                        input("\tType 'Y' for yes or 'N' for no \n")).upper()
            elif wrong_question == "4":
                question_four()
                results()
                print("Are all answers correct?")
                correct_answers = str(
                    input("\tType 'Y' for yes or 'N' for no \n")).upper()
                if correct_answers == "N":
                    wrong_question = str(
                        input("\tPlease enter the question number to answer again: \n"))
                elif correct_answers == "Y":
                    print("\tThank you for your corrections.")
                    print("\tYour responses will now be recorded on our server.")
                else:
                    print("\tDid you type 'Y' for yes and 'N' for no? \n")
                    print("\tWere all the responses above correct? \n")
                    correct_answers = str(
                        input("\tType 'Y' for yes or 'N' for no \n")).upper()
            elif wrong_question == "5":
                question_five()
                results()
                print("Are all answers correct?")
                correct_answers = str(
                    input("\tType 'Y' for yes or 'N' for no \n")).upper()
                if correct_answers == "N":
                    wrong_question = str(
                        input("\tPlease enter the question number to answer again: \n"))
                elif correct_answers == "Y":
                    print("\tThank you for your corrections.")
                    print("\tYour responses will now be recorded on our server.")
                else:
                    print("\tDid you type 'Y' for yes and 'N' for no? \n")
                    print("\tWere all the responses above correct? \n")
                    correct_answers = str(
                        input("\tType 'Y' for yes or 'N' for no \n")).upper()
            elif wrong_question == "6":
                question_six()
                results()
                print("Are all answers correct?")
                correct_answers = str(
                    input("\tType 'Y' for yes or 'N' for no \n")).upper()
                if correct_answers == "N":
                    wrong_question = str(
                        input("\tPlease enter the question number to answer again: \n"))
                elif correct_answers == "Y":
                    print("\tThank you for your corrections.")
                    print("\tYour responses will now be recorded on our server.")
                else:
                    print("\tDid you type 'Y' for yes and 'N' for no? \n")
                    print("\tWere all the responses above correct? \n")
                    correct_answers = str(
                        input("\tType 'Y' for yes or 'N' for no \n")).upper()
            else:
                print("\tPlease select from questions '1 - 6' \n")
                wrong_question = str(
                    input("\tPlease enter the incorrect question number: \n"))
        else:
            print("\tDid you type 'Y' for yes and 'N' for no? \n")
            print("\tWere all the responses above correct? \n")
            correct_answers = str(
                input("\tType 'Y' for yes or 'N' for no \n")).upper()


def add_to_sheet(data):
    """Adding user responses to sheet"""
    responses_sheet.append_row(data)
    print("Responses recorded successfully.")


def print_averages():
    """Returns the average results from survey responses"""
    return


def view_data():
    """Counterpart function to user_input for reading response data"""
    return


def main():
    """Main function that allows user to read or write to database"""
    print("Welcome!")
    print("What would you like to do today?")
    print("Please enter '1' or '2' to make a selection \n")
    print("\t1: Answer the 'Programming Preferences' survey")
    print("\t2: View aggregated data from user responses")
    global read_or_write
    read_or_write = str(input("/n"))
    if read_or_write == "1":
        user_input()
    elif read_or_write == "2":
        view_data()
    else:
        print("Please enter 1 or 2 and press enter.")
        read_or_write = str(input("/n"))





