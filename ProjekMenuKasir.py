# membuat program menu

# fungsi login
def get_login():
    print("+=============================+")
    print("|/////HALAMAN LOGIN KASIR/////|")
    print("+=============================+")
    username = input("Username : ")
    password = input("Password : ")
 
    if username == "admin" and password == "adminpass":
        print("Login berhasil...\n")
        main_menu()
    else:
        print("Login gagal coba lagi..")
        get_login()

# fungsi menu
def main_menu():
    print("""
+==================================+
|/////MAIN MENU APLIKASI KASIR/////|
+==================================+
| Selamat datang di aplikasi kasir |
+----------------------------------+
| Menu aplikasi                    |
| 1. Program kasir                 |
| 2. Program kalkulator            |
| 3. Exit program                  |
+----------------------------------+
  """)
        
    # input pilihan
    pilihan = input("pilih menu : ")
 
    # pilihan menu
    if pilihan == "1":
        kasir()
    elif pilihan == "2":
        kalkulator()
    else:
        print("program exit")
        exit()

# fungsi kasir 
def kasir():
    print("""
+===================================+
|///////////////////////////////////|
|////PT SAHABAT PANGAN SEJAHTERA////|
|///////////////////////////////////|
+===================================+
|  Nama Barang   |  Kode  |  Harga  |
+----------------+--------+---------+
| Cireng         | CRG    | 10000   |
| Nuget          | NGT    | 15000   |
| Bakso Ayam     | BSA    | 15000   |
| Bakso Sapi     | BSS    | 20000   |
| Pempek         | PPK    | 10000   |
+===================================+
 """)
  
    pesan = str(input("Kode Makanan (CRG/NGT/BSA/BSS/PPK) : "))
    jumlahpesan = int(input("Jumlah Beli : "))
    
    if pesan == "CRG":
      listnama = "Cireng"
      harga = (10000 * jumlahpesan)    
      if jumlahpesan >= 10:
        diskon = int(harga * 0.2)
        totalharga = int(harga - diskon)
      else:
        diskon =(0)
        totalharga = int(harga)
        
    elif pesan == "NGT":
      listnama = "Nuget"
      harga = (15000 * jumlahpesan)
      if jumlahpesan >= 10:
        diskon = int(harga * 0.2)
        totalharga = int(harga - diskon)
      else:
        diskon =(0)
        totalharga = int(harga)
        
    elif pesan == "BSA":
      listnama = "Baso Ayam"
      harga = (15000 * jumlahpesan)
      if jumlahpesan >= 10:
        diskon = int(harga * 0.2)
        totalharga = int(harga - diskon)
      else:
        diskon =(0)
        totalharga = int(harga)
        
    elif pesan == "BSS":
      listnama = "Baso Sapi"
      harga = (20000 * jumlahpesan)
      if jumlahpesan >= 10:
        diskon = int(harga * 0.2)
        totalharga = int(harga - diskon)
      else:
        diskon =(0)
        totalharga = int(harga)
    elif pesan == "PPK":
      listnama = "Pempek"
      harga = (10000 * jumlahpesan)
      if jumlahpesan >= 10:
        diskon = int(harga * 0.2)
        totalharga = int(harga - diskon)
      else:
        diskon =(0)
        totalharga = int(harga)
        
    else:
      listnama = "-"
      harga = "-"
      diskon = "-"
      totalharga = "-"
      
    print("""
+---------------------------------+
|/////////STRUK PEMBELIAN/////////|
+---------------------------------+
 Menu         : {}
 Jumlah Pesan : {}
 Harga        : {}
 Diskon       : {}
+---------------------------------+
 Jumlah Bayar : {}
+---------------------------------+
      """.format(listnama, jumlahpesan, 
      harga, diskon, totalharga))
    
    counter_kasir()
    
# counter kasir
def counter_kasir():
  
    counter = input("Belanja lagi ? (y/t) : ")
    if counter == "y":
        kasir()
     
    elif counter == "t":
        tanya()
     
    else:
        print("Input program salah! harap ulangi.")
   
# fungsi kalkulator
def kalkulator():
    print("""
+==============================+
|//////PROGRAM KALKULATOR//////|
+==============================+
| Operator                     |
| - Tambah (+)                 |
| - Kurang (-)                 |
| - Bagi (/)                   |
| - Kali (*)                   |
| - Sisa bagi/Modulus (mod)    |
+------------------------------+
  """)
     
    a = int(input("Masukan bilangan pertama: "))
    operator = input("Pilih operator: ")
    b = int(input("Masukan bilangan kedua: "))
 
    if operator == "+":
        print("Hasil dari {} + {} = {}"
        .format(a, b, a + b))
    elif operator == "-":
        print("Hasil dari {} - {} adalah {}"
        .format(a, b, a - b))
    elif operator == "/":
        print("Hasil dari {} / {} = {}"
        .format(a, b, a / b))
    elif operator == "*":
        print("Hasil dari {} * {} = {}"
        .format(a, b, a * b))
    elif operator == "mod":
        print("Hasil dari {} % {} = {}"
        .format(a, b, a % b))
    else:
        print("Masukan input yang benar sesuai menu diatas")
    counter_kalkulator()
    
# counter kalkulator
def counter_kalkulator():
  
    counter = input("Hitung lagi ? (y/t) : ")
    if counter == "y":
        kalkulator()
     
    elif counter == "t":
        tanya()
     
    else:
        print("Input program salah! harap ulangi.")

# fungsi tanya
def tanya():
    tanya = input("Kembali ke menu..? (y/t)")
    if tanya == "y":
        main_menu()
    elif tanya == "t":
        exit()
    else:
        print("Input salah")
        print("Masukkan input dengan benar")
 

# main program
if __name__=="__main__":
    get_login()