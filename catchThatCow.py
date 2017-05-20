# -*- coding: utf-8 -*-
"""
Created on Sat May 20 14:44:24 2017

@author: AlphaTao
#抓住那头牛 POJ3278
"""

def bsf(x,k):
    step=0
    allList=range(0,100001)
    alist=[]
    alist.append(x)
    allList.remove(x)
    while (len(allList)>0):
        blist=[]
        step+=1
        for item in alist:
            if (item-1)==k or (item+1)==k or 2*item==k:
                return step
            if (item-1) in allList:
                blist.append(item-1)
                allList.remove(item-1)
            if (item+1) in allList:
                blist.append(item+1)
                allList.remove(item+1)
            if (2*item) in allList:
                blist.append(item*2)
                allList.remove(item*2)
        alist=blist[:]

if __name__=='__main__':
    x,k=map(int,raw_input().split())
    print bsf(x,k)
    