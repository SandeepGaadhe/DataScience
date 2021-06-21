import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd

# Load the R data set mtcars as a pandas dataframe.
mtcars = sm.datasets.get_rdataset("mtcars", "datasets", cache=True).data
df = pd.DataFrame(mtcars)

# Build another linear regression model by considering the log of independent variable wt, and log of dependent variable mpg.
model = smf.ols(formula='np.log(mpg) ~ np.log(wt)', data=mtcars)

# Fit the model with data, and display the R-squared value.
linear_model_result = model.fit()

#slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

print(linear_model_result.summary())
