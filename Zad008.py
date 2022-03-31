list = [54,3,5,76,7,4,32,2,4,6,9,9,7,3,2,3,345,5,3,3,2]

print("Liczby podzielne przez 2:")
suma = 0;
for x in list:
    if x % 2 == 0:
        print(x)
        suma += x
print(f"Suma: {suma}")

print()
print("Liczby podzielne przez 2 i 3:")
suma2 =0;
for x in list:
    if x % 2 == 0:
        if x % 3 == 0:
            print(x)
            suma2 += x
print(f"Suma: {suma2}")

print()

# liczb = 0
# for x in list:
#     if x>= 10 or x <=100:
#         liczb += 1

count = sum(map(lambda x : x>= 10 or x <=100, list))
print(f"Liczb w przedziale od 10 do 100 jest: {count}")
