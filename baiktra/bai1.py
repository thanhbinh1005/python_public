my_list = []
my_list = input("nhap day so: ")
cnt = {}
for num in my_list:
    if num in my_list:
        cnt[num] +=1
    else
        cnt[num] =1
new_list = []  
for number in cnt:  
    if cnt[number] % 5 == 0 and cnt[number] % 10 != 0:  
        new_list.append(number)  
print(new_list)
