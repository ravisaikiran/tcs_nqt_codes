#findind prefixes
m=int(input("Enter the size for the name list: "))
names=[]
for i in range(m):
    names.append(input("enter the name{}: ".format(i+1)))
n=int(input("Enter the size for the query list: "))
query=[]
for i in range(n):
    query.append(input("enter the query{}: ".format(i+1)))
res=[0]*n
for i in range(n):
    for j in names:
        if j[:len(j)-1].find(query[i])==0:
            res[i]+=1
print(res)
