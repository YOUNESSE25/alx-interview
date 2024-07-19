#!/usr/bin/python3
'''
 script that reads stdin line by line and computes metrics:
'''


import sys

cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
sizeTotal = 0
Ctr = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache.keys():
                cache[code] += 1
            sizeTotal += size
            Ctr += 1

        if Ctr == 10:
            Ctr = 0
            print('File size: {}'.format(sizeTotal))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(sizeTotal))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
