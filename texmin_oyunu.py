import random
import time
print("""************
1 və 50 arasinda bir eded yazin..////
******************""")

print("Unutmayin, sadece 7 eded texmin haqqiniz var.. :) ")
texmin_haqqi = 7
texmin = random.randint(1,50)

while True:

    if texmin_haqqi == 0:
        print("İstifade haqqiniz bitdi..")
        break

    eded = int(input("Ededi daxil edin: "))

    if eded > texmin:
        print("Yoxlanilir..")
        time.sleep(1)
        texmin_haqqi -= 1
        print("DİQQET: {} texmin haqqiniz qaldi!".format(texmin_haqqi))
        time.sleep(1)
        print("DAHA KICIK EDED DAXIL EDIN..")

    elif eded < texmin:
        print("Yoxlanilir...")
        time.sleep(1)
        texmin_haqqi -= 1
        print("DİQQET: {} texmin haqqiniz qaldi!".format(texmin_haqqi))
        time.sleep(1)
        print("DAHA BOYUK EDED DAXIL EDIN..")


    else:
        print("Yoxlanilir...")
        time.sleep(2)
        print("TEBRIKLER :)  Dogru tapdiniz. {} ededi dogrudur..".format(texmin))
