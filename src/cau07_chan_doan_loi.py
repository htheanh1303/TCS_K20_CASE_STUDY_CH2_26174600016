ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat W: "))
so_phut = int(input("Nhap so phut: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh:.3f} kWh")
#loi xay ra 
#dong 2 input() luon tra ve chuoi (str). Vi vay, cong_suat_w dang la chuoi "250", khong phai so, nen phep nhan voi so_phut gay loi.
#dong 6 co hai loi : sai ten "dien_nang_kwh" va dau ngoac ")"      