from random import choice, randint
import math
import operator as op

""" Table_div_num, table or divisor being used for the calculation
Num_array, array with the available numbers to be used in the calculation
Operator, operator to be used in the calculation """


def create_calculation(table_div_num, num_array, operator):
    operations = {
        "*": op.mul,
        "//": op.floordiv,
        "%": op.mod
    }

    random_integer = choice(num_array)  # Random integer from the available numbers in the num_array.
    calculation_answer = operations[operator](random_integer, table_div_num)
    num_array.remove(random_integer)  # Remove option from array, so it can't be used again.

    # Returns the calculation answer, the random number and the updated num_array.
    return calculation_answer, random_integer, num_array


# Function to check if the user input is valid.
def input_valid_str(question, error_msg, possible_answers):
    svar = input(question).lower()
    while svar not in possible_answers:  # If answer is incorrect, return a error message.
        svar = input(f'{error_msg}\n{question}').lower()

    return svar


# Function to check if the user input is valid.
def input_valid_int(question, error_msg, min, max):
    while True:  # Loop until a valid integer is entered
        str = input(question)
        if str.isdigit():  # Only accept integers
            svar = int(str)
            if svar >= min and svar <= max:
                return svar  # Correct integer is being returned.
        print(error_msg)


game_on = True
lose = False

num_questions = None
table_divisor = None
operator_selected = None
questions_answered = 0

# Game loop, while boolean game_on is True the game will continue.
while game_on:
    
    still_alive = True  # Boolean to check if the user is still alive.
    num_array = list(range(0, 13))  # List with all the numbers from 0 to 12.

    # If the user didn't lose during their previous attempt, the game will ask the user to different options.
    if lose is False:
        num_questions = input_valid_int("Välj antal frågor för detta spelet: ", "Ange ett giltigt svar!", 12, 39)
        operator_selected = input_valid_str("Välj operator (* , //, %) eller Random: ", "Ange ett giltigt svar!",
                                            ["*", "//", "%", "random"])
        if operator_selected == "*":
            table_divisor = input_valid_int("Välj tabell (2-12): ", "Ange ett giltigt svar!", 1, 12)
        elif operator_selected == "//" or operator_selected == "%":
            table_divisor = input_valid_int("Välj divisor (2-5): ", "Ange ett giltigt svar!", 2, 5)
        else:
            table_divisor = 2

    door_array = list(range(1, num_questions + 1))  # An array with the number of available doors.

    # If there are more than 13 questions, the array will be doubled, or if there are more than 26 questions, 
    # the array will be tripled and contain the same number to use for the calculation multiple times times.
    if num_questions > 26:
        num_array *= 3
    elif num_questions > 13:
        num_array *= 2
    

    while still_alive:
        questions_answered += 1
        door_chosen = 0
        zombie_door = choice(door_array)  # The zombie door is chosen between the available doors in the array.
        operator = operator_selected
        if operator_selected == "random":  # If the operator is random, the operator will be chosen randomly.
            operator = choice(["*", "//", "%"])
            if operator == "*":
                table_divisor = randint(2, 12)
            elif operator == "//" or operator == "%":
                table_divisor = randint(2, 5)

        question_answer, random_integer, num_array = create_calculation(table_divisor, num_array, operator)
        user_answer = input_valid_int(f"Vad är {random_integer} {operator} {table_divisor}? ", "Ange ett giltigt svar!", 0,
                                      math.inf)
        if user_answer != question_answer:
            print("Fel svar, du blev uppäten av zombies!")
            still_alive = False
            lose = True
        else:
            if len(door_array) == 1:
                print(f"Du har vunnit! Du klarade alla frågor och valde rätt dörrar!")
                still_alive = False
            else:
                while door_chosen not in door_array:
                    door_chosen = input_valid_int(f"Välj en dörr ({door_array}) ", "Ange ett giltigt svar!", 1,
                                                  num_questions)
                    if door_chosen not in door_array:
                        print("Du har valt en dörr som inte finns i listan!")
                    elif door_chosen == zombie_door:
                        print(f"Åh nej, zombisarna var bakom dörr {zombie_door}")
                        print("Du blev uppäten av en zombie! Du förlorade ditt liv!")
                        still_alive = False
                        lose = True
                    else:
                        print(f"Du gick rätt, zombiesarna var bakom dörr {zombie_door}")
                        print(f"Du har klarat {questions_answered} frågor av {num_questions}!")
                
                door_array.remove(door_chosen)
                
                
        print("--------------------------------")
    play_again = input_valid_str("Vill du spela igen? (Ja/Nej) ", "Ange ett giltigt svar!", ('ja', 'nej'))
    if play_again == "nej":
        game_on = False
