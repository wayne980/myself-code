# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 13:56:37 2018

@author: wayne
"""

import json
import torch
import time
from collections import OrderedDict
start=time.time()
print('start!')

dis=json.load(open('imagenet_k_distance.json','r'))

imagenet_k_nearest=OrderedDict()

k=11
for key in dis.keys():
    temp=dis[key]
    temp=torch.Tensor(temp)
    _,sort_dis=torch.sort(temp)
    imagenet_k_nearest[key]=sort_dis[:k].tolist()
json.dump(imagenet_k_nearest,open('imagenet_k11_nearest.json','w')) 

end=time.time()
usetime=end-start
print('end!',usetime)
