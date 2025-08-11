from sys import argv as ar

#program for printing the command line arguments and the type in which they are contained 

# for i in ar : 
#     print(i)

# print(ar) # all the elements from the command line in the list will be in str only 
# print('No. of args: ', len(ar)) 

# program 2 for adding the given numbers provided in command line
print(ar)
l1=ar[1:]
sum =0
for x in l1:
    sum=sum+int(x)

print('The sum of cl args is: ',sum)    
