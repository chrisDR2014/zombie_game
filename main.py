#E-Nivå

#Användaren blir inlåst i ett hus med zombies och enda sättet att ta sig ut är att 
#svara rätt på matematiska frågor och välja rätt dörr för att undvika att bli uppäten av zombiesar.
#Antal frågor ska vara 12 och varje fråga består av två delar, först måste användaren 
#svara rätt på en matematisk fråga och sedan välja rätt dörr för att undvika zombiesarna.

# create a input

from random import randint

zombie_door = randint(1,12)
print(zombie_door)
user_input = int(input("Välj tabell (1-12) "))

random_integer = randint(1,12)
question_answer = user_input * random_integer
print(question_answer)
user_answer = int(input(f"Vad är {random_integer}*{user_input}? "))
if question_answer == user_answer:
    user_select_door = int(input("Du har rätt svar! Välj en dörr (1-12) "))
    if user_select_door == zombie_door:
        print("Du blev uppäten av en zombie! Du förlorade ditt liv!")
    else:
        print("Du undviker zombiesarna!")


def choose_door(number):
    