#coding=utf-8

'''
Created on 2017年3月6日
@author: brisyramshere
'''
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pylab import draw_networkx_edge_labels
from networkx.drawing.layout import spring_layout
from matplotlib.transforms import BboxBase
from networkx.algorithms.clique import enumerate_all_cliques
f = file('case0.txt','r')
factor = 1
G = nx.Graph()   #新建一个网络图
edgewidth=[]
while 1:
    data = f.readline();
    x = int(str(data.split(' ')[0]))
    y = int(str(data.split(' ')[1]))  #使用split将字符串以空格符号分开，前一个为x，后一个为y
    weight = int(str(data.split(' ')[2]))
    cost=int(str(data.split(' ')[3]))
    G.add_edge(x, y)
    G[x][y]['b']=weight
    G[x][y]['c']=cost
    #G.add_weighted_edges_from([(x,y,weight)]);   #在网络中添加x-y这一条边
    edgewidth.append(weight*0.1)
    factor = factor + 1  
    if factor == 96:
        break
else:
    print 'error'
pos=nx.fruchterman_reingold_layout(G,dim=2,k=0.8,scale=1.5)
#pos=spring_layout(G)
nx.draw_networkx_nodes(G,pos,node_size=100,alpha=0.7)
nx.draw_networkx_labels(G, pos,font_size=9)
edge_labels=nx.get_edge_attributes(G, 'c')
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_edge_labels(G,pos,font_size=8,clip_on=True,font_color='red')
plt.show()

#聚类
print enumerate_all_cliques(G)
