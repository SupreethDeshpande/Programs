import pandas as pd
import math
class Node:
    def __init__(self,l):
        self.label=l
        self.branches={}
def entropy(data):
    total_ex=len(data)
    positive_ex=len(data.loc[data['PlayTennis']=='Yes'])
    negative_ex=len(data.loc[data['PlayTennis']=='No'])
    entropy=0
    if(positive_ex>0):
        entropy=(-1)*(positive_ex/float(total_ex))*(math.log(positive_ex,2)-math.log(total_ex,2))
    if(negative_ex>0):
        entropy+=(positive_ex/float(total_ex))*(math.log(positive_ex,2)-math.log(total_ex,2))
    return entropy
def gain(s,data,attrib):
    values=set(data[attrib])
    print(values)
    gain=s
    for val in values:
        gain-=len(data.loc[data[attrib]==val])/float(len(data))*entropy(data.loc[data[attrib]==val])
    return gain
def get_attribute(data):
    entropy_s=entropy(data)
    attribute=""
    max_gain=0
    for attr in data.columns[:len(data.columns)-1]:
        g=gain(entropy_s,data,attr)
        if g>max_gain:
            max_gain=g
            attribute=attr
    return attribute
def decision_tree(data):
    root=Node('NULL')
    if(entropy(data)==0):
        if(len(data.loc[data[data.columns[-1]]=='Yes'])==len(data)):
            root.label='Yes'
            return root
        else:
            root.label='No'
            return root
    if(len(data.columns)==1):
        return
    else:
        attrib=get_attribute(data)
        root.label=attrib
        values=set(data[attrib])
        for val in values:
            root.branches[val]=decision_tree(data.loc[data[attrib]==val].drop(attrib,axis=1))
    return root
def get_rules(root,rule,rules):
    if not root.branches:
        rules.append(rule[:-2]+"=>"+root.label)
    return rules
def test(tree,test_str):
    if not tree.branches:
        return tree.label
    return test(tree.branches[test_str[tree.label]],test_str)
data=pd.read_csv('tennis.csv')
entropy_s=entropy(data)
attrib_count=0
cols=len(data.columns)-1
tree=decision_tree(data)
rules=get_rules(tree,"",[])
print(rules)
test_str={}
print('Enter Test case Input:')
for i in data.columns[:-1]:
    test_str[i]=input(i+": ")
print(test_str)
print(test(tree,test_str))

#Outlook,Temperature,Humidity,Wind,PlayTennis
#Sunny,Hot,High,Weak,No
#Sunny,Hot,High,Strong,No
#Overcast,Hot,High,Weak,Yes
#Rain,Mild,High,Weak,Yes
#Rain,Cool,Normal,Weak,Yes
#Rain,Cool,Normal,Strong,No
#Overcast,Cool,Normal,Strong,Yes
#Sunny,Mild,High,Weak,No
#Sunny,Cool,Normal,Weak,Yes
#Rain,Mild,Normal,Weak,Yes
#Sunny,Mild,Normal,Strong,Yes
#Overcast,Mild,High,Strong,Yes
#Overcast,Hot,Normal,Weak,Yes
#Rain,Mild,High,Strong,No
