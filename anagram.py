str1=input("Enter the first string: ")
str2=input("Enter the second string: ")

l1=[]
l2=[]
s1=set(l1)
s2=set(l2)

for i in str1:
    l1.append(i)
for j in str2:
    l2.append(j)

if s1==s2 and len(l1)==len(l2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")