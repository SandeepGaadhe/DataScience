import statsmodels.api as sm
import pandas as pd
import statsmodels.formula.api as smf

# Source : http://joelcarlson.github.io/2016/05/10/Exploring-Interactions/

#Perform the following tasks:

# Load the R dataset mtcars.
mtcars = sm.datasets.get_rdataset("mtcars", "datasets", cache=True).data
#print(mtcars.head()) #take a quick look

# Capture the data as a pandas dataframe.
df = pd.DataFrame(mtcars)
#print(df)

# Build a linear regression model with independent variable wt, and dependent variable mpg.
model = smf.ols(formula='mpg ~ wt', data=mtcars)

# Fit the model with data, and display the R-squared value.
linear_model_result = model.fit()
print(linear_model_result.summary())
