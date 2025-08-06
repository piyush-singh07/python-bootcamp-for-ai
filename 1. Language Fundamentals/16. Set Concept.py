s={10,90,'hello',90.88}
print(type(s))
print(s)

s.add(65)
s.add('pop')
s.add(34.22)
print(s)
s.add('pop')
s.add(90)
s.add(1233)
print(s)
s.remove('pop')
s.remove(1233)
print(s)

#since, in set order is not pereserved so indexing and slicing are not possible

#print(s[1])  # TypeError : set doest not support indexing
#print(s[2:6])  #TypeErroe: set object is not subscriptable

# if we write empty curly

set1={}
print(type(set1))
print(set1)

set2=set()
print(type(set2))
print(set2)
