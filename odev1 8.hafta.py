dosya=open("asal.txt",mode="w",encoding="utf-8")
sayac = 0
sayi = 0
while sayac < 10:
    sayi += 1
    m = 1
    for i in range(2, sayi):
        if sayi % i == 0:
            m = 0
            break
    if m == 1:
        sayac += 1
        print(sayi)
        dosya.write(str(sayi))
dosya.close()