#program for slice
str1= 'javaprogramminglanguage'
print(str1[3:9])
print(str1[3:])
print(str1[:9])
print(str1[:])
print(str1[3:1000])
print(str1[5:2])
print('empty string printed in upper line')

str2='pythonprogramminglanguage'
temp=str2[0].upper()+str2[1:len(str2)-1]+str2[-1]
print(temp)
temp1=str2[0].upper()+str2[1:len(str2)-1]+str2[-1].upper()
print(temp1)
temp2=str2[0]+str2[1:len(str2)-1].upper()+str2[-1]
print(temp2)


# + and * operators in str where * is used for string repeatioton
s='hello'
#print(s+10)
temp4='bye'
print(s+temp4)

print(temp4*3)
print(5*temp4)