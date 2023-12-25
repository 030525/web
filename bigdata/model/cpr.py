from input import Xy

X,y = Xy('../data/train.csv',2000)

X1,y1 = Xy('../data/test.csv',1000)

features = set(X.columns)
features1 = set(X1.columns)

gap = features - features1
print(gap)