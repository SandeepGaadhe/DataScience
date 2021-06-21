import statsmodels.api as sm
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.stats import anova

# Load the R data set mtcars as a pandas dataframe.
mtcars = sm.datasets.get_rdataset("mtcars", "datasets", cache=True).data
df = pd.DataFrame(mtcars)

# Build a linear regression model by considering the log of independent variable wt, and log of dependent variable mpg.
# Fit the model with data.
model = smf.ols(formula='np.log(mpg) ~ np.log(wt)', data=mtcars).fit()

# Perform ANOVA on the linear model obtained in the previous step.(Hint:Use anova.anova_lm)
print(anova.anova_lm(model))

# Display the F-statistic value.
print(anova.anova_lm(model).F["np.log(wt)"])