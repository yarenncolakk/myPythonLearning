#1
'''
n = int(input("Kaç sayı girmek istiyorsunuz? "))
sayilar = []
for i in range(n):
 sayi = float(input(f"{i+1}. sayıyı girin: "))
 sayilar.append(sayi)

en_buyuk = max(sayilar)
print(f"Girdiğiniz sayılar arasında en büyüğü: {en_buyuk}")
'''

'''
#2
kelime=input("Bir kelime girin:")
ters_kelime=kelime[::-1]
print(f"Girdiğiniz kelimenin tersi:{ters_kelime}")
'''

'''
#3
terim_sayisi=int(input("Kaç terim hesaplamak istiyorsunuz?"))
fibonacci=[0,1]

for i in range(2,terim_sayisi):
    yeni_terim=fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(yeni_terim)

print(f"İlk {terim_sayisi} Fibonacci terimi:{fibonacci}")
'''

'''
#4
sayi = int(input("Bir sayı girin: "))

if sayi > 1:
 for i in range(2, sayi):
  if (sayi % i) == 0:
   print(f"{sayi} asal bir sayı değildir.")
   break
  else:
   print(f"{sayi} asal bir sayıdır.")
else:
 print(f"{sayi} asal bir sayı değildir.")
 '''

#5
ders_sayisi=int(input("Kaç dersiniz var?"))
notlar=[]
toplam=0

for i in range(ders_sayisi):
    not_deg=float(input(f"{i+1}. dersin notunu girin:"))
    notlar.append(not_deg)
    toplam += not_deg

ortalama=toplam/ders_sayisi

print(f"Not ortalamanız:{ortalama:.2f}")

if ortalama >=50:
     print("Tebrikler, geçtiniz!")
else:
    print("Maalesef, kaldınız.")
                


