animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print animals

for i in animals:
    print i
    
print " "
print "First, second, third numbers are ordinal numbers but"
print "But we need to count by cardinal numbers"
print " "

for i in range(len(animals)):
    print "Index %d in the list is %s" % (i, animals[i])
    
print animals[4]