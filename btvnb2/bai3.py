# a) Tính tổng S(n)
n = int(input(" Nhập số nguyên dương n = "))
tong = 0
for i in range (1,2*n+2) :
    if i % 2 == 0 :
        tong -= i
    else :
        tong += i
print ("Tổng S(n) = ", tong )
# b) 
n = int(input(" Nhập số nguyên dương n = "))
tong = 0
for i in range (1,n+1):
    tong += 1/i
print ("Tổng S(n) = ", tong)
# c)
a = int (input( "Nhập số nguyên a = "))
b = int (input( "Nhập số nguyên b = "))
c = int (input( "Nhập số nguyên c = "))
D = b**2-4*a*c
if a == 0 :
    print (" Pt bậc nhất ")
else : 
    print ("Pt bậc 2")
    if D > 0 :
        x1 = (-b + D**0.5) / 2*a
        x2 = (-b - D**0.5) / 2*a
        print ("PT có  2 nghiệm là x1 = ",x1,"x2 = ",x2)
    if D == 0 :
        x1=x2=-b/2*a
        print ("Pt có nghiệm duy nhất là :", x1)
    else :
        print ("Pt vô nghiệm")