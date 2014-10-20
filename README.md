Mamushi
=======

Python based chatting room application

														Spesifikasi Protokol Chat Room
																Kelompok X
														5111100086 Muhammad Bagus Andra
														5112100024 Hafieludin Yusuf Rizana
														5112100122 Ratih Ayuh Indraswari
														5112100137 Pradipta Ghusti
														5112100144 Dimas Widdy Pratama
														5112100161 Soca Gumilar 


1.	 Pendahuluan

	Dokumen spesifikasi ini dibuat dengan tujuan menjelaskan dan memaparkan secara detil 
	protokol yang kelompok kami buat untuk aplikasi chatting. Aplikasi chatting yang kami
	buat berbasiskan ruangan (Chat Room),tujuan dari pembuatan aplikasi ini adalah agar
	beberapa pengguna dapat berkomunikasi dan berkolaborasi dalam suatu tempat tanpat harus
	bertemu tatap muka secara langsung.

	Penjabaran protokol yang dipakai pada dokumen ini dimaksudkan agar pengembang lain dapat
	melakukan pengembangan aplikasi yang dapat terhubung dengan aplikasi kami tanpa harus 
	dibatasi oleh bahasa pemrograman , kerangka kerja ataupun lingkungan sistem yang dipakai.
	dengan menggunakan protokol yang sama maka beberapa aplikasi yang berbeda dapat saling
	terhubung dan berkomunikasi dengan syarat pembuatan aplikasi itu mematuhi protokol yang
	dijabarkan pada dokumen ini.

2.	 Terminologi
	
	Server
	 Aplikasi yang berfungsi melayani aplikasi client yang terhubung

	Client
	 Aplikasi yang digunakan oleh user , terhubung dengan server untuk
	 melakukan komunikasi 

	User
	 Pengguna aplikasi

	Chat Room
	 Ruangan tempat user dapat berkumpul dan melakukan komunikasi dengan cara
	 mengirim chat

	Chat
	 pesan yang dikirimkan user

	Login
	 Proses autentikasi user sebelum user dapat terhubung ke server, ditujukan
	 agar server mengetahui identitas user yang sedang berkomunikasi

	Logout
	 Proses keluar nya user dari server

	TCP
	 Transmission Control Protocol, suatu protokol pada transport layer yang
	 bersifat reliable

	Request
	 Suatu bentuk data yang dikirimkan oleh Client kepada server untuk melakukan suatu perintah

	Response
	 Suatu bentuk data yang dikirimkan oleh Server kepada Client sebagai balasan dari suatu 
	 Request


3.	 Skema Umum
	
	Skema umum dari komunikasi antar client dan server dapat digambarkan sebagai berikut


	+-------------------------+                    +-----------------------+
	|                         |                    |                       |
	|  +------------------+   |                    |                       |
	|  |   Antar Muka     |   |                    |   +----+----------+   |
	|  +--------+---------+   |                    |   | Server Program|   |
	|           |             |                    |   |               |   |
	|  Data     | ^           |        Response    |   +---------------+   |
	|           v |           |                    |                       |
	|             |           |    <---------------+                       |
	|  +----------+-------+   |                    |                       |
	|  |  Client Backend  +----------------------> |                       |
	|  +------------------+   |                    |                       |
	|                         |   Request          |                       |
	|                         |                    |                       |
	+-------------------------+                    +-----------------------+
                                                                        
        	Client                                         Server                 

    Client mengirimkan request yang berisikan perintah tertentu kepada server kemudian 
    server akan mengirim kembali response yang merupakan balasan terhadap request yang
    diterima dari client


4.	 Format Data
	
	Data request dan response yang dikirimkan dalam berkomunikasi mempunyai format tertentu
	format yang dipakai diambil dari format tipe data dictionary pada python , atau mirip juga
	dengan format json seperti berikut

	{atribut1=data1,atribut2=data2,atribut3=data3....}


5.	 Jenis Perintah

	Jenis Perintah yang dapat dikirimkan oleh client kepada server antara lain adalah

	- Melakukan registrasi
	- Melakukan Login
	- Membuat Chat room
	- Menghapus Chat room
 	- Join kedalam chat room
	- Mengirimkan pesan chat
	- Keluar dari chatroom
	- Logout dari aplikasi

5.1	 Melakukan Registrasi

	Registrasi dilakukan oleh user untuk mendapatkan autorisasi dalam menggunakan aplikasi
	setelah melakukan registrasi , data user akan disimpan di dalam server dan server akan
	mengembalikan response berhasil , sedangkan jika gagal , server akan mengembalikan response
	gagal kepada user

	Format request registrasi
	{"FLAG”=“REG” , “SENDER”=“nama_client” , “RECEIVER” = “server” , “CONTENT” ={username=“username” password=“password”} , “TYPE=“TEXT” }

	jika registrasi berhasil server akan mengembalikan response sebagai berikut

	Format response registrasi (berhasil)
	{“FLAG”=“DATA” , “CONTENT” =“anda berhasil terdaftar dengan username: user_name” , “TYPE=“TEXT” , CODE=“REG_OK”}

	jika registrasi gagal server akan mengembalikan response sebagai berikut

	Format response registrasi (gagal)
	{“FLAG”=“DATA” , “CONTENT” =“username sudah terdaftar” , “TYPE=“TEXT” , CODE=“REG_DUPE”}

5.2	 Melakukan Login

	Login dilakukan oleh user untuk mengautentikasi dirinya dalam menggunakan aplikasi pada server
	sebelum melakukan login user sudah harus terlebih dahulu terdaftar pada server. jika login berhasil
	server akan mengembalikan response berhasil sedangkan jika login gagal maka server akan mengembalikan
	response gagal

	Format request login
	{“FLAG”=“LOGIN” , “SENDER”=“nama_client” , “RECEIVER” = “server” , “CONTENT” ={username=“username” password=“password”} , “TYPE=“TEXT” }

	Format response login (berhasil)
	{“FLAG”=“DATA” , “CONTENT” =“Login berhasil: user_name” , “TYPE=“TEXT” , CODE=“LOGIN_OK”}

	Format response login gagal karena user sudah login
	{“FLAG”=“DATA” , “CONTENT” =“Login gagal , user telah ter-login” , “TYPE=“TEXT” , CODE=“LOGIN_DUPE”}

	Format response registrasi gagal karena user salah memasukkan password
	{“FLAG”=“DATA” , “CONTENT” =“Login gagal ,password salah” , “TYPE=“TEXT” , CODE=“BAD_PASS”}

	Format response registrasi gagal karena user belum terdaftar
	{“FLAG”=“DATA” , “CONTENT” =“Login gagal , user tidak ditemukan” , “TYPE=“TEXT” , CODE=“USER_NONEXIST”}

5.3	 Membuat Room

	Perintah ini dilakukan ketika user ingin membuat room , jika pembuatan room berhasil maka server akan mengembalikan
	response berhasil sedangkan jika room sudah ada maka server akan mengembalikan response gagal

	Format request membuat room
	{“FLAG”=“MAKE_ROOM” , “SENDER”=“nama_client” , “RECEIVER” = “server” , “CONTENT” =nama_room, “TYPE=“TEXT” }

	Format response membuat room (berhasil)
	{“FLAG”=“DATA” , “CONTENT” =“nama_room berhasil dibuat” , “TYPE=“TEXT” , CODE=“MAKE_ROOM_OK”}

	Format response membuat room (gagal)
	{“FLAG”=“DATA” , “CONTENT” =“nama_room sudah ada” , “TYPE=“TEXT” , CODE=“MAKE_ROOM_DUPE”}

5.4	 Menghapus Chat room
	Perintah ini dilakukan ketika user ingin menghapus room , jika penghapusan room berhasil maka server akan mengembalikan
	response berhasil sedangkan jika room tidak ada maka server akan mengembalikan response gagal

	Format request menghapus room
	{“FLAG”=“DEL_ROOM” , “SENDER”=“nama_client” , “RECEIVER” = “server” , “CONTENT” =nama_room, “TYPE=“TEXT” }

	Format response menghapus room (berhasil)
	{“FLAG”=“DATA” , “CONTENT” =“nama_room berhasil dihapus” , “TYPE=“TEXT” , CODE=“DEL_ROOM_OK”}

	Format response menghapus room (gagal)
	{“FLAG”=“DATA” , “CONTENT” =“nama_room tidak ditemukan” , “TYPE=“TEXT” , CODE=“DEL_ROOM_NOT_EXIST”}

5.5  Join Chat Room
	Perintah ini dlakukan ketika user ingin masuk atau bergabung dalam suatu chat room , jika join room berhasil maka server akan 
	mengembalikan response berhasil sedangkan jika room tidak ada  atau user sudah join maka server mengembalikan response gagal

	Format request join room
	{“FLAG”=“JOIN_ROOM” , “SENDER”=“nama_client” , “RECEIVER” = “server” , “CONTENT” =nama_room, “TYPE=“TEXT” }

	Format response join room (berhasil)
	{“FLAG”=“DATA” , “CONTENT” =“nama_room” , “TYPE=“TEXT” , CODE=“JOIN_ROOM_OK”}

	Format response join room (gagal)
	{“FLAG”=“DATA” , “CONTENT” =“tidak dapat masuk ke dalam room nama_room” , “TYPE=“TEXT” , CODE=“JOIN_ROOM_FAILED”}

5.5  Mengirimkan pesan chat
	Perintah ini dlakukan ketika user ingin mengirimkan pesan chat , user akan mengirim request yang diterima oleh server 
	yang akan di kirimkan ke ruangan tujuan chat tersebut

	Format request mengirim chat
	{“FLAG”=“SEND” , “SENDER”=“nama_client” , “RECEIVER” = “nama_room” , “CONTENT” =isi_chat, “TYPE=“TEXT” }

	Format response mengirim chat (berhasil)
	{“FLAG”=“DATA” , “CONTENT” =“chat ke room nama_room berhasil dikirim” , “TYPE=“TEXT” , CODE=“SEND_OK”}

5.6	 Keluar dari Chat Room
	Perintah ini dilakukan ketika user ingin keluar dari chatroom , user mengirim request kepada server sehingga
	server mengetahui bahwa user tersebut sudah tidak berada dalam suatu room dan server melakukan update pada list
	user yang terdapat pada suatu room

	Format request 
	{“FLAG”=“QUIT_ROOM” , “SENDER”=“nama_client” , “RECEIVER” = “nama_room” , “CONTENT” =nama_room, “TYPE=“TEXT” }

	Format response join room (berhasil)
	{“FLAG”=“DATA” , “CONTENT” =“nama_room” , “TYPE=“TEXT” , CODE=“ROOM_QUITTED”}

5.7	 Logout dari aplikasi
	Perintah ini dilakukan ketika user ingin keluar dari aplikasi , user mengirim request kepada server sehingga server
	mengetahui bahwa user tersebut tidak sedang online , dan server menghapus user tersebut dari daftar user yang 
	sedang online

	Format request 
	{“FLAG”=“LOGOUT” , “SENDER”=“nama_client” , “RECEIVER” = “server” , “CONTENT” =“ username“ TYPE=“TEXT” }
	
	Format response join room (berhasil)
	{“FLAG”=“DATA” , “CONTENT” =“username telah log out” , “TYPE=“TEXT” , CODE=“LOGOUT_OK”}




