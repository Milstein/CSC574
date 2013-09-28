import sys
from math import sqrt, floor
from random import randint

if len(sys.argv) != 2:
    print "No H(m) given, generating large random one."
    hm = randint(1000000, 1000000000)
    print "Using H(m) = {}".format(hm)
else:
    hm = float(sys.argv[1])

def gen_message(remainder):
    result = []
    while remainder != 0:
        new = floor(sqrt(remainder))
        result.append(new)
        remainder -= new ** 2

    return result

def check_result(m, hm):
    running_sum = 0
    for i in m:
        running_sum += i**2
    return int(running_sum) == int(hm)

m1_result = []
m2_result = []

for m1_hack in range(1, int(floor(sqrt(hm)))):
    m1_remainder = hm - m1_hack**2

    m1_result = gen_message(m1_remainder)
    m1_result.append(float(m1_hack))

    m2_result = gen_message(hm)

    if set(m2_result) != set(m1_result):
        if not check_result(m1_result, hm):
            print "M1 is invalid: {}".format(m1_result)
            sys.exit(1)
        if not check_result(m2_result, hm):
            print "M2 is invalid: {}".format(m2_result)
            sys.exit(1)

        print "m1: {}".format(m1_result)
        print "m2: {}".format(m2_result)
        print "Validation passed"
        sys.exit(0)

print "Two unique messages could not be found."
print "m1 == m2 == {}".format(m1_result)
