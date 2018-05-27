from sklearn.datasets import load_iris
import os
dataset = load_iris()
X = dataset.data
y = dataset.target
# print(dataset.DESCR)

print(os.path.expanduser("~"))#C:\Users\Jackey


import numpy as np
import  csv
#创建训练集和测试集
from sklearn.cross_validation import train_test_split
#导入K近邻分类器
from sklearn.neighbors import  KNeighborsClassifier
data_filename="ionosphere.data"
x=np.zeros((351,34),dtype='float')
y=np.zeros((351,),dtype='bool')

with open(data_filename,'r') as input_file:

    reader=csv.reader(input_file)
    for i,row in enumerate(reader):
        data=[float(datum) for datum in row[:-1]]
        x[i]=data
        y[i]=row[-1]=='g'

# print(x[1])
# print(y)
from matplotlib import  pyplot as plt
avg_scores=[]
all_scores=[]
parameter=list(range(0,20))
for param in parameter:
    print("random_num=",param)
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=param)
    estimator = KNeighborsClassifier()
    estimator.fit(x_train, y_train)
    y_predicted = estimator.predict(x_test)
    accuracy = np.mean(y_test == y_predicted) * 100
    print("The accuracy is {0:.1f}%".format(accuracy))
    from sklearn.cross_validation import cross_val_score

    scores = cross_val_score(estimator, x, y, scoring="accuracy")
    average_accuracy = np.mean(scores) * 100
    print("The cross accuracy is {0:.1f}%".format(accuracy))
    avg_scores.append(np.mean(scores))
    all_scores.append(scores)





