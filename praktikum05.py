class StudentGradeSystem:
    def __init__(self):  # Perbaikan: gunakan __init__ bukan _init_
        self.students = {}  # Dictionary untuk menyimpan data mahasiswa
        
    def calculate_final_grade(self, task, uts, uas):
        """Menghitung nilai akhir berdasarkan komponen nilai"""
        return (task * 0.30) + (uts * 0.35) + (uas * 0.35)
    
    def add_student(self):
        """Menambah data mahasiswa baru"""
        print("\nTambah Data")
        nim = input("NIM      : ")
        if nim in self.students:
            print("NIM sudah terdaftar!")
            return
            
        name = input("Nama     : ")
        try:
            task = float(input("Nilai Tugas : "))
            uts = float(input("Nilai UTS   : "))
            uas = float(input("Nilai UAS   : "))
            
            if not all(0 <= score <= 100 for score in [task, uts, uas]):
                print("Nilai harus berada dalam rentang 0-100!")
                return
                
            final = self.calculate_final_grade(task, uts, uas)
            self.students[nim] = {
                'nama': name,
                'tugas': task,
                'uts': uts,
                'uas': uas,
                'akhir': final
            }
            print("Data berhasil ditambahkan!")
        except ValueError:
            print("Input nilai harus berupa angka!")
    
    def update_student(self):
        """Mengubah data mahasiswa"""
        print("\nUbah Data")
        nim = input("Masukkan NIM yang akan diubah: ")
        if nim not in self.students:
            print("NIM tidak ditemukan!")
            return
            
        try:
            name = input("Nama baru     : ")
            task = float(input("Nilai Tugas   : "))
            uts = float(input("Nilai UTS     : "))
            uas = float(input("Nilai UAS     : "))
            
            if not all(0 <= score <= 100 for score in [task, uts, uas]):
                print("Nilai harus berada dalam rentang 0-100!")
                return
                
            final = self.calculate_final_grade(task, uts, uas)
            self.students[nim].update({
                'nama': name,
                'tugas': task,
                'uts': uts,
                'uas': uas,
                'akhir': final
            })
            print("Data berhasil diubah!")
        except ValueError:
            print("Input nilai harus berupa angka!")
    
    def delete_student(self):
        """Menghapus data mahasiswa"""
        print("\nHapus Data")
        nim = input("Masukkan NIM yang akan dihapus: ")
        if nim in self.students:
            del self.students[nim]
            print("Data berhasil dihapus!")
        else:
            print("NIM tidak ditemukan!")
    
    def search_student(self):
        """Mencari data mahasiswa"""
        print("\nCari Data")
        nim = input("Masukkan NIM yang dicari: ")
        if nim in self.students:
            student = self.students[nim]
            self.display_header()
            print(f"| 1 | {nim:^6} | {student['nama']:<15} | {student['tugas']:^5} | "
                  f"{student['uts']:^5} | {student['uas']:^5} | {student['akhir']:^6.2f} |")
            self.display_footer()
        else:
            print("NIM tidak ditemukan!")
    
    def display_header(self):
        """Menampilkan header tabel"""
        print("\nDaftar Nilai")
        print("=" * 65)
        print("| NO | NIM    | NAMA           | TUGAS | UTS  | UAS  | AKHIR |")
        print("=" * 65)
    
    def display_footer(self):
        """Menampilkan footer tabel"""
        print("=" * 65)
    
    def display_students(self):
        """Menampilkan semua data mahasiswa"""
        if not self.students:
            print("\nDaftar Nilai")
            print("=" * 65)
            print("|                      TIDAK ADA DATA                           |")
            print("=" * 65)
            return
            
        self.display_header()
        for idx, (nim, student) in enumerate(self.students.items(), 1):
            print(f"| {idx:2} | {nim:^6} | {student['nama']:<15} | {student['tugas']:^5} | "
                  f"{student['uts']:^5} | {student['uas']:^5} | {student['akhir']:^6.2f} |")
        self.display_footer()
    
    def run(self):
        """Menjalankan program utama"""
        menu = {
            'l': self.display_students,
            't': self.add_student,
            'u': self.update_student,
            'h': self.delete_student,
            'c': self.search_student
        }
        
        while True:
            print("\nProgram Input Nilai")
            print("=" * 20)
            print("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari (K)eluar]")
            choice = input().lower()
            
            if choice == 'k':
                print("Program selesai, sampai jumpa!")
                break
            elif choice in menu:
                menu[choice]()
            else:
                print("Menu tidak valid!")

if __name__ == "__main__":  # Perbaikan: gunakan __name__ bukan _name_
    system = StudentGradeSystem()
    system.run()