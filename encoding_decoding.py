s1=input()
s2=input()
en=''
de=''
for i in s1:
    if i.isalpha() or i.isspace() or i==',' or i=='.':
        if i.isalpha():
            en+=chr(ord(i)+5)
        elif i.isspace() or i==',' or i=='.':
            en+=i
    else:
        print("INVALID INPUT")
        en=''
        break
for i in s2:
    if i.isalpha() or i.isspace() or i==',' or i=='.':
        if i.isalpha():
            de+=chr(ord(i)-5)
        elif i.isspace() or i==',' or i=='.':
            de+=i
    else:
        print("INVALID INPUT")
        de=''
        break
print(en)
print(de)
