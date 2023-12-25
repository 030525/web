from output import output
from input import Xy

data,y = Xy("../data/test.csv",1000)

print(data.shape)


print(output(data))