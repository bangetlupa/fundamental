# 'append' menambahkan data di paling ujung
# 'pop' membuang data paling ujung
# 'len'


gorengan = ['tahu', 'ubi', 'bakwan', 'risol']
print('tampilkan variable gorengan')
print(gorengan)

print('\nproses semua dengan for in')
for i in gorengan:
    print(i)

print('\ntampilkan isi gorengan pada indeks tertentu')
print(gorengan[0])
print(gorengan[2])

print('\ntampilkan dengan for in range')
for i in range(0, len(gorengan)):
    print(gorengan[i])

gorengan = [1, 'tahu', 121, 42]
print('\ntampilkan dengan for in range,dimana tipe data berbeda')
for i in range(0, len(gorengan)):
    print(gorengan[i])

print('kembalikan list gorengan')
gorengan = ['tahu', 'ubi', 'bakwan', 'risol']
print('tambahan 1 gorengan baru')
gorengan.append('pisang')  # menambahkan isi list
print(gorengan)

# mylist = "Hellobro"
# x = len(gorengan)
# print(x)




