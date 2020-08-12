#!/usr/bin/env python

import os, errno


path = 'C:/Users/TESDA NV/Desktop/UTPRAS/2020/IBT_REPORTS/semi_annual/'
f = open('tvi.txt','r')

try:
    for i in f:
        os.mkdir(os.path.join(path,i.strip()))

except OSError as e:
    if e.errno == errno.EEXIST:
        print('Done creating folders')
    else:
        raise
    

f.close()
