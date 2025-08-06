t1=(10,90,'hi',97.2)
print(type(t1))

#t1[0]='pop'  ----> not possible as tuple is immutable and it does not allow any changes in the object

#slicing and indexing is possible



print(t1[1:3])
print(t1[-1])
print(t1[1:1000])

# since tuple is immutable hence no append and remove methods are there
#t1.append('hello')  ----->> attribute error
#t1.remove(90)    ------>> attribute error


#in case of tuple if we have a single element in the round bracket then it is considered as int
# float , str whatever we gave hence since element not possible as an element in tuple 
#if we want to have single element in a tuple then we have to provide comma 
a=(10)
print(type(a))  # will give type as int
b=(9.99)
print(type(b)) # will give type as float
c=('hi') 
print(type(c)) # will give type as str
tup=(87,)
print(type(tup)) # will give type as tuple
