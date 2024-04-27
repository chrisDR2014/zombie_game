from random import choice
import math
import operator as op

def create_calculation(table_num, num_array, operator):
    operations = {
        "*": op.mul,
        "//": op.floordiv,
        "%": op.mod
    }
    
    random_integer = choice(num_array)
    question_answer = operations[operator](random_integer, table_num)
    num_array.remove(random_integer)
    print(question_answer)

    return question_answer, random_integer, num_array

def input_valid_str(question, error_msg, possible_answers):
    svar = input(question).lower()
    while svar not in possible_answers:
        svar = input(f'{error_msg}\n{question}').lower()

    return svar


def input_valid_int(question, error_msg, min, max):
    while True:  # Loopa tills korrekt värde skrivs in
        str = input(question)
        if str.isdigit():  # Bara innehåller siffror (0-9)
            svar = int(str)
            if svar >= min and svar <= max:
                return svar  # Korrekt tal, returnera värdet
        print(error_msg)

game_on = True
lose = False


num_questions = None
user_input = None
operator_selected = None

while game_on:
    still_alive = True
    num_array =  list(range(0, 13))

    if lose == False:
        num_questions = input_valid_int("Välj antal frågor för detta spelet? ", "Ange ett giltigt svar!", 12, 39)
        operator_selected = input_valid_str("Välj operator (* (multiplikation), // (heltalsdivision) eller % (modulus)) ", "Ange ett giltigt svar!", ["*", "//", "%"])
        if operator_selected == "*":
            user_input = input_valid_int("Välj tabell (2-12) ", "Ange ett giltigt svar!", 1, 12)
        elif operator_selected == "//":
            user_input = input_valid_int("Välj divisor (2-5) ", "Ange ett giltigt svar!", 2, 5)
        else:
            user_input = input_valid_int("Välj divisor (2-5) ", "Ange ett giltigt svar!", 2, 5)
    
    door_array = list(range(1, num_questions + 1))
    
    if num_questions > 13:
        num_array = num_array + num_array
    
    if num_questions > 26:
        num_array = num_array + num_array + num_array

    
    while still_alive:
        print(num_array)
        door_chosen = 0;
        zombie_door = choice(door_array)
        print("Zombie dörr:", zombie_door)
        question_answer, random_integer, num_array = create_calculation(user_input, num_array, operator_selected)
        user_answer = input_valid_int(f"Vad är {random_integer} {operator_selected} {user_input}? ", "Ange ett giltigt svar!", 0, math.inf)
        if user_answer != question_answer:
            print("Fel svar, du blev uppäten av zombies!")
            still_alive = False
            lose = True
        else:
            if len(door_array) == 1:
                print(f"Du har klarat dig, zombiesarna var bakom dörr {zombie_door}")
                still_alive = False
            else: 
                while door_chosen not in door_array:
                    door_chosen = input_valid_int(f"Välj en dörr ({door_array}) ", "Ange ett giltigt svar!", 1, num_questions)
                    if door_chosen not in door_array:
                        print("Du har valt en dörr som inte finns i listan!")
                        
                door_array.remove(door_chosen)
                if door_chosen == zombie_door:
                    print("Du blev uppäten av en zombie! Du förlorade ditt liv!")
                    still_alive = False
                    lose = True

    play_again = input_valid_str("Vill du spela igen? (Ja/Nej) ", "Ange ett giltigt svar!", ('ja', 'nej'))
    if play_again == "nej":
        game_on = False