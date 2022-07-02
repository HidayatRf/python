# membuat log in sederhana dengan python 
## hasil belajar [ IF ELSE | ELIF ]

data_nama = ""
data_password = ""



input_user = input("sikahkan register tekan Y untuk lanjut : ")
if input_user == "Y" or input_user == "y":
    user_nama = input("masukan nama anda : ")
    user_pass = input("masukan password : ")
    data_nama = user_nama
    data_password = user_pass

    pertanyaan = input("apakah anda ingin log-in yes/else: ")
    if pertanyaan == "yes":
        user_nama = input("Masukan nama : ")
        if user_nama == data_nama:
            user_pass = input("Masukan password : ")
            if user_pass == data_password:
                print("login succsess")
        else:
            while True:
                user_nama = input("Tolong Masukan nama yang benar: ")
                if user_nama == data_nama:
                    user_pass = input("masukan password : ")
                    if user_pass == data_password:
                        print("login succsess 2")
                        break

                        
    else: 
        print(f"""terimakasih telah register! 
data anda nama : {data_nama} 
password : {data_password}""")






