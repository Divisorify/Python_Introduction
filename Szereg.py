def szereg():
    i = 1
    szereg = 1
    while i < 31:
        szereg = (i / (i + 2)) * szereg

        i = i + 1;
    print(szereg)

print(szereg())