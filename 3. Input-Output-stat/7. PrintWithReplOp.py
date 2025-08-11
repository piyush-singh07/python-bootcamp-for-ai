name='Jack'
sal=10000.0
friend='Jony'
hobby='Race'

print('Your name is {}, your salary is {}, your friend is {}, your hobby is {}'.format(name,sal,friend,hobby))
#we can provide index also
print('Your name is {0}, your salary is {1}, your friend is {2}, your hobby is {3}'.format(name,sal,friend,hobby))
#if we change the index the corresponsing values will be replaced
print('Your name is {3}, your salary is {1}, your friend is {0}, your hobby is {2}'.format(name,sal,friend,hobby))
#we can give key value pairs also
print('with key values')
print('Your name is {n}, your salary is {s}, your friend is {f}, your hobby is {h}'.format(n=name,s=sal,f=friend,h=hobby))