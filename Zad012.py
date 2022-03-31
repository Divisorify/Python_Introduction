import datetime

def to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day

date = datetime.date(2019,2,28)
str = datetime.date.today()
str1 = str.strftime('%d-%m-%Y')
print(f"Dziś jest {str1}")

timedelta = str - date

print(f"Różnica pomiędzy dziś, a 28.02.2019 to {timedelta}")

roznica = to_integer(str)- to_integer(date)

if (roznica < 0):
    print("Jest to data z przyszłości.")
else:
    print("Jest to data z przeszłości.")