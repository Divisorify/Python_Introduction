print("Program oblicza miejsca zerowe funkcji kwadratowej.")
a = int(input("Podaj wartość 'a' do sprawdzenia: "))
b = int(input("Podaj wartość 'b' do sprawdzenia: "))
c = int(input("Podaj wartość 'c' do sprawdzenia: "))

delta = pow(b,2) + 4 * a * c

print(f"Delta wynosi: {delta}")
print()
if delta>0:
    pdelta = pow(delta,1/2.0)
    print("Pierwiastek z delty wynosi: %d" % (pdelta))
    x1 = (-b-pdelta)/2*a
    x2 = (-b+pdelta)/2*a
    print("Delta dodatnia, posiada dwa miejsca zerowe x1 i x2, ktorych wartosci wynosza: %d  i  %d" % (x1,x2))
if delta==0:
    x3=-b/2*a
    print("Delta wynosi 0, posiada więc ona jedno miejsce zerowe, ktorej wartosc to %d" % (x3))
if delta<0:
    pdelta = pow(delta,1/2.0)
    print("Pierwiastek z delty wynosi: %d" % (pdelta))
    re=(-b-pdelta)/2*a
    im=(-b+pdelta)/2*a
    print("Czesc rzeczywista: (-%d-%d i)/2*%d" % (b,pdelta,a))
    print("Czesc urojona: (-%d+%d i)/2*%d" % (b,pdelta,a))