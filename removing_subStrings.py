#input string1=xxyzyzyv
#      string2=xyz
#output   2(len of string after removing str2 from str1 recursively)
def fun(s1,s2):
    if s2 not in s1:
        return len(s1)
    else:
        i=s1.index(s2)
        s1=s1[:i]+s1[i+len(s2):]
        return fun(s1,s2)
string1=input()
string2=input()
x=fun(string1,string2)
print(x)
