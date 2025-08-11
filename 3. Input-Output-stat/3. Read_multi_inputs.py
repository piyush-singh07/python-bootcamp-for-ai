#read multiple values from keyboard in a single line

inp1,inp2=[int(x) for x in input('Enter 2 numbers : ').split()]
print('The sum is: ',inp1+inp2)


#the below lines are the behind the scene of the above line
s=input('Enter two no.s: ')
l=s.split()
print(l)
l2=[int(i) for i in l]
print(l2)
a,b=l2
print(a)
print(b)
print('sum is: ',a+b)


#sample prog to read 5 numbers and write min value
l1=[int(x) for x in input('Enter 5 nums with comma separation: ').split(',')]
print('Min is', min(l1))


#take 3 float values with comma separation and write its sum
a,b,c=[float(i) for i in input('Enter 3 float values with comma : ').split(',')]
print('The sum of 3 floats are: ',a+b+c)