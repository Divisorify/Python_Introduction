s = input("Podaj łańcuch znaków do sprawdzenia: ")
def isStringAlpha(s):
    for char in s:
        print(char, char.isalpha())

isStringAlpha(s)