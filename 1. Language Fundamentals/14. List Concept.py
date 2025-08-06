list1=['hello', 10, 99.8, True, 'myway']
print('Memory address is :' ,id(list1))
print('list1 is :',list1)
list1[0]='no way'
print('printing list1 after making changes in first place')
print(list1)

list2=[]
list2.append(99)
list2.append('love')
list2.append(98.8)
list2.append(False)
list2.append(10+90j)

print(20*'#')
print('list2 object:')

print(list2)
print('Memory address of list2 is :', id(list2))
print('Object at third position is',list2[3])

list2.remove(False)
print('third object removed to check the indexing now')
print(list2)

print('Memory address of list2 is :', id(list2))
print('Object at third position is',list2[3])

print('slice operator examples')
print(30*'---')
print('\n')
print('printing the list2 again : ', list2)
list2.remove(list2[-1])
print('printing the list2 again after removing last element : ', list2)
list2.append(True)
list2.append(76)
print('printing the list2 again after adding 2 element : ', list2)
print(list2[1:3])
print(list2[-1])
print(list2[2:-1])



