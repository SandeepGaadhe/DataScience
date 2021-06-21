import statsmodels.api as sm
import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.stats import anova
 
# Load the R dataset mtcars.
mtcars = sm.datasets.get_rdataset("mtcars", "datasets", cache=True).data

# Capture the data as a pandas dataframe.
df = pd.DataFrame(mtcars)

# Build a linear regression model with independent variable wt, and dependent variable mpg.
# Fit the model with data
model = smf.ols(formula='mpg ~ wt', data=mtcars).fit()

# Perform ANOVA on the linear model obtained in the previous step.(Hint:Use anova.anova_lm)
print(anova.anova_lm(model))

# Display the F-statistic value.
#print(847.725250/9.277398)
print(anova.anova_lm(model).F["wt"])
#print(f.sf(31.81, 2, 27))