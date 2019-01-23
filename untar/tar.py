# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 11:36:16 2019

@author: wayne
"""
import tarfile
import os
import time
start=time.time()
path='/mnt/disk1/weijiwei/fall11/'
#path='F:/tar/'
b=os.listdir('/mnt/disk1/weijiwei/fall11')
print('all file :',len(b))

for file in b:
    d=file.split('.')[0]
    tar_file=tarfile.open(path+file)
    a_name=tar_file.getnames()
    
    
    for names in a_name:
        tar_file.extract(names,path+d)
    tar_file.close()
    os.remove(path+file)

end=time.time()
usetime=end-start
print('end!',usetime)

#print(a)
