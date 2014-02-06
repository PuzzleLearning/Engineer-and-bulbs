import sys

def write_value( value ): 
    sys.stdout.write( str(value) ) 

bulbs = dict()
for __x in range(1, 1000):
    bulbs[__x] = False

for i in range(1, 1000):
    for b in bulbs:
        if b % i == 0:
            print 'found i= ' + str(i) + ' divides the ' + str(b)
            print 'changing light'
            bulbs[b] = not bulbs[b]

print '{'
for i in range (1, 1000):
    if bulbs[i] is True:
        write_value(str(i) + ',')
print '}'
