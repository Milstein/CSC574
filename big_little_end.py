#!/usr/bin/env python
import sys
from random import randint
from array import array

# Define function for converting from one endian to the other

def convert(in_str):
    """Convert 32 bit str between little and big endian."""
    assert len(in_str) == 32
    assert type(in_str) == str

    return in_str[24:] + in_str[16:24] + in_str[8:16] + in_str[:8]

# Generate two 32 bit binary strings

x_nonnative_bin = ""
y_nonnative_bin = ""
for i in range (0, 32):
    x_nonnative_bin += str(randint(0,1))
    y_nonnative_bin += str(randint(0,1))

x_nonnative_int = int(b"{}".format(x_nonnative_bin),2)
y_nonnative_int = int(b"{}".format(y_nonnative_bin),2)

print "X nonnative bin: {}".format(x_nonnative_bin)
print "Y nonnative bin: {}".format(y_nonnative_bin)
print "X nonnative int: {}".format(x_nonnative_int)
print "Y nonnative int: {}".format(y_nonnative_int)

# For both, swap 8 far left with 8 far right, same for right mid and left mid

x_native_bin = convert(x_nonnative_bin)
y_native_bin = convert(y_nonnative_bin)
print "X native bin: {}".format(x_native_bin)
print "Y native bin: {}".format(y_native_bin)

# Convert to int and add the numbers

x_native_int = int(b"{}".format(x_native_bin),2)
y_native_int = int(b"{}".format(y_native_bin),2)
print "X native int: {}".format(x_native_int)
print "Y native int: {}".format(y_native_int)

result_native_int = x_native_int + y_native_int

print "Native math: {} + {} = {}".format(x_native_int, 
                                         y_native_int, 
                                         result_native_int)

# Convert result to 32 bit binary string

result_native_bin = '{0:032b}'.format(result_native_int)

if len(result_native_bin) > 32:
    # Note: Handling this situation wasn't required by the problem
    print "Overflow occurred, system-dependent logic should run here."
    result_native_bin = result_native_bin[:32]

print "Result native bin: {}".format(result_native_bin)

# Perform same swap that occurred in step two

result_nonnative_bin = convert(result_native_bin)
print "Result nonnative bin (final): {}".format(result_nonnative_bin)
