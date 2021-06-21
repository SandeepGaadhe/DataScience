import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd


#Logistic Regression
#Now, let's understand how to perform logistic regression using statsmodels with the following steps:

#Download the popular iris data set (containing data of 3 species) from R repository.
df = sm.datasets.get_rdataset("iris").data 
df.info()
print(df.Species.unique() )

#iris = df

# Subset the data of only two species.
df_subset = df[(df.Species == "versicolor") | (df.Species == "virginica" )].copy() 

#Perform transformations, if required.
df_subset.Species = df_subset.Species.map({"versicolor": 1, "virginica": 0}) 

# Inplace keyword not working
#df_subset.rename(columns={"Sepal.Length": "Sepal_Length", "Sepal.Width": "Sepal_Width",	"Petal.Length": "Petal_Length", "Petal.Width": "Petal_Width"}, Inplace=True) 

#Define a patsy formula and create a model using logit.
model = smf.logit("Species ~ Petal.Length + Petal.Width", data=df_subset)
result = model.fit() 
print(f"result : {result}")

#Fit the model with supplied data.
df_new = pd.DataFrame({"Petal_Length": np.random.randn(20)*0.5 + 5,
                       "Petal_Width": np.random.randn(20)*0.5 + 1.7})
df_new["P-Species"] = result.predict(df_new)
df_new["P-Species"].head(3)

df_new["Species"] = (df_new["P-Species"] > 0.5).astype(int)
df_new.head()

#View summary of the model.
result.summary()

