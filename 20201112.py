import pandas as pd
import numpy as np
import matplotlib as plt
import  scipy,math
#  The Bubble Algorithm
bulu=[99,3,4,5,6,2,6,8,11,2,15,6,1,100]
sort=[]

def BubbleSort(x):
    for i in range(len(bulu)):
        for j in range(len(bulu)-i-1):
            if bulu[j]>bulu[j+1]:
                bulu[j],bulu[j+1]=bulu[j+1],bulu[j]
BubbleSort(bulu)

for i in bulu:
    print(i)












