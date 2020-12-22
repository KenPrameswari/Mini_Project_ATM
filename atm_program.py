from random import randint
import datetime
from customer import Customer

atm1 = Customer('Ken Prameswari', 1234, 10000)

#LOOPING PEMERIKSAAN
while True:
    id = int(input('Masukkan pin Anda : '))
    percobaan = 0

    #LOOPING VERIFIKASI
    while(id != int(atm1.checkPin()) and percobaan < 3):
        id = int(input('PIN yang Anda masukkan salah. Silahkan coba lagi : '))
        percobaan += 1

        if percobaan == 3:
            print('Eror. Silahkan ambil kartu Anda dan masukkan lagi')
            exit()

    while True:
        print('Selamat Datang ' + atm1.id)
        print('Menu Utama : ')
        print('1. Cek Saldo')
        print('2. Debet')
        print('3. Simpan')
        print('4. Ganti Pin')
        print('5. Keluar')

        variable = int(input('Pilih nomor : '))
        if variable == 1:
            print('Saldo Anda : ' + 'Rp' + str(atm1.checkBalance()))
            exit()

        elif variable == 2:
            nominal = int(input('Masukkan nominal saldo yang akan di debet : Rp'))
            if nominal < int(atm1.checkBalance()):
                print('Sisa saldo Anda : ' + 'Rp' + str(atm1.withdrawBalance(nominal)))
            else:
                print('Saldo Anda tidak cukup')
            exit()

        elif variable == 3:
            nominal = int(input('Masukkan nominal saldo yang akan di simpan : Rp'))
            print('Saldo Anda : ' + 'Rp' + str(atm1.depositBalance(nominal)))
            exit()

        elif variable == 4:
            pin_baru = input('Masukkan nomor pin baru :')
            if int(pin_baru) != int(atm1.checkPin()):
                print('Pin baru Anda : ' + pin_baru)
            else:
                print('Pin yang Anda masukkan sama dengan pin Anda sebelumnya. Mohon masukkan nomor baru.')
            exit()

        elif variable == 5:
            print(str(randint(100000,1000000)) + ' ' + str(datetime.datetime.now()) + ' ' + str(atm1.checkBalance()))
            exit()

        else:
            print('Eror. Nomor yang Anda masukkan salah.')
            exit()
