import os
import pandas as pd
data_folder="ml-100k"
rating_filename=os.path.join(data_folder,"u.data")
all_rating=pd.read_csv(rating_filename,delimiter="\t",header=None,names=["UserID","MovieID","Rating","Datetime"])
all_rating["Datetime"]=pd.to_datetime(all_rating['Datetime'],unit='s')
# print(all_rating[:5000])

all_rating["Favorable"]=all_rating["Rating"]>3
# print(all_rating[10:15])

#从数据集中选取一部分数据作为训练集
ratings=all_rating[all_rating["UserID"].isin(range(200))]
#建立一个只包含用户新欢的某部电影的数据行
favorable_ratings=ratings[ratings["Favorable"]]

#按照用户ID进行分组
from collections import defaultdict
favorable_reviews_by_users=dict((k,frozenset(v.values)) for k,v in favorable_ratings.groupby("UserID")["MovieID"])
num_favorable_by_movie=ratings[["MovieID","Favorable"]].groupby("MovieID").sum()
#最受欢迎的五部电影
print(num_favorable_by_movie.sort_values("Favorable",ascending=False)[:5])

frequent_itemsets={}
min_support=50
frequent_itemsets[1]=dict((frozenset((movie_id,)),row["Favorable"]) for movie_id,row in num_favorable_by_movie.iterrows() if row["Favorable"]>min_support)
def find_frequent_itemsets(favorable_review_by_users,k_l_itemsets,min_support):
    counts=defaultdict(int)
    for user,reviews in favorable_review_by_users.items():
        for itemset in k_l_itemsets:
            if itemset.issubset(reviews):
                for other_reviewed_movie in reviews-itemset:
                    current_superset=itemset | frozenset((other_reviewed_movie,))
                    counts[current_superset]+=1

    return dict([(itemset,frequency) for itemset,frequency in counts.items() if frequency>=min_support])
import  sys

for k in range(2,20):
    cur_frequent_itemsets=find_frequent_itemsets(favorable_reviews_by_users,frequent_itemsets[k-1],min_support)
    if len(cur_frequent_itemsets) == 0:
        print("Did not find any frequent itemsets of length {}".format(k))
        sys.stdout.flush()
        break
    else:
        print("I found {} frequent itemsets of length {}".format(cur_frequent_itemsets))
        sys.stdout.flush()
        frequent_itemsets[k]=cur_frequent_itemsets

print(frequent_itemsets)
