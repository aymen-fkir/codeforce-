n=int(input())
arr=[]
res=""
for i in range(n):
    arr.append(input())
for j in range(n):
    if len(arr[j])<=10 :
        res+=arr[j]+"\n"
    else:
        res+=arr[j][0]+str(len(arr[j])-2)+arr[j][len(arr[j])-1]+"\n"
print(res)