# Evaluasi Tengah Semester Mata Kuliah Integrasi Sistem

Project ini merupakan aplikasi web simpel untuk mencari lowongan pekerjaan dan membuat lowongan pekerjaan.

# Anggota

| Nama                            | NRP          |
| ------------------------------- | ------------ |
| Marcelinus Alvinanda Chrisantya | `5027221012` |

# 1. Project memiliki ketentuan sebagai berikut:

    • Memiliki fitur Create, Read, Update, Delete data

    • Koneksi ke database (MongoDB atau yang lainnya)

    • Backend CRUD ke database

    • Mengimplementasikan UI

# 2. Cara menjalankan Project

a. Install semua module yang diperlukan, mulai dari GRPC, GRPC-Tools, Flask, Proto, dan lain sebagainya.

b. Compile file protobuf yang sudah dibuat berdasarkan service yang ingin digunakan menggunakan command berikut: 
```
python -m grpc_tools.protoc --proto_path=protobuf --python_out=backend --grpc_python_out=backend protobuf/jobs.proto  
```
c. Setelah itu jalankan file server.py sebagai backend yang akan berhubungan dengan database yang digunakan *saya menggunakan MongoDB. Berikut cara menjalankannya:

```
python ./server.py
```

d. Langkah berikutnya saya menjalankan app.py yang berisi module Flask untuk menghubungkan antara backend dengan frontend yang digunakan *saya menggunakan html. Berikut cara menjalankannya:

```
python ./app.py
```