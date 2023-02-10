#!/bin/env python3

import sys, getopt

fname = sys.argv[1]

addresses = [0x5CA94C, 0x5CA9A8, 0x5CAA04, 0x5CAA60, 0x5CAABC, 0x5CAB18, 0x5CAB74, 0x5CABD0, 0x5CAC2C, 0x5CAC88, 0x5CACE4, 0x5CAD40, 0x5CAD9C, 0x5CADF8, 0x5CAE54, 0x5CAEB0, 0x5CAF0C, 0x5CAF68, 0x5CAFC4, 0x5CB020, 0x5CB07C, 0x5CB0D8, 0x5CB134, 0x5CB190, 0x5CB1EC, 0x5CB248, 0x5CB2A4, 0x5CB300, 0x5CB35C, 0x5CB3B8, 0x5CB414, 0x5CB470, 0x5CB4CC, 0x5CB528, 0x5CB584, 0x5CB5E0, 0x5CB63C, 0x5CB698, 0x5CB6F4, 0x5CB750, 0x5CB7AC, 0x5CB808]
fow_offset = 0x3

try:
    rom = open(fname, "r+b")
    print("Opened {0} for writing.".format(fname))
except:
    sys.exit("Error opening file: {0}".format(fname))

for map in addresses:
    rom.seek(map + fow_offset,0)
    i = rom.read(1)
    print(i)
    if i == b'\x00':
        rom.seek(map + fow_offset,0)
        rom.write(b'\x01')
        print("Applied fog of war to map at location {:06X}".format(map))
    elif i == b'\x01':
        print("Map at location {:06X} already had Fog of War".format(map))
    else:
        print("Fog of War for Map at location {0:06X} neither enabled nor disabled (was passed {1})".format(map,i))

rom.close()
