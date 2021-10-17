# for, while

data_barang = ['buku', 'papan', 'batik']

for data_item in data_barang:
    print(data_item + ' ' + 'tulis')


# for number in range(0, 10):
#     print(number)
#
#
# nama = 'fadila'
# for huruf in nama:
#     print(huruf)


# string itu adalah list, list char

index = 0
while index < 10:
    print(index)
    index = index + 1

# aplikasi cmd
input_user = ''
while input_user != 'c':
    input_user = input('Masukkan teks : ')
    print('teks anda adalah ' + input_user)