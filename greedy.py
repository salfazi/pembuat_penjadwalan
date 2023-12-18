class GreedyScheduler:
    def __init__(self):
        self.jadwal = []

    def tambahMataKuliah(self, mataKuliah):
        self.jadwal.append(mataKuliah)

    def apakahRuanganTersedia(self, mataKuliah):
        # Implementasi logika pengecekan ketersediaan ruangan
        # Sesuaikan sesuai dengan aturan atau batasan spesifik Anda
        # Pastikan juga memeriksa ketersediaan ruangan untuk kelas tertentu
        return True  # Gantilah dengan logika sesuai kebutuhan

    def apakahWaktuTersedia(self, mataKuliah):
        # Implementasi logika pengecekan ketersediaan waktu
        # Sesuaikan sesuai dengan aturan atau batasan spesifik Anda
        return True  # Gantilah dengan logika sesuai kebutuhan

    def optimalkanJadwal(self):
        self.jadwal.sort(key=lambda x: (x['waktuMulai'], x['kelas'], x['ruangan']))

        jadwal_optimalkan = []

        for mataKuliah in self.jadwal:
            ruangan_tersedia = self.apakahRuanganTersedia(mataKuliah)
            waktu_tersedia = self.apakahWaktuTersedia(mataKuliah)

            if ruangan_tersedia and waktu_tersedia:
                jadwal_optimalkan.append(mataKuliah)

        return jadwal_optimalkan


# Contoh Penggunaan
scheduler = GreedyScheduler()

# Input pengguna untuk menambahkan mata kuliah
jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: "))

print("=================================================================")
for i in range(1, jumlah_mata_kuliah + 1):
    nama_mata_kuliah = input(f"Masukkan nama mata kuliah ke-{i}: ")
    kelas = input(f"Masukkan kelas untuk {nama_mata_kuliah}: ")
    ruangan = input(f"Masukkan ruangan untuk {nama_mata_kuliah}: ")
    waktu_mulai = int(input(f"Masukkan waktu mulai untuk {nama_mata_kuliah} (contoh: 8 untuk pukul 8:00): "))
    waktu_selesai = int(input(f"Masukkan waktu selesai untuk {nama_mata_kuliah} (contoh: 10 untuk pukul 10:00): "))
    print("=================================================================")

    # Tambahkan mata kuliah ke dalam jadwal
    scheduler.tambahMataKuliah({'namaMataKuliah': nama_mata_kuliah, 'kelas': kelas, 'ruangan': ruangan, 'waktuMulai': waktu_mulai, 'waktuSelesai': waktu_selesai})

# Optimalkan jadwal menggunakan Algoritma Greedy
jadwal_optimalkan = scheduler.optimalkanJadwal()

# Tampilkan jadwal yang sudah dioptimalkan dengan format yang lebih terstruktur
print("Jadwal yang Dioptimalkan:")
for mataKuliah in jadwal_optimalkan:
    print(f"Mata Kuliah: {mataKuliah['namaMataKuliah']}")
    print(f"Kelas: {mataKuliah['kelas']}")
    print(f"Ruangan: {mataKuliah['ruangan']}")
    print(f"Waktu Mulai: {mataKuliah['waktuMulai']}")
    print(f"Waktu Selesai: {mataKuliah['waktuSelesai']}\n")
