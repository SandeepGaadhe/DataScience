import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd

# Load the R dataset biopsy from the MASS package.
biopsy_set = sm.datasets.get_rdataset('biopsy','MASS').data
#biopsy_set.info()

# Capture the data as a pandas dataframe.
df = pd.DataFrame(biopsy_set)
#print(df)

# Rename the column name class to Class.
df.rename(columns={'class' : 'Class'},inplace=True)
#print(df)

# Transform the Class column values benign and malignant to '0' and '1' respectively.
#df_subset.Species = df_subset.Species.map({"versicolor": 1, "virginica": 0}) 
df.Class = df.Class.map({"benign" : 0, "malignant" : 1})
#print(1)
# Build a logistic regression model with independent variable V1 and dependent variable Class.
model = smf.logit("Class ~ V1", data=df)

# Fit the model with data, and display the pseudo R-squared value.
result = model.fit() 
print(result.summary())

