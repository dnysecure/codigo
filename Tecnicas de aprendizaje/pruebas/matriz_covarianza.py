import pandas as pd
iris=pd.read_csv("https://raw.githubusercontent.com/toneloy/data/master/iris.csv", usecols=[0,1,2,3])
iris.head()

iris.describre() # de que tipo es?
#cov_mat = iris.cov()
#cov_mat

#cov_mat.loc["petal_width", "sepal_width"]