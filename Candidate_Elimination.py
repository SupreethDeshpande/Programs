import numpy as np
import pandas as pd
data=pd.DataFrame(data=pd.read_csv('data.csv'))
print('The dataset is:')
print(data)
concepts=np.array(data.iloc[:,0:-1])
print('\n The concepts are:\n',concepts)
target=np.array(data.iloc[:,-1])
print('\n The target is:\n',target)
if target[0] == 'NO':
    for i in range(1,len(target)):
        if target[i] == 'YES':
            target[0],target[i]=target[i],target[0]
            temp=[i for i in concepts[i]]
            concepts[i]=concepts[0]
            concepts[0]=temp
            break
       
def learn(concepts,target):
    specific_h=concepts[0].copy()
    general_h=[['?' for i in range(len(specific_h))]for i in range(len(specific_h))]
   
    for i,h in enumerate(concepts):
        if target[i] =='YES':
            for x in range(len(specific_h)):
                if h[x]!=specific_h[x]:
                    specific_h[x]='?'
                    general_h[x][x]='?'
        if target[i]=='NO':
            for x in range(len(specific_h)):
                if h[x]!=specific_h[x]:
                    general_h[x][x]=specific_h[x]
                else:
                    general_h[x][x]='?'
                           
    indices=[i for i,val in enumerate(general_h) if val == ['?','?','?','?','?','?']]
    for i in indices:
        general_h.remove(['?','?','?','?','?','?'])
    return specific_h,general_h
s_final,g_final=learn(concepts,target)
print("\n Final S:",s_final)
print("\n Final G:",g_final)

#sunny  warm  normal  strong  warm    same  YES
#sunny  warm    high  strong  warm    same  YES
#rainy  cold    high  strong  warm  change   NO
#sunny  warm    high  strong  cool  change  YES
