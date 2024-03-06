hari_kerja = 25
hari_kerja_perbulan = 30
gaji = 50000000
hari_lembur = 10
tarif_lembur = 5900000

gaji_pokok = (hari_kerja / hari_kerja_perbulan)* gaji
gaji_lembur = (hari_lembur*tarif_lembur)
total_gaji = int(gaji_pokok+gaji_lembur)
total_gaji =f"{total_gaji:,.2f}"
print("Rp", total_gaji)