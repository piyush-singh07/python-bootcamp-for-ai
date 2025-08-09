#equality operators can be used for content comparison
print(10==10) #T
print(10!=10) #F
print(10==0) #F
print(10!=90) #T
print(10==10.0) #T
print(10==True) #F compares 1 with 10
print(0.0==False) #T
print('Hello'=='Hello') #T
print('hello'=='Hello') #F
print('Hello'==10) #F compares ascii values 
print('hello'==False) #F compares ascii value with 0 and hello ascii value
print('Hello'==True) #F
print(1==True) #T
print(0==False) #T


#difference between == and is operator
# in python we have reusability in case of only 
# in fundamental DTs but not in case collect

l1=[10,90,20]
l2=[10,90,20]

print('===Comparion of == and is operator')
print(l1==l2) #T
print(l1 is l2) #F
l3=l1
print(l1==l3) #T
print(l1 is l3) #T