import pandas as pd
import numpy as np
import random
from sklearn.utils import shuffle
df=pd.read_csv('F:/DaiSEE/DAiSEE/DAiSEE/Labels/NewLabels.csv')
list0=[]
list1=[]
list2=[]
list3=[]
new=pd.DataFrame(columns=['ClipID','Engagement'])
for i in range(0,len(df)):
    if df.loc[i,'Engagement']==0:
        list0.append(df.loc[i,'ClipID'])
    if df.loc[i,'Engagement']==1:
        if df.loc[i,'Boredom']==3:
            list1.append(df.loc[i,'ClipID'])
    if df.loc[i,'Engagement']==2:
        if df.loc[i,'Boredom']==0:
            list2.append(df.loc[i,'ClipID'])
    if df.loc[i,'Engagement']==3:
        if df.loc[i,'Boredom']==0:
            list3.append(df.loc[i,'ClipID'])
list0*=3
list1*=3
list2=random.sample(list2, 100)
list3=random.sample(list3, 100)
new['ClipID']=list0[0:100]+list1[0:100]+list2+list3
new['Engagement']=[0]*100+[1]*100+[2]*100+[3]*100
# new.to_csv('F:/DaiSEE/DAiSEE/DAiSEE/Labels/SampleLabels.csv',index=False)
print(new.head(10))
new = shuffle(new)
print(new.head(10))


