# CAPSTONE PROJECT MODUL 1 (Kevin Octavianus)

dict_data_produk = {
    1011:{'Nama Produk':'Beras','Stock':1000, 'Satuan':'Bal', 'Lokasi': 'Gudang A'},
    1002:{'Nama Produk':'Gula','Stock':200, 'Satuan':'Bal', 'Lokasi': 'Gudang B'},
    1003:{'Nama Produk':'Aqua','Stock':100, 'Satuan':'Dus', 'Lokasi': 'Gudang A'}
}

# function cek value input menu
def cek_input_menu (input_pertanyaan):
    while True:
        input_menu = input(input_pertanyaan)
        if input_menu.isnumeric():
            input_menu = int (input_menu)
            return input_menu
        else :
            print ('\n\033[1mNilai menu yang dimasukkan harus bernilai angka.\033[0m')
       
# function menu utama
def menu_utama():
    while True:
        input_menu_utama=cek_input_menu('''\033[1m
===================================================================================
--------------------------------SELAMAT DATANG-------------------------------------
-----------------------------GUDANG TOKO SEMBAKO-----------------------------------
===================================================================================
\033[0m
Menu :
1. Menampilkan Data
2. Menambahkan Data Baru
3. Mengubah Data
4. Menghapus Data
5. Keluar Program

Masukkan menu yang ingin dipilih : ''')
        if input_menu_utama == 1:     # MENU 1 = MENAMPILKAN DATA
            menu_1 ()
        elif input_menu_utama == 2:   # MENU 2 = MENAMBAHKAN DATA
            menu_2 ()
        elif input_menu_utama == 3:   # MENU 3 = MEMPERBAHARUI DATA
            menu_3 ()
        elif input_menu_utama == 4:   # MENU 4 = MENGHAPUS DATA
            menu_4 ()
        elif input_menu_utama == 5:
            while True: # looping untuk konfirmasi keluar program
                input_konfirmasi = input ('Apakah anda yakin ingin keluar dari program ? (Y/N)').title()
                if input_konfirmasi == 'Y':
                    break
                elif input_konfirmasi == 'N':
                    break
                else:
                    print ('\033[1mNilai yang anda masukkan salah. Harap masukkan Y atau N\033[0m\n')
            if input_konfirmasi == 'Y':
                print ('\033[1m\nSelamat Tinggal dan Terima Kasih !\033[0m') # MENU 5 = EXIT PROGRAM
                break
        else:
            print ('\033[1m\nNilai input menu yang dimasukkan salah. Harap masukkan kembali angka 1-5.\033[0m')

# menu 1
def menu_1 ():
    while True :
        input_submenu1 = cek_input_menu('''\033[1m
++++++++++++++++++++++++++++++++++++SUBMENU 1++++++++++++++++++++++++++++++++++++++
--------------------------------MENAMPILKAN DATA-----------------------------------
\033[0m
Menu :
1. Menampilkan Seluruh Data
2. Menampilkan Data dengan Input Data
3. Kembali ke menu utama

Masukkan submenu yang ingin dipilih : ''')
        if input_submenu1 == 1:
            if len(dict_data_produk)==0:             # Pengecekan apakah data tersedia atau tidak
                print ('\033[1mData Tidak Tersedia\033[0m')
            else:
                menu_1_submenu_1()
        elif input_submenu1 == 2:
            if len(dict_data_produk)==0:             # Pengecekan apakah data tersedia atau tidak
                print ('\033[1mData Tidak Tersedia\033[0m')
            else:
                menu_1_submenu_2 ()
        elif input_submenu1 == 3:
            break
        else:
            print ('\n\033[1mNilai input submenu yang dimasukkan salah. Harap masukkan kembali angka 1-3.\033[0m')
        

# menampilkan semua data yang tersedia
def menu_1_submenu_1 ():
    global dict_data_produk
    dict_data_produk = (dict(sorted(dict_data_produk.items())))
    print ('\nBerikut Data Gudang yang Tersedia\n')
    print ('================================================================================')
    for i in (((list(dict_data_produk.values()))[0]).keys()):    # Memanggil keys dalam value pada keys pertama
        if i =='Nama Produk':
            print ("\033[1m|{:^15}|\033[0m".format('Kode Produk'),end="")
        print ("\033[1m{:^15}|\033[0m".format(i),end="")
    print ('\n--------------------------------------------------------------------------------')
    for i in dict_data_produk.keys():
        print ("|"+" "*5 + "{:04d}".format(i)+" "*6+"|",end="")
        for j in dict_data_produk[i].keys():
            print ("{:^15}|".format(dict_data_produk[i][j]),end="")
        print ()
    print ('--------------------------------------------------------------------------------')

# function menu_1_submeu_2 menampilkan data dengan kata kunci
def menu_1_submenu_2 ():
    while True:
        input_kolom_produk = (input('''
Input Kolom yang tersedia :
1. Kode Produk 
2. Nama Produk
3. Lokasi
Masukkan Input Nama Kolom : '''))
        input_kolom_nilai_produk = ""
        if input_kolom_produk == '1':
            input_kolom_produk = 'Kode Produk'
            input_kolom_nilai_produk = cek_value_kode_produk ('Masukkan Nomor Kode Produk yang datanya ingin ditampilkan : ')
            mengecek_produk_dalam_dict (input_kolom_produk,input_kolom_nilai_produk)
            break
        elif input_kolom_produk == '2':
            input_kolom_produk = 'Nama Produk'
            input_kolom_nilai_produk = cek_value_nama_produk ('Masukkan Nama Produk yang datanya ingin ditampilkan : ')
            mengecek_produk_dalam_dict (input_kolom_produk,input_kolom_nilai_produk)
            break
        elif input_kolom_produk == '3':
            input_kolom_produk = 'Lokasi'
            input_kolom_nilai_produk = cek_value_lokasi('Masukkan Lokasi yang datanya ingin ditampilkan (Gudang A / Gudang B):')
            mengecek_produk_dalam_dict (input_kolom_produk,input_kolom_nilai_produk)
            break
        else:
            print ('\033[1mKolom Tidak Tersedia. Harap masukkan kembali nama Kolom.\033[0m')

# function mengecek kata kunci pada data (dict)
def mengecek_produk_dalam_dict (input_nama_kolom_produk,input_nilai_produk):
    while True:
        bool_data_tersedia = False
        if input_nama_kolom_produk == 'Kode Produk':
            for i in dict_data_produk.keys():
                if i == input_nilai_produk:
                    tampilan_data_tertentu (input_nama_kolom_produk,input_nilai_produk)
                    bool_data_tersedia = True
                    break
            if bool_data_tersedia == False:
                print ('\n\033[1mData Tidak Tersedia\033[0m\n')
                break
            break
        else:
            for i in dict_data_produk.keys():
                if dict_data_produk[i][input_nama_kolom_produk] == input_nilai_produk:
                    tampilan_data_tertentu (input_nama_kolom_produk,input_nilai_produk)
                    bool_data_tersedia = True
                    break
            if bool_data_tersedia == False:
                print ('\n\033[1mData Tidak Tersedia\033[0m\n')
                break
            break

# function menampilkan data tertentu
def tampilan_data_tertentu (input_nama_kolom_produk,input_kode_produk):
    global dict_data_produk
    dict_data_produk = (dict(sorted(dict_data_produk.items())))
    print ('\n================================================================================')
    for i in (((list(dict_data_produk.values()))[0]).keys()):
        if i == 'Nama Produk':
            print ("\033[1m|{:^15}|\033[0m".format('Kode Produk'),end="")
        print ("\033[1m{:^15}|\033[0m".format(i),end="")
    print ('\n--------------------------------------------------------------------------------')
    if input_nama_kolom_produk == 'Kode Produk':
        list_hasil=[]
        for i in dict_data_produk.keys():
            list_dummy =[]
            if i == input_kode_produk:
                print ("|"+" "*5 + "{:04d}".format(i)+" "*6+"|",end="")
                list_dummy.append(i)
                for j in dict_data_produk[i].keys():
                    print ("{:^15}|".format(dict_data_produk[i][j]),end="")
                    list_dummy.append(dict_data_produk[i][j])
                print ()
            if list_dummy != []:
                list_hasil.append(list_dummy)
    
    else:
        list_hasil=[]
        for i in dict_data_produk.keys():
            list_dummy =[]
            if dict_data_produk[i][input_nama_kolom_produk] == input_kode_produk:
                print ("|"+" "*5 + "{:04d}".format(i)+" "*6+"|",end="")
                list_dummy.append(i)
                for j in dict_data_produk[i].keys():
                    print ("{:^15}|".format(dict_data_produk[i][j]),end="")
                    list_dummy.append(dict_data_produk[i][j])
                print ()
            if list_dummy != []:
                list_hasil.append(list_dummy)
    print ('--------------------------------------------------------------------------------')
    return list_hasil

#function menu 2
def menu_2 ():
    while True:
        input_submenu2 = cek_input_menu ('''\033[1m
++++++++++++++++++++++++++++++++++++SUBMENU 2++++++++++++++++++++++++++++++++++++++
--------------------------------Menambahkan Data-----------------------------------
\033[0m
Menu :
1. Menambahkan Data
2. Kembali Ke Menu Utama

Masukkan submenu yang ingin dipilih : ''')
        if input_submenu2 == 1:
            menu_2_submenu_1()
        elif input_submenu2 == 2:
            break
        else:
            print ('\n\033[1mNilai input submenu yang dimasukkan salah. Harap masukkan kembali angka 1-3.\033[0m')

# function menu_2_submenu_1 menambahkan data baru
def menu_2_submenu_1 ():
    while True:
        bool_check_kode_produk = False
        input_kode_produk_baru = cek_value_kode_produk ('Masukkan Kode Produk baru : ')
        for i in dict_data_produk:
            if i == input_kode_produk_baru:
                print ('\n\033[1mNilai kode produk sudah ada.\033[0m')
                bool_check_kode_produk = True
        if bool_check_kode_produk == True:
            break
        input_nama_produk_baru = cek_value_nama_produk ('Masukkan Nama Produk baru : ')
        input_stock_produk_baru = cek_value_stock ('Masukkan Stock Produk baru : ')
        input_stock_satuan_baru = cek_value_satuan ('Masukkan Satuan baru (Bal / Dus / Pcs / Lusin / Pak) :')
        input_lokasi_satuan_baru = cek_value_lokasi ('Masukkan lokasi produk baru (Gudang A / Gudang B):')
        print ('================================================================================')
        print ("\033[1m|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|\033[0m".format('Kode Produk','Nama Produk', 'Stock', 'Satuan', 'Lokasi'))
        print ('--------------------------------------------------------------------------------')
        print ("|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|".format(input_kode_produk_baru,
                                                            input_nama_produk_baru, 
                                                            input_stock_produk_baru, 
                                                            input_stock_satuan_baru, 
                                                            input_lokasi_satuan_baru))
        print ('--------------------------------------------------------------------------------')
        while True:
            input_pilihan_simpan = input ('\nApakah data baru ini ingin dimasukkan ke database ? (Y/N)').capitalize()
            if input_pilihan_simpan == 'Y':
                dict_data_produk [input_kode_produk_baru] = {'Nama Produk':input_nama_produk_baru,
                                                        'Stock':input_stock_produk_baru,
                                                        'Satuan':input_stock_satuan_baru,
                                                        'Lokasi':input_lokasi_satuan_baru}
                print ('\n\033[1mData Baru Tersimpan\033[0m')
                break
            elif input_pilihan_simpan == 'N':
                break
            else:
                print ('\033[1mNilai yang anda masukkan salah. Harap masukkan Y atau N\033[0m')
        break

# menu_3
def menu_3 ():
    while True:
        input_submenu_3 = cek_input_menu('''\033[1m
++++++++++++++++++++++++++++++++++++SUBMENU 3++++++++++++++++++++++++++++++++++++++
-------------------------------Memperbaharui Data----------------------------------
\033[0m
Menu :
1. Memperbaharui Data
2. Kembali Ke Menu Utama

Masukkan submenu yang ingin dipilih : ''')
        if input_submenu_3 == 1:
            if len(dict_data_produk)==0:             # Pengecekan apakah data tersedia atau tidak
                print ('\033[1mData Tidak Tersedia\033[0m')
            else:
                menu_3_submenu_1 ()
        elif input_submenu_3 == 2:
            break
        else:
            print ('\n\033[1mNilai input submenu yang dimasukkan salah. Harap masukkan kembali angka 1-3.\033[0m')

# menu_3_submenu_1 memperbaharui data
def menu_3_submenu_1 ():
    while True :
        menu_1_submenu_1 ()
        input_kolom_produk = (input('''
Input Kolom yang tersedia:
1. Kode Produk
2. Nama Produk
3. Lokasi
Masukkan Input Nama Kolom : '''))
        if input_kolom_produk == '1':
            input_kolom_produk = 'Kode Produk'
            input_kolom_nilai_produk = cek_value_kode_produk('Masukkan Kode Produk untuk ditampilkan yang ingin diperbaharui : ')
            nilai_index_kolom = menu_3_submenu_1_cek_kode (input_kolom_produk,input_kolom_nilai_produk)
            if nilai_index_kolom == False:
                break
            else :
                menu_3_submenu_1_update_data (nilai_index_kolom)
                break
        elif input_kolom_produk == '2':
            input_kolom_produk = 'Nama Produk'
            input_kolom_nilai_produk = cek_value_nama_produk ('Masukkan Nama Produk untuk ditampilkan yang ingin diperbaharui (Gudang A / Gudang B): ')
            nilai_index_kolom = menu_3_submenu_1_cek_kode (input_kolom_produk,input_kolom_nilai_produk)
            if nilai_index_kolom == False:
                break
            else:
                menu_3_submenu_1_update_data (nilai_index_kolom)
                break
        elif input_kolom_produk == '3':
            input_kolom_produk = 'Lokasi'
            input_kolom_nilai_produk = cek_value_lokasi ('Masukkan Lokasi untuk ditampilkan yang ingin diperbaharui: ')
            nilai_index_kolom = menu_3_submenu_1_cek_kode (input_kolom_produk,input_kolom_nilai_produk)
            if nilai_index_kolom == False:
                break
            else:
                menu_3_submenu_1_update_data (nilai_index_kolom)
                break
        else:
            print ('\033[1mKolom Tidak Tersedia. Harap masukkan kembali nama Kolom.\033[0m')

# function menu_3_submenu_1_cek_kode mengecek nilai produk pada data (dict)
def menu_3_submenu_1_cek_kode (input_nama_kolom_produk,input_nilai_produk):
    bool_data_tersedia = False
    if input_nama_kolom_produk == 'Kode Produk':
        for i in dict_data_produk.keys():
            if i == input_nilai_produk:
                hasil_list = tampilan_data_tertentu (input_nama_kolom_produk,input_nilai_produk)
                bool_data_tersedia = True
                return hasil_list
    if input_nama_kolom_produk == 'Nama Produk' or input_nama_kolom_produk == 'Lokasi' :
        for i in dict_data_produk.keys():
            if dict_data_produk[i][input_nama_kolom_produk] == input_nilai_produk:
                hasil_list = tampilan_data_tertentu (input_nama_kolom_produk,input_nilai_produk)
                bool_data_tersedia = True
                return hasil_list
    if bool_data_tersedia == False:
        print ('\n\033[1mData Tidak Tersedia\033[0m\n')
        return bool_data_tersedia
    
# function menu_3_submenu_1_update_data memperbaharui data
def menu_3_submenu_1_update_data  (nilai_index):
    while True:
        input_pilihan_simpan = input ('\nApakah ingin memperbaharui data ini  ? (Y/N)').capitalize()
        if input_pilihan_simpan == 'Y':
            while True :
                input_kolom_diupdate = input ('''
Input Kolom yang tersedia :
1. Kode Produk
2. Nama Produk
3. Stock
4. Satuan
5. Lokasi
Masukkan Input Nama Kolom yang ingin diperbaharui : ''')
                if input_kolom_diupdate == '1':
                    input_kolom_diupdate = 'Kode Produk'

                    while True:
                        input_nilai_diupdate = cek_value_kode_produk ('Masukkan Nilai Kode Produk baru yang ingin diperbaharui : ')
                        bool_cek = True
                        for i in dict_data_produk:
                            if i == input_nilai_diupdate:
                                print ('\033[1mKode Produk sudah terdaftar. Harap masukkan nilai lain.\033[0m\n')    
                                bool_cek = False
                        if bool_cek == True:
                            break
                    
                    # menampilkan data dengan nilai yang diperbaharui
                    print ('================================================================================')
                    print ("\033[1m|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|\033[0m".format('Kode Produk','Nama Produk', 'Stock', 'Satuan', 'Lokasi'))
                    print ('--------------------------------------------------------------------------------')
                    for i in nilai_index[0]:
                        if i == nilai_index[0][0]:
                            print ("|"+" "*5 + "{:04d}".format(input_nilai_diupdate)+" "*6+"|",end="")
                        else:
                            print ("{:^15}|".format(i),end="")
                    print ('\n--------------------------------------------------------------------------------\n')

                    # konfirmasi update
                    while True:
                        input_konfirmasi_update = input ('Apakah anda yakin ingin memperbaharui data menjadi seperti ini ? (Y/N)').title()
                        if input_konfirmasi_update == 'Y':
                            dict_data_produk [input_nilai_diupdate] = dict_data_produk.pop(nilai_index[0][0])
                            print ('\nData Terupdate\n')
                            break
                        elif input_konfirmasi_update == 'N':
                            break
                        else : 
                            print ('\033[1mNilai yang anda masukkan salah. Harap masukkan Y atau N\033[0m')
                    break
                
                elif input_kolom_diupdate == '2' or input_kolom_diupdate == '3' or input_kolom_diupdate == '4' or input_kolom_diupdate == '5':
                    if input_kolom_diupdate == '2':
                        input_nama_kolom_diupdate = 'Nama Produk'
                    elif input_kolom_diupdate == '3':
                        input_nama_kolom_diupdate = 'Stock'
                    elif input_kolom_diupdate == '4':
                        input_nama_kolom_diupdate = 'Satuan'
                    elif input_kolom_diupdate == '5':
                        input_nama_kolom_diupdate = 'Lokasi'
                    for i in (((list(dict_data_produk.values()))[0]).keys()):
                        if i == input_nama_kolom_diupdate:
                            if i == 'Nama Produk':
                                input_nilai_diupdate = cek_value_nama_produk ('Masukkan Nama Produk baru yang ingin diperbaharui : ')
                            elif i == 'Stock':
                                input_nilai_diupdate = cek_value_stock ('Masukkan Stock baru ingin diperbaharui : ')
                            elif i == 'Satuan' :
                                input_nilai_diupdate = cek_value_satuan ('Masukkan Satuan baru yang ingin diperbaharui (Bal / Dus / Pcs / Lusin / Pak) : ').title()
                            elif i == 'Lokasi':
                                input_nilai_diupdate = cek_value_lokasi ('Masukkan Lokasi baru yang ingin diperbaharui (Gudang A / Gudang B) : ')
                            
                            # menampilkan data dengan nilai data yang diperbaharui
                            print ('================================================================================')
                            print ("\033[1m|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|\033[0m".format('Kode Produk','Nama Produk', 'Stock', 'Satuan', 'Lokasi'))
                            print ('--------------------------------------------------------------------------------')
                            for i in range(len(nilai_index)):
                                x=False
                                for j in nilai_index[i]:
                                    if j == nilai_index[i][0] and x==False: # condition pertama
                                        print ("|{:^15}|".format(j),end="")
                                        x=True
                                    elif j == nilai_index[i][int(input_kolom_diupdate)-1]:
                                        print ("{:^15}|".format(input_nilai_diupdate),end="")
                                    else:
                                        print ("{:^15}|".format(j),end="")
                                if i == len(nilai_index)-1:
                                    continue
                                else:
                                    print ("")
                            print ('\n--------------------------------------------------------------------------------\n')

                            # konfirmasi update
                            while True : 
                                input_konfirmasi_update = input ('Apakah anda yakin ingin memperbaharui data menjadi seperti ini ? (Y/N)').title()
                                if input_konfirmasi_update == 'Y':
                                    for i in range (len(nilai_index)): # update dengan nilai baru
                                        dict_data_produk [nilai_index[i][0]][input_nama_kolom_diupdate]=input_nilai_diupdate
                                    print ('\nData Terupdate\n')
                                    break
                                elif input_konfirmasi_update == 'N':
                                    break
                                else:
                                    print ('\033[1mNilai yang anda masukkan salah. Harap masukkan Y atau N\033[0m\n')
                    break # keluar dari looping while input kolom
                else :
                    print ('\033[1mKolom input tidak tersedia. Mohon masukkan ulang\033[0m')
            break # keluar dari looping while utama
        elif input_pilihan_simpan == 'N':
            break
        else:
            print ('\033[1mNilai yang anda masukkan salah. Harap masukkan Y atau N\033[0m')

# function cek value lokasi harus Gudang A atau Gudang B
def cek_value_lokasi (input_pertanyaan):
    while True:
        lokasi = input (input_pertanyaan).title()
        if lokasi == 'Gudang A' or lokasi == 'Gudang B':
            return lokasi
        else:
            print ('\033[1mInput yang dimasukkan salah. Mohon masukkan ulang.\033[0m\n')

# function cek value stock harus int dan maksimal 9999
def cek_value_stock (input_pertanyaan):
    while True:
        stock = input (input_pertanyaan)
        if stock.isnumeric():
            stock = int (stock)
            if stock > 9999 :
                print ('\033[1mMaksimal stock produk bernilai 9999. Mohon masukkan ulang\033[0m\n')
            else :
                return stock
        else:
            print ('\033[1mStock harus bernilai angka dan tidak bisa bernilai negatif. Mohon masukkan ulang\033[0m\n')

# function cek value kode_produk maksimal 4 digit angka
def cek_value_kode_produk (input_pertanyaan):
    while True:
        kode_produk = input (input_pertanyaan)
        if kode_produk.isnumeric():
            kode_produk = int (kode_produk)
            if kode_produk > 9999:
                    print ('\033[1mMohon masukkan kode produk dengan maks 4 digit angka.\033[0m\n')
                    continue
            else:
                return kode_produk
        print ('\033[1mKode produk harus bernilai angka dan tidak bisa bernilai negatif. Mohon masukkan ulang\033[0m\n')

# function cek value nama_produk harus string dan maks 15 karakter
def cek_value_nama_produk (input_pertanyaan):
     while True:
        nama_produk = input(input_pertanyaan).title()
        if len(nama_produk) > 15 :
            print ('\033[1mJumlah karakter maksimal 15. Mohon masukkan ulang\033[0m\n')
        elif nama_produk.isalpha():
            return nama_produk
        else :
            print ('\033[1mNama produk tidak bisa bernilai angka. Mohon masukkan ulang\033[0m\n')
            #return nama_produk

# function cek value nama_produk harus (Bal/Dus/Pcs/Lusin/Pak)
def cek_value_satuan (input_pertanyaan):
     while True:
        nama_satuan = input(input_pertanyaan).title()
        if nama_satuan == 'Bal' or nama_satuan == 'Dus' or nama_satuan == 'Pcs' or nama_satuan == 'Lusin' or nama_satuan == 'Pak' :
            return nama_satuan
        else :
            print ('\033[1mNama satuan tidak sesuai. Mohon masukka ulang\033[0m\n')
            #return nama_produk

# function menu_4
def menu_4 ():
    while True:
        input_submenu_4=cek_input_menu('''\033[1m
++++++++++++++++++++++++++++++++++++SUBMENU 4++++++++++++++++++++++++++++++++++++++
--------------------------------- Menghapus Data-----------------------------------
\033[0m
Menu :
1. Menghapus Data
2. Kembali Ke Menu Utama

Masukkan submenu yang ingin dipilih : ''')
        if input_submenu_4 == 1:
            if len(dict_data_produk)==0:             # Pengecekan apakah data tersedia atau tidak
                print ('\033[1mData Tidak Tersedia\033[0m')
            else:
                menu_4_submenu_1 ()
        elif input_submenu_4 == 2:
            break
        else:
            print ('\033[1m\nNilai input submenu yang dimasukkan salah. Harap masukkan kembali angka 1-2.\033[0m')

# function menu_4_submenu_1
def menu_4_submenu_1 ():
    menu_1_submenu_1()
    while True:
        input_kolom_produk = (input('''
Input Kolom yang tersedia : 
1. Kode Produk
2. Nama Produk
3. Lokasi
Masukkan Input Nama Kolom : '''))
        input_kolom_nilai_produk = ""
        if input_kolom_produk == '1' or input_kolom_produk == '2' or input_kolom_produk == '3':
            if input_kolom_produk == '1':
                input_kolom_produk = 'Kode Produk'
                input_kolom_nilai_produk = cek_value_kode_produk ('Masukkan Kode Produk yang ingin ditampilkan : ')
            elif input_kolom_produk == '2':  
                input_kolom_produk = 'Nama Produk' 
                input_kolom_nilai_produk = cek_value_nama_produk ('Masukkan Nama Produk yang ingin ditampilkan : ')
            elif input_kolom_produk == '3':
                input_kolom_produk = 'Lokasi' 
                input_kolom_nilai_produk = cek_value_lokasi ('Masukkan Lokasi yang ingin ditampilkan (Gudang A / Gudang B) : ')  

            hasil_cek = menu_4_submenu_1_cek_kode (input_kolom_produk,input_kolom_nilai_produk)

            if hasil_cek == False:
                break
            else:
                menu_4_submenu_1_hapus_data (input_kolom_produk,input_kolom_nilai_produk)
            break
        else :
            print ('\033[1mKolom Tidak Tersedia. Harap masukkan kembali nama Kolom.\033[0m')

# function menu_4_submenu_1_cek_kode
def menu_4_submenu_1_cek_kode (input_nama_kolom_produk,input_nilai_produk):
    while True :
        bool_data_tersedia = False
        if input_nama_kolom_produk == 'Kode Produk':
            for i in dict_data_produk.keys():
                if i == input_nilai_produk:
                    tampilan_data_tertentu (input_nama_kolom_produk,input_nilai_produk)
                    bool_data_tersedia = True
                    break
            if bool_data_tersedia == False:
                print ('\n\033[1mData Tidak Tersedia\n\033[0m')
                return bool_data_tersedia
            break
        elif input_nama_kolom_produk == 'Nama Produk' or input_nama_kolom_produk == 'Lokasi':
            for i in dict_data_produk.keys():
                if dict_data_produk[i][input_nama_kolom_produk] == input_nilai_produk:
                    tampilan_data_tertentu (input_nama_kolom_produk,input_nilai_produk)
                    bool_data_tersedia = True
                    break
            if bool_data_tersedia == False:
                print ('\n\033[1mData Tidak Tersedia\n\033[0m')
                return bool_data_tersedia
            break
        

# function menu_4_submenu_1_hapus_data
def menu_4_submenu_1_hapus_data (input_kolom_produk, input_kolom_nilai_produk):
    while True:
        input_konfirmasi_hapus = input('\nApakah anda yakin ingin menghapus data ini ? (Y/N)').capitalize()
        if input_konfirmasi_hapus == 'Y':
            if input_kolom_produk == 'Kode Produk':
                del dict_data_produk [input_kolom_nilai_produk]
                print ('\nData terhapus')
                break
            elif input_kolom_produk == 'Nama Produk' or input_kolom_produk == 'Lokasi':
                list_index_ingin_dihapus = []
                list_index_ingin_dihapus = [i for i in dict_data_produk if dict_data_produk[i][input_kolom_produk]==input_kolom_nilai_produk]
                for i in list_index_ingin_dihapus:
                    del dict_data_produk[i]
                print ('\nData terhapus')
                break
        elif input_konfirmasi_hapus == 'N':
            break
        else:
            print ('\033[1mNilai yang anda masukkan salah. Harap masukkan Y atau N\033[0m')

menu_utama()

