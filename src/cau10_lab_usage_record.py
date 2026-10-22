from datetime import datetime
# 1. Nhap du lieu
ma_phien = input("Nhap ma phien: ")
ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat thiet bi (W): "))
so_phut = int(input("Nhap thoi gian su dung (phut): "))
don_gia_kwh = float(input("Nhap don gia dien (VND/kWh): "))
# 2. Tinh dien nang tieu thu va chi phi dien
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
# 3. Kiem tra thoi gian su dung tren 60 phut
tren_60_phut = so_phut > 60
# 4. Lay thoi diem ghi nhan hien tai
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
# 5. In ket qua bang f-string
print(f"Ma phien: {ma_phien}")
print(f"May: {ma_may}")
print(f"Cong suat: {cong_suat_w:.2f} W")
print(f"Thoi luong: {so_phut} phút")
print(f"Dien nang: {dien_nang_kwh:.3f} kWh")
print(f"Chi phi: {chi_phi:.2f} VND")
print(f"Tren 60 phut: {tren_60_phut}")
print(f"Ghi nhan luc: {thoi_diem_text}")
