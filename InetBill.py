#READ-INFO : Author : Ananda Fikri - Clone Writer
#contact me at akbarijlal2@gmail.com for the next inf
#Enjoy Programming with Snakies :)

#Banner Header
print("="*50)
print("=", " "*11, "PSYCIOT BY CLONEWRITER"," "*11, "=")
print("="*16, "INTERNET BILLING", "="*16)
print("=", " "*9, "Authorized by Ananda Fikri", " "*9, "=")
print("="*50)

#membuat program perubahan waktu
start   = str(input("input the started time (hh.mm)\t: "))
end     = str(input("input the ended time (hh.mm)\t: "))

#end point and algoritm conditional
print("-"*50)

pricePerTime = 500
pricePerHour = 3000
is_tenMin = pricePerTime

is_accstart = str(start).split(".")
is_accend = str(end).split(".")
is_retTimStart = int(is_accstart[0]) * 60 + int(is_accstart[1])
is_retTimEnd = int(is_accend[0]) * 60 + int(is_accend[1])

#================TESTER=================
# print(is_retTimEnd - is_retTimStart)
# print(is_accstart)
# print(is_accend)
# print(is_retTimStart)
#=======================================

is_negatime = int(is_retTimEnd - is_retTimStart)
is_est = float("{:.2f}".format(is_negatime))
is_estConv = int(is_est)
is_tenMult = int((is_estConv/10)*pricePerTime)

#nevermind, haha
print()

#info
if is_negatime > 1 and is_negatime < 60:
    print("Time assesment\t\t\t:", is_negatime, 'Minutes')
elif is_negatime == 1:
    print("Time assesment\t\t\t: A Minute")

#Don't be confused ahaha
elif is_negatime % 60 == 0:
    if is_negatime == 60:
        print("Time assesment\t\t\t:", str(int(is_negatime/60)), "Hour")
    elif is_negatime % 60 == 0:
        print("Time assesment\t\t\t:", str(int(is_negatime/60)), "Hours")
elif is_negatime % 60 != 0:
    print("Time assesment\t\t\t:", str(int(is_negatime/60)), "Hour", str(int(is_negatime%60)), "Minutes")
else:
    print("Time is invalid")

# logic of condition
if is_retTimEnd > is_retTimStart:
   if is_estConv >0 and is_estConv < 10:
       print("Total Price\t\t\t: " + str(pricePerTime))
   elif is_estConv >= 10 and is_estConv < 60:
       print("Total Price\t\t\t: " + str(is_tenMult))
   elif is_estConv == 60:
       print("Total Price\t\t\t: " + str(pricePerHour))
   elif is_estConv > 60:
       print("Total Price\t\t\t: " + str(((pricePerHour)+int(float("%.2g" % (((is_negatime%60)/10)*pricePerTime))))))
   else:
       exit()

#end task
print()
print("="*20, "THANK YOU", "="*19)
print("<"*9, "https://github.com/clonewriter", ">"*9)
