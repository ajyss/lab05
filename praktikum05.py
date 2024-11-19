def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

def tampilkan_menu():
    print("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari (K)eluar]:"), 

def tampilkan_daftar(data_mahasiswa):
    print("\nDaftar Nilai")
    print("=" * 62)
    print("| NO |    NIM    |      NAMA      | TUGAS | UTS | UAS | AKHIR |")
    print("=" * 62)
    
    if not data_mahasiswa:
        print("|                     TIDAK ADA DATA                            |")
    else:
        for idx, (nim, data) in enumerate(data_mahasiswa.items(), 1):
            print("| {:<2} | {:<9} | {:<13} | {:<5} | {:<3} | {:<3} | {:<5.2f} |".format(
                idx, nim, data['nama'], 
                data['tugas'], data['uts'], data['uas'], 
                data['nilai_akhir']
            ))
    
    print("=" * 62)

def tambah_data(data_mahasiswa):
    print("\nTambah Data")
    nim = input("NIM        : ")
    nama = input("Nama       : ")
    tugas = int(input("Nilai Tugas: "))
    uts = int(input("Nilai UTS  : "))
    uas = int(input("Nilai UAS  : "))
    
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    
    data_mahasiswa[nim] = {
        'nama': nama,
        'tugas': tugas,
        'uts': uts,
        'uas': uas,
        'nilai_akhir': nilai_akhir
    }

def main():
    data_mahasiswa = {}
    while True:
        tampilkan_menu()
        pilihan = input().lower()
        
        if pilihan == 'l':
            tampilkan_daftar(data_mahasiswa)
        elif pilihan == 't':
            tambah_data(data_mahasiswa)
            tampilkan_daftar(data_mahasiswa)
        elif pilihan == 'u':

            pass
        elif pilihan == 'h':
           
            pass
        elif pilihan == 'c':
            
            pass
        elif pilihan == 'k':
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    print("Input Nilai")
    print("=" * 18)
    main()