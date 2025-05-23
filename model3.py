
from pickle import dump,load
from pandas import read_csv
A = read_csv("na_drug (1).csv")
X = A[["Satisfaction","EaseOfUse"]]
Y = A[["Effective"]]
from sklearn.tree import DecisionTreeRegressor
dtr = DecisionTreeRegressor()
model = dtr.fit(X,Y)
dump(model,open("model.pkl","wb"))