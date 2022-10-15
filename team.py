n=int(input())
arr=[]
result=0
for i in range(n):
    arr.append(input())
for j in range(n):
    art=arr[j].split(" ")
    if int(art[0])+int(art[1])+int(art[2])>=2:
        result+=1
print(result)






