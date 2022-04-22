#perulangan
#for i in range(5):
#angka = 1
#print(angka)
#angka = angka + 1
#print(angka)
#angka = angka + 1
#print(angka)
#di atas cara lama

#dibawah dengan list
angka2= [12,13,97,31,4]
for angka in angka2:
    print(f"i sekarang -> {angka}")
print('akhir dari program')

#ini dengan range
angka2_range = range(3)
for i in angka2_range:
    print(f"i sekarang ->{i}")
print('akhir program 2')

#menggunakan string
data_str = 'sendiri'
for huruf in data_str:
    print(f'huruf {huruf}')
print('akhir program 4')
#======================================
#WHILE
angka = 5
while angka > 1:
    angka -= 1
    print(f'hendy keren {angka}')
    if angka == 2:
        print('terlihat lewat')
        continue #continue agar bybass langsung ke atas lagi
    print('itu benar')
#tes membuat prcabangan dengan while
def kurang(x, y):
    return x - y


print("tolong baca total buku yg ada")

while True:
    stock = float(input('stock buku : '))
    read = float(input('buku sudah di baca: '))
    if stock == read:
        print('selamat anda sudah baca semua')
        break
    elif stock > read:
        print('tolong baca sisa', kurang(stock, read), 'buku')
        sisa = input('sudah beraba kali sisa buku anda baca? ')
        if sisa =='1':
            print('baca satu kali lagi')
            break
        elif sisa >= '2':
            print('sudah cukup tidak perlu di baca lagi maksimal 2 kali')
            break
        elif sisa < '1':
            print('tlg dibaca maksimal 2 kali')
            break


    else:
        print('stock buku harus lebih besar atau sama dari yg dibaca')















































