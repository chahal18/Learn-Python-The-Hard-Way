i=0 
numbers = []

while i < 6:
    print "At the top i is %d" % i 
    numbers.append(i)
    i=i+1
    
    print "Numbers now: ", numbers 
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers: 
    print num
    
# DRILL 1 - Converting the above process into a function
print "This is the drill_1"
def drill_1(n):
    i=0
    numbers1 = [ ]
    while i < n:
        print "Item: %d" % i
        numbers1.append(i)
        i += 1
    print numbers1

# DRILL 2 - Using the above function
print "\nUsing n=5 in the above function!"
drill_1(5)

print "\nUsing n=7 in the above function!"
drill_1(7)

# DRILL 3 & 4 - A variable step size for the above function
def drill_3(n, step):
    i=0
    numbers3 = [ ]
    while i < n:
        print "Item: %d" % i
        numbers3.append(i)
        i += step
    print numbers3
    
drill_3(14, 3)

# DRILL 5 - Using a for loop instead
def drill_5(n, step):
    numbers5 = range(0, n, step)
    for i in numbers5:
        print "Item: %d" % i
    print numbers5
    
drill_5(102, 8)