# Khai bao bien
ma_may = "PC12"
cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000
# 13. Tinh dien nang tieu thu va chi phi dien
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
# 14. In ket qua va kieu du lieu
print("Ma may:",ma_may)
print("dien nang tieu thu:", dien_nang_kwh, "kWh")
print("Kieu du lieu dien nang:", type(dien_nang_kwh))
print("Chi phi dien:", chi_phi, "dong")
print("Kieu du lieu chi phi:", type(chi_phi))
# 16. Thay so phut bang 60 roi tinh lai
print("Ma may:",ma_may)
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("Sau khi thay so phut bang 60:")
print("dien nang tieu thu:", dien_nang_kwh, "kWh")
print("Chi phi dien:", chi_phi, "dong")
