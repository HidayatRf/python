import os
os.system("clear")

print('\n==================\n')
data_user_nama = ""
data_user_password = ""
data_teams = [	
	{
		"nama": "reza fairuz h",
		"umur": 17,
		"job": "front end",
		"skills": ["html", "css", "python", "javascript"]
	},
	{
		"nama": "m rizky sanjaya",
		"umur": 20,
		"job": "front end",
		"skills": ["html", "css", "javascript"]
	},
	{
		"nama": "nathael surta athana",
		"umur": 19,
		"job": "back end",
		"skills": ["nodeJs", "python", "laravel", "php"]
	},
]

def main():
	if data_user_nama == "":
		register()
		question = input("apakah anda ingin log-in ( y/n ) : ").lower()
		if question == "y":
			os.system("clear")
			log_in()
			print("silahkan masukan pilihan anda")
			while True:
				question = input("( tambah | hapus | edit | list )\n -|:").lower()
				if question == "tambah":
					add_data(data_teams)
					print(data_teams)
				elif question == "hapus":
					delete_data(data_teams)
				elif question == "edit":
					update_data(data_teams)
				elif question == "list":
					list_all_data(data_teams)
				else:
					print("kamu telah berhenti dalam mengedit data")
					print("data kamu")
					break
		else:
			print("terimakasih telah berkunjung")

def register():
	global data_user_nama, data_user_password
	
	print("register section")
	print("silahkan registrasi")	
	
	while True:
		user_nama = input("masukan nama : ")
		password = input("masukan password : ")
		user_data = {"nama": [], "password": []}	
		
		for i in user_nama:
			user_data["nama"].append(i)
	#	===============================	#	
		for i in password:
			user_data['password'].append(i)
			
		if len(user_data['nama']) <= 4 and len(user_data['password']) <= 6:
			print("maaf nama dan passwor anda terlalu pendek")
		else:
			data_user_nama = user_nama
			data_user_password = password
			print("anda berhasil register")
			print(f"selemat datang {user_nama}")
			return True

def log_in():
	print("\nlog-in section")
	print("silahkan masukan nama yang sesuai\n")
	
	while True:
		user_nama = input("masukan nama anda : ")
		password = input("masukan password anda : ")
		if user_nama == data_user_nama and password == data_user_password:
			print(f"selamat datang {user_nama}")
			print("setelah kamu log-in kamu menjadi bisa untuk")
			print("( menambah | menghapus | edit | menampilkan ) data")
			return
		else:
			print("maaf data yang anda masukan salah")

def add_data(datas):
	your_data = {
		"nama": input("masukan nama : "),
		"umur": int(input("masukan umur : ")),
		"job": input("masukan jenis job : "),
		"skills": input("masukan skills example1, example2 : ").split(',')
	}
	
	for i, data in enumerate(datas):
		print(data['nama'])
		if data['nama'] != your_data['nama']:
			datas.append(your_data)
			print("data sukses ditambahkan\n")
			break
		else:
			while True:
				print("data sama")
				your_data = {
					"nama": input("masukan nama : "),
					"umur": int(input("masukan umur : ")),
					"job": input("masukan jenis job : "),
					"skills": input("masukan skills example1, example2 : ").split(',')
				}
					
				if your_data['nama'] != data['nama']:
					datas.append(your_data)
					print("data sukses ditambahkan\n")
					break

def list_all_data(datas):
	for i, data in enumerate(datas):
		print(f"nama : {data['nama']}")
		print(f"umur : {data['umur']}")
		print(f"job : {data['job']}")
		print(f"skill : {data['skills']}\n")

def delete_data(datas):
	print('tolong hapus data dengan index\n')
	for i, data in enumerate(datas):
		print(f"index. {i + 1} : {data['nama']}")
	
	question = int(input("hapus : "))
	for i, data in enumerate(datas):
		if question - 1 == i:
			datas.pop(question - 1)

def update_data(datas):
	print("daftar nama : ")
	for data in datas:
		print(f"nama : {data['nama']}")
	
	question = input("\ntolong masukan nama yang ingin di ubah : ")
	for data in datas:
		if question == data['nama']:
			print(f"nama sebelum : {data['nama']}")
			update_nama = input("masukan nama baru : ")
			data['nama'] = update_nama
			print(f"umur sebelum : {data['umur']}")
			update_umur = int(input("masukan nama baru : "))
			data['umur'] = update_umur
			print(f"job sebelum : {data['job']}")
			update_job = input("masukan job baru : ")
			data['job'] = update_job
			
			while True:
				print("\nmenambah skill ( add )")
				print("mengedit skill ( edit )")
				print("mengahapus skill ( remove )")
				print("\n")
				skill_container = ""
				for i, value in enumerate(data['skills']):
					skill_container += f"index {i + 1} : {value}\n"
				
				question = input("tentukan pilihan : ")
				for i, value in enumerate(data['skills']):
					if question == "add":
						print(skill_container)
						print("masukan skill baru")
						skill_baru = input("-|:")
						data['skills'].append(skill_baru)
						print("skill baru sudah berhasil ditambahkan")
						print(data['skills'])
						break
					
					elif question == "edit":
						print(skill_container)
						print("masukan pilihan sesuai index")
						question = int(input("-|:"))
						if question - 1 == i:
							print(f"add function data : {value}")
							break
						
					elif question == "remove":
						print(skill_container)
						print("masukan pilihan sesuai index")
						question = int(input("-|:"))
						if question - 1 == i:
							print(f"add function data : {value}")
							break

main()

print('\n==================\n')
