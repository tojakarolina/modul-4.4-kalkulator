import sys
import logging
logging.basicConfig(level=logging.INFO)

def calculate_2_numbers(function, num_1, num_2):
    if function == 1:
            calculation = num_1 + num_2
    elif function == 2:
            calculation = num_1 - num_2
    elif function == 3:
            calculation = num_1*num_2
    elif function == 4:
            calculation = num_1 / num_2
    else: 
            exit(1)
    return calculation

if __name__ == "__main__":
    pytanie = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    skl_1 = float(input("Podaj składnik 1. "))
    skl_2 = float(input("Podaj składnik 2. "))
    odp = ""
    if pytanie == 1:
            odp = "Dodaję"
    elif pytanie == 2:
            odp = "Odejmuję"
    elif pytanie == 3:
            odp = "Mnożę"
    elif pytanie == 4:
            odp = "Dzielę"
    logging.info(f"{odp} {skl_1:.2f} i {skl_2:.2f}")
    print(f"Wynik to {calculate_2_numbers(pytanie,skl_1,skl_2)}")

