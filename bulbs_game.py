import sys
import six


def write_value(value):
    sys.stdout.write(str(value))


bulbs = dict()
for x in range(1, 1000):
    bulbs[x] = False

for i in range(1, 1000):
    for b in bulbs:
        if b % i == 0:
            six.print_('found i= {} divides the {}'.format(str(i), str(b)))
            six.print_('changing light')
            bulbs[b] = not bulbs[b]

write_value('{')
for i in range(1, 1000):
    if bulbs[i] is True:
        write_value(str(i) + ',')
six.print_('}')
