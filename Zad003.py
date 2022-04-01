
try:
    x = int(input("Proszę wprowadzić liczbę 1: "))
    y = int(input("Proszę wprowadzić liczbę 2: "))
except ValueError:
    print ("Uch! to nie jest poprawna liczba! Spróbuj jeszcze raz...")


print(f"Suma liczb: {y+x}")