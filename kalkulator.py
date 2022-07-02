# membuat kalulator sederhana

angka1 = int(input("masukan angka pertama : "))
operator = input("masukan operator : ")
angka2 = int(input("masukan angka kedua : "))


if operator == '+':
    hasil = angka1 + angka2
    print(f"hasil dari {angka1} {operator} {angka2} = {hasil}")

elif operator == "-":
    hasil = angka1 - angka2
    print(f"hasil dari {angka1} {operator} {angka2} = {hasil}")

elif operator == "x" or operator == "*" or operator == "X":
    hasil = angka1 * angka2
    print(f"hasil dari {angka1} {operator} {angka2} = {hasil}")

elif operator == "/":
    if angka1 <= 0:
        while True:
            print("tolong masukan angka yang lebih dari 0")
            angka1 = int(input("masukan angka : "))
            angka2 = int(input("masukan angka2 : "))
            hasil = angka1 / angka2
            print(f"hasil dari {angka1} {operator} {angka2} = {hasil}")
            break

    elif angka2 <= 0:
        while True:
            print("tolong masukan angka yang lebih dari 0")
            angka1 = int(input("masukan angka1 : "))
            angka2 = int(input("masukan angka2 : "))
            hasil = angka1 / angka2
            print(f"hasil dari {angka1} {operator} {angka2} = {hasil}")
            break
    else:
        print(f"hasil dari {angka1} {operator} {angka2} = {hasil}")


