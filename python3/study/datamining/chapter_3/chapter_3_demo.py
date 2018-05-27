import pandas as pd
import  numpy as np
data_filename="dicision trees sample.csv"
result=pd.read_csv(data_filename,skiprows=[0,])
result.columns = ["Date", "Start (ET)", "Visitor Team", "VisitorPts", "Home Team", "HomePts", "Score Type", "OT?","Notes"]
print(result.ix[:5])
result["HomeWin"]=result["VisitorPts"]<result["HomePts"]
y_true=result["HomeWin"].values
from collections import defaultdict
won_last=defaultdict(int)
for index,row in result.iterrows():
    home_team=row["Home Team"]
    visitor_team=row["Visitor Team"]
    row["HomeLastWin"]=won_last[home_team]
    row["VisitorLastWin"]=won_last[visitor_team]
    result.ix[index]=row

    won_last[home_team]=row["HomeWin"]
    won_last[visitor_team]=not  row["HomeWin"]
print(result.ix[20:25])

from sklearn.tree import  DecisionTreeClassifier
from sklearn.cross_validation import  cross_val_score
clf=DecisionTreeClassifier(random_state=14)
x_previouswins=result[["HomeLastWin","VisitorLastWin"]].values
scores=cross_val_score(clf,x_previouswins,y_true,scoring='accuracy')
print("Using just the last result from the home and visitor teams")
print("Accuracy: {0:.1f}%".format(np.mean(scores) * 100))