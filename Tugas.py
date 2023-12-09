import pandas as pd

data = {
        'nama' : ['John', 'Jane', 'Bob', 'Alice'],
        'usia' : [25, 35, 30, 28],
        'gaji' : [50000, 60000, 70000, 55000]
}

df = pd.DataFrame(data)

df['kategori_umur'] = df['usia'].apply(lambda row: 'Muda' if row < 30 else 'Tua')

df['bonus_gaji'] = df.apply(lambda row:row['gaji']*1.05 if row['usia'] < 30 else row['gaji']*1.1, axis=1)

df['bonus_karyawan_senior'] = df.apply(lambda row:row['bonus_gaji']*2 if row['usia'] >= 30 else row['bonus_gaji']*1, axis=1)

print(df)

# Pertanyaan 1:

# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.

# Pertanyaan 2:

# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.

# Pertanyaan 3:

# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.

# Pertanyaan 4:

# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.

# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://github.com/diashfirdaus-cyber/Pemdas_Itenas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.