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

x_native_bin = ""
y_native_bin = ""
for i in range (0, 32):
    x_native_bin += str(randint(0,1))
    y_native_bin += str(randint(0,1))

x_native_int = int(b"{}".format(x_native_bin),2)
y_native_int = int(b"{}".format(y_native_bin),2)

print "X native: {}".format(x_native_int)
print "Y native: {}".format(y_native_int)
print "X native bin: {}".format(x_native_bin)
print "Y native bin: {}".format(y_native_bin)

# For both, swap 8 far left with 8 far right, same for right mid and left mid

x_nonnative_bin = convert(x_native_bin)
y_nonnative_bin = convert(y_native_bin)
x_nonnative_int = int(b"{}".format(x_nonnative_bin),2)
y_nonnative_int = int(b"{}".format(y_nonnative_bin),2)

print "X non-native: {}".format(x_nonnative_int)
print "Y non-native: {}".format(y_nonnative_int)
print "X non-native bin: {}".format(x_nonnative_bin)
print "Y non-native bin: {}".format(y_nonnative_bin)

# Convert to int and add the numbers

result_nonnative_int = x_nonnative_int + y_nonnative_int

print "Non-native math:"
print "{} + {} = {}".format(x_nonnative_int, 
                            y_nonnative_int, 
                            result_nonnative_int)

# Convert result to 32 bit binary string

result_nonnative_bin = '{0:032b}'.format(result_nonnative_int)

if len(result_nonnative_bin) > 32:
    print "Overflow occurred, OS should handle it"
    result_nonnative_bin = result_nonnative_bin[:32]

print "Result non-native bin: {}".format(result_nonnative_bin)

# Perform same swap that occurred in step two

result_native_bin = convert(result_nonnative_bin)
print "Result native: {}".format(result_native_bin)
