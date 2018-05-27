import numpy as np
from collections import defaultdict
from operator import  itemgetter
dataset_filename="affinity_dataset.txt"
X=np.loadtxt(dataset_filename)
print(X[:5])#打印前五次的交易信息
#数据五列依次代表面包，牛奶，奶酪，苹果，香蕉
features=["bread","milk","cheese","apples","bananas"]

num_apple_purchases=0
for simple in X:
    if simple[3]==1:
        num_apple_purchases+=1
print("{0} people bought Apples".format(num_apple_purchases))
rule_valid=0
rule_invalid=0
for sample in X:
    if sample[3]==1:
        if(sample[4]==1):
            rule_valid+=1
        else:
            rule_invalid+=1
print("{0} cases of the rule being valid were discovered".format(rule_valid))
print("{0} cases of the rule being invalid were discovered".format(rule_invalid))

#置信度support和支持度confidence
support=rule_valid
confidence=rule_valid/num_apple_purchases
print("The support is {0} and the confidence is {1:.3f}".format(support,confidence))
print("As a percentage,that is {0:.3f}".format(100*confidence))
#创建数据字典，用来存放计算结果
valid_rules=defaultdict(int)
invalid_rules=defaultdict(int)
num_occurances=defaultdict(int)
#通过循环对样本的每个个体以及个体的每个特征值进行处理
n_features=X.shape
print("n_features:",n_features)
print("len:",n_features[1])
for sample in X:
    for premise in range(n_features[1]):
        if sample[premise]==0:continue
        #统计个项指标为1的出现次数
        num_occurances[premise]+=1
        for conclusion in range(n_features[1]):
            #如果结论和推测是同个数据，比如买苹果的买苹果
            if premise==conclusion:
                continue
            if(sample[conclusion])==1:
                valid_rules[(premise,conclusion)]+=1
            else:
                invalid_rules[(premise,conclusion)]+=1
support=invalid_rules
confidence=defaultdict(float)
for premise,conclusion in valid_rules.keys():
    confidence[(premise,conclusion)]=valid_rules[(premise,conclusion)]/num_occurances[premise]
for premise,conclusion in confidence:
    premise_name=features[premise]
    conclusion_name=features[conclusion]
    print("Rule: If a person buys {0} they will also buy {1}".format(premise_name, conclusion_name))
    print(" - Confidence: {0:.3f}".format(confidence[(premise, conclusion)]))
    print(" - Support: {0}".format(support[(premise, conclusion)]))


# 对置信度进行排序
sorted_confidence=sorted(confidence.items(),key=itemgetter(1),reverse=True)
print(sorted_confidence)
