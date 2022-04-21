def tambah (x,y):
    return x + y
def kurang (x,y):
    return x - y
def kali (x,y):
    return x*y
def bagi (x,y):
    return x/y

print('pilihlah operator');print('1.tambah 2.kurang 3.kali 4.bagi')

while True:
    operator = input('pilih operator:')
    if operator in ('1','2','3','4'):
        num1 = float(input(':'))
        num2 = float(input(':'))
        if operator == '1':
            print(num1,'+',num2,'=',tambah(num1,num2))
        elif operator == '2':
            print(num1, '-', num2, '=', kurang(num1, num2))
        elif operator == '3':
            print(num1, '*', num2, '=', kali(num1, num2))
        elif operator == '4':
            print(num1, ':', num2, '=', bagi(num1, num2))
        selesai = input("apakah mau terus jika tidak pilih 'no': ")
        if selesai == 'no':
            break

    else:
        print('operator hanya 1,2.3.4')





