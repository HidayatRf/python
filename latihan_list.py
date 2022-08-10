# latihan list | arr dakam python
"""
--- TODO ---
_____
 1. -| membuat data makanan | success
 2. -| menampilkan data makanan | success
 3. -| user dapat menambah dan menghapus

"""

daftar_makanan = [
        ["sushi","8.45","¥340"],
        ["shoyu ramen","9.0","¥850"],
        ["bento","8.9","¥1.200"]
]

for i,data in enumerate(daftar_makanan):
    print(f"no.{i} | nama : {data[0]} | rating : {data[1]} | harga : {data[2]}\n")


question = input("apakah anda mau menambahkan daftar makanan | y/else : ")

if question == "y" or question == "Y":
    nama_makanan = input("masukan nama makanan : ")
    rating_makanan = input("masukan rating dari makanan : ")
    harga_makanan = input("masukan harga dari makanan : ")
    print(f"nama : {nama_makanan}\nrating : {rating_makanan}\nharga : {harga_makanan}")

    question = input("apakah anda sudah puas dengan hasilnya  y/else : ")
    if question == "y" or question == "Y":
        data_makanan = [nama_makanan, rating_makanan, harga_makanan]
        daftar_makanan.append(data_makanan)
        
        question = input("tekan Y untuk menampilkan daftar makanan : ")
        if question != "y" or question == "y":
            for i,list_makanan in enumerate(daftar_makanan):
                print(f"\nno.{i} nama : {list_makanan[0]} | rating : {list_makanan[1]} | harga : {list_makanan[2]}")


    else:
        nama_makanan = input("masukan nama makanan : ")
        rating_makanan = input("masukan rating dari makanan : ")
        harga_makanan = input("masukan harga dari makanan :  ")
        data_makanan = [nama_makanan, rating_makanan, harga_makanan]
        daftar_makanan.append(data_makanan)
        for i,list_makanan in enumerate(daftar_makanan):
            print(f"no.{i} nama : {list_makanan[0]} | rating : {list_makanan[1]} | harga : {list_makanan[2]}")

else:
    for i,list_makanan in enumerate(daftar_makanan):
        print(f"no{i} nama {list_makanan[0]} | rating : {list_makanan[1]} | harga : {list_makanan[2]}")
    
        












