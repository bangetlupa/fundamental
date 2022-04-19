def tambah (x,y):
    return x + y
def kurang(x, y):
    return x - y
def kali(x, y):
    return x * y
def bagi(x, y):
    return x / y
print("Select operation.");print("1.tambah");print("2.kurang");print("3.kali");print("4.bagi")
while True:
    choice = input("tentukan operator(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", tambah(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", kurang(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", kali(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", bagi(num1, num2))
    else:
        print("Invalid Input")




