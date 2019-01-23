"""
Created on Sat Dec 15 23:31:10 2018

@author: wayne
"""

import json
import torch
import torch.nn.functional as F
from collections import OrderedDict
import time


a=torch.randn(4)
b=torch.randn(4)
print(a,b)
c=torch.div(a,b)
print(c)

start=time.time()
print('start')

graphs=json.load(open('imagenet-induced-graph.json','r'))
wnids=graphs['wnids']
'''
def euclid_dis(word_vectors):
    dis=OrderedDict()
    adj_matrix=torch.FloatTensor()
    for i in range(word_vectors.size()[0]):
        temp=torch.add(word_vectors,-word_vectors[i])
        temp=torch.norm(temp,p=2,dim=1)
        distance=temp.data.cpu()
        dis[wnids[i]]=distance.tolist()
        distance=torch.unsqueeze(distance,0)
        adj_matrix=torch.cat((adj_matrix,distance),0)
    json.dump(dis,open('imagenet_k_distance.json','w'))
    return adj_matrix
print(len(wnids))
'''


    
def cos_dis(word_vec):
    dis=OrderedDict()
    word2vec=word_vec.cuda()
    adjacency_matrix=torch.FloatTensor()
    temp=torch.norm(word2vec,p=2,dim=1)
    
    for i in range(word2vec.size()[0]):    
        word=word2vec[i].view(-1,1)
        distance=torch.mm(word2vec,word)
        demo=torch.mul(temp,temp[i])
        demo=torch.unsqueeze(demo,1)
        distance=torch.div(distance,demo)
        distance=distance.data.cpu()
        dis[wnids[i]]=distance.tolist()
        adjacency_matrix=torch.cat((adjacency_matrix,distance),1)
    json.dump(dis,open('imagenet_k_cos_distance.json','w'))
    return adjacency_matrix
#dd=cos_dis()

print(len(wnids))

word_vectors=torch.tensor(graphs['vectors']).cuda()
word_vectors=F.normalize(word_vectors)
print(word_vectors.shape)

print('save distance matrix')
adjacency_matrix=cos_dis(word_vectors)

print('OK!')
adjacency=torch.zeros(adjacency_matrix.size())
_,sort_dis=torch.sort(adjacency_matrix,1)
k=6
imagenet_k_nearest=OrderedDict()

for i in range(adjacency.shape[0]):
    imagenet_k_nearest[wnids[i]]=sort_dis[i][:k].tolist()
json.dump(imagenet_k_nearest,open('imagenet_k_cos_nearest.json','w'))
end=time.time()
longtime=end-start
print('end!',longtime)

