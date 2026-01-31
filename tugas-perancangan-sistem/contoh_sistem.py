# Contoh sederhana perancangan sistem pengelolaan data mahasiswa

data_mahasiswa = []

def tambah_mahasiswa(nama, nim):
    mahasiswa = {
        "nama": nama,
        "nim": nim
    }
    data_mahasiswa.append(mahasiswa)

def tampilkan_mahasiswa():
    for mhs in data_mahasiswa:
        print("Nama:", mhs["nama"], "| NIM:", mhs["nim"])


# Simulasi penggunaan sistem
tambah_mahasiswa("Andi", "123456")
tambah_mahasiswa("Budi", "654321")

tampilkan_mahasiswa()