# Borrowed from https://isc.sans.edu/diary/How+do+you+spell+%22PSK%22%3F/16643 useful snippet.
from random import randint
import sys
if not (len(sys.argv) == 2):                                           # verify syntax
        print "Syntax PSK LENGTH_OF_PSK"

rndstrlen = int(sys.argv[1])                                           # how long is the output string?
outstring=""

chars = "abcedfghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789"       # define the list of valid characters
charlist = list(chars)                                                 # change it to a list for lookups

numchars = len(charlist)  -1                                           # get length of string list, -1 for start from zero

for i in range (0, rndstrlen):
     c = charlist[randint(0,numchars)]                                 # pick a random char from the list
     outstring += c                                                    # append it to outstring

print outstring
