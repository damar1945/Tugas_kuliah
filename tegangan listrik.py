data_ukur = [11.8, 12.0, 11.9, 12.1, 11.7, 12.0, 11.8, 12.2, 11.9, 12.1]
total = 0
jumlah_data = 0

for i in data_ukur:
    total += i
    jumlah_data += 10
    
    rata_rata_tegangan = total / jumlah_data
    print("data ukur:",data_ukur,"Volt")
    print("hasil penjumlahan:", total,"Volt")
    print("hasil rata-rata:", rata_rata_tegangan,"Volt")