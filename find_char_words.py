#input: I am a little bird
#output:characters=18 ,words=5

s=input("Enter the String:")
c=0
w=0
for i in range(len(s)):
    c=c+1
    if s[i]==' ':     #we can also use s[i].isspace() as a condition_check
        w+=1
print("Number of characters are {} and words are {} in the given string".format(c,w+1))
