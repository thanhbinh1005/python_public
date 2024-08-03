setA = set()
setB = set()

#  Nhap
nA = int(input())
nB = int(input())
print()

for i in range(nA):
    setA.add(int(input()))
print()
for i in range(nB):
    setB.add(int(input()))

# Tin toan
lstDS = []
lstDS2 = []
for i in setA:
    set_tmp = {i}
    if set_tmp.issubset(setB) == True:
        lstDS.append(i)
    else:
        lstDS2.append(i)
    set_tmp.clear()
# dki o ca 2 ban
print(lstDS)
# chi dki o ban 1
print(lstDS2)