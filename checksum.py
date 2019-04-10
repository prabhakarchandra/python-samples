# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:03:48 2019

@author: Prabhakar Chandrasekaran
"""

"""
This is the code to read a file, calculate the checksum value of every row 
and add the value of checksum as the last column of every record.

checksum.py <<input_file>> <<output_file>> <<delimiter>> <<header>>

Note: 
    1. Output file will be overwritten. 
    2. Default delimiter will be assumed to be pipe. 
    3. Default header value is set to false.
    4. Script will abort if input file does not exist.
    5. Script will abort if enough arguments are not passed.

example call:
checksum.py /nas_pp/test/dw2/stg/dwkkfzdf114_20190410.pre /nas_pp/test/dw2/stg/dwkkfzdf114_20190410.cks tab none
checksum.py /nas_pp/test/dw2/stg/dwkkfzdf114_20190410.pre /nas_pp/test/dw2/stg/dwkkfzdf114_20190410.cks comma header
checksum.py /nas_pp/test/dw2/stg/dwkkfzdf114_20190410.pre /nas_pp/test/dw2/stg/dwkkfzdf114_20190410.cks pipe header
python checksum.py C:\ZionsWork\Training\Python\Emp_small.csv C:\ZionsWork\Training\Python\Emp_small_out.csv comma header
"""
import sys
import os
import hashlib

if len(sys.argv) != 5:
    print("Provide the right number of arguments. Aborting...")
    sys.exit(1)

input_exists = os.path.isfile(sys.argv[1])
output_exists = os.path.isfile(sys.argv[2])

if not(input_exists):
    print("Input file does not exist. Aborting...")
    sys.exit(1)

if (output_exists):
    os.remove(sys.argv[2])

delimiter_switcher = {
        'tab'   : '\t',
        'pipe'  : '|',
        'comma' : ',' }

delimiter = delimiter_switcher.get(sys.argv[3], '|')

header_switcher = {
        'header' : True,
        'none'   : False}

header = header_switcher.get(sys.argv[4], False)

input_file = open(sys.argv[1], "r")
output_file = open(sys.argv[2], "w")

if header:
    input_file_index = 0
    for every_line in input_file:
        if input_file_index == 0:
            output_file.write(every_line.rstrip('\n') + delimiter + 'Checksum' + '\n')
            input_file_index += 1
        else:
            output_file.write(every_line.rstrip('\n') + delimiter + hashlib.md5(every_line.encode()).hexdigest() + '\n')        
else:
    for every_line in input_file:
        output_file.write(every_line.rstrip('\n') + delimiter + hashlib.md5(every_line.encode()).hexdigest() + '\n')

input_file.close()
output_file.close()

sys.exit(0)