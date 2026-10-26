aqi = 165
kabut_pekat = True

if aqi <= 50 :
    status = print("baik")
    
elif 50 >= aqi <=100 :
    status = print("sedang")
 

elif   100 >= aqi <= 150 :
    status = print("tidak sehat bagi kelompok sensitif")

elif aqi >= 150 :
    status = print("Sangat tidak sehat")
    

if kabut_pekat:
    print("gunakan masker dan hindari aktivitas luar ruangan ")
else:
    print("aman")