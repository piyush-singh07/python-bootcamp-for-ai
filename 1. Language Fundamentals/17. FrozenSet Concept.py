s={1,2,3,4}
l=[10,20,30,40]
t=(100,200,300,400)

#frozenset() method will have only 1 argument which can be either list,tuple or set
fs1=frozenset(s)
fs2=frozenset(l)
fs3=frozenset(t)

print(fs1)
print(fs2)
print(fs3)

print(type(fs1))
print(type(fs2))
print(type(fs3))

#since, frozenset is immutable hence we can not add or remove anything 

#fs1.add(1000)  #AttributeError: no such attribute 'add'
#fs1.remove(1)   #AttributeError: no such attribute 'remove'