cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("dien nang tieu thu:", dien_nang_kwh, "kWh")
print("Kieu du lieu dien nang:", type(dien_nang_kwh))
print("Chi phi dien:", chi_phi, "dong")
print("Kieu du lieu chi phi:", type(chi_phi))
#Thay so phut bang 60 roi tinh lai
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("Sau khi thay so phut bang 60:")
print("dien nang tieu thu:", dien_nang_kwh, "kWh")
print("Chi phi dien:", chi_phi, "dong")
#du doan ket qua:
#dien nang tieu thu: 0.375 kWh
#Kieu du lieu dien nang: <class 'float'>
#Chi phi dien: 1125.0 dong
#Kieu du lieu chi phi: <class 'float'>
#Sau khi thay so phut bang 60:
#dien nang tieu thu: 0.25 kWh
#Chi phi dien: 750.0 dong
