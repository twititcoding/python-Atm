import rupiah
import os


# saldo
saldo = 10000000
nama = "Mr. GHOSAM"
No_rekening = 1122334455

# fungsi pembersih


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
# fungsi untukkeluar


def keluar():
    print("\n")
    exit()

# fungsi untuk menu pilihan


def to_menu():
    print("""
    [1] transaksi kembali
    [2] keluar
    """)
    s = int(input("Masukan Pilihan :"))
    if (s == 1):
        menu()
    elif(s == 2):
        keluar()
    else:
        print("error")

# kembali ke menu login


def login():
    print("\n")
    input("Tekan Enter untuk kembali...")
    tampilan_login()

# fungsi tampilan login


def tampilan_login():
    clear_screen()
    print("\n")

    print("="*40)
    print("PROGRAM BANK BANKTUT (ATM)")
    print("="*40)
    print("SELAMAT DATANG DI BANK BANKTUT")
    print("pin = 12345678")

    pin = int(input("masukan pin:"))

    if (pin == 12345678):
        menu()
    else:
        login()

# menu utama


def menu():
    clear_screen()
    print("""

    [1] Penarikan Tunai.
    [2] Transfer Ke Rekening
    [3] Cek Saldo
    [0] Keluar

    """)

    pilihan = int(input("masukan pilihan :"))
    if (pilihan == 1):
        menu_penarikan()
    elif (pilihan == 2):
        menu_transfer()
    elif (pilihan == 3):
        menu_saldo()
    elif (pilihan == 0):
        keluar()

    else:
        print("error")
        login()

#  fungsi menu inti transfer


def menu_transfer():
    clear_screen()
    print("""
    ==========================
    MENU TRANSFER BANK BANKTUT
    ++++++++++++++++++++++++++

    """)
    rekening = int(input("masukan nomer rekening tujuan :"))
    transfer = int(input("masukan jumlah transfer :"))
    nama_penerima = str(input("masukan Nama Penerima :"))

    stuktransfer = ("""

        =================================
        +         BANK BANKTUT          +
        +++++++++++++++++++++++++++++++++
         Nama Penerima ={}
         Rek Tujuan ={}
         Jumlah ={}
        +++++++++++++++++++++++++++++++++
        +   Transaksi telah berhasil    +
        +++++++++++++++++++++++++++++++++

    """)
    print(stuktransfer.format(nama_penerima,
                              rekening, rupiah.rupiah_format(transfer)))

    to_menu()

# fungsi menu cek saldo


def menu_saldo():
    clear_screen()
    ceksaldo = ("""
            \n
        ----------------------------
        MENU CEK SALDO
        ----------------------------
        Nama pemilik rekening :{}
        No Rekening :{}
        Jumlah Saldo Anda :{}
        ----------------------------
        """)
    print(ceksaldo .format(nama, No_rekening, rupiah.rupiah_format(saldo)))
    to_menu()


def menu_penarikan():
    clear_screen()
    print("MENU PENARIKAN")
    print(40*"-")

    print("saldo anda Rp:{}".format(rupiah.rupiah_format(saldo)))
    penarikan = int(input("masukan jumlah uang:"))
    if (penarikan >= saldo):
        print(

            """
            \n
        ----------------------------
        SALDO ANDA TIDAK MENCUKUPI
        ----------------------------
        """)
    elif (penarikan >= 50000):
        hasil = (saldo - penarikan)

        stuck = ("""
        =================================
        +       BANK GHOSAM UANG        +
        +++++++++++++++++++++++++++++++++
         Jumlah = Rp: {}
         Saldo Anda =Rp: {}
        +++++++++++++++++++++++++++++++++
        +   Selamat Menikmati uang nya  +
        +++++++++++++++++++++++++++++++++
        """)
        print(stuck.format(rupiah.rupiah_format(
            penarikan), (rupiah.rupiah_format(hasil))))

    elif (saldo < 50000):
        print("untuk saat ini saldo kurang dari Rp:50.000 ")

    else:
        print("tidak bisa diambil")

    to_menu()


if __name__ == "__main__":

    while True:
        tampilan_login()
