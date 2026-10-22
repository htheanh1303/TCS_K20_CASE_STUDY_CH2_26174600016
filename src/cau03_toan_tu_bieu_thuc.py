tong_phut = 135
cong_suat_w = 250
# tinh so gio va so phut con lai
so_gio = tong_phut // 60
so_phut_con_lai = tong_phut % 60
print("So gio:", so_gio)
print("So phut con lai:", so_phut_con_lai)
# bien su dung lau 
bien_su_dung_lau = tong_phut > 60
print("Su dung lau:", bien_su_dung_lau)
#kiem tra du lieu hop le
du_lieu_hop_le = cong_suat_w > 0 and tong_phut > 0
print("Du lieu hop le:", du_lieu_hop_le)
#du doan va kiem chung
print("100 + 20 * 3 =", 100 + 20 * 3)
print("(100 + 20) * 3 =", (100 + 20) * 3)
