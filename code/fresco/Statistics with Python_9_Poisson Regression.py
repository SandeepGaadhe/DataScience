import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd

# Load the R dataset Insurance from the MASS package.
insurance_set = sm.datasets.get_rdataset('Insurance','MASS').data

# Capture the data as a pandas dataframe.
df = pd.DataFrame(insurance_set)

# Build a Poisson regression model with a log of an independent variable Holders, and dependent variable Claims.
poisson_model = smf.poisson('Claims ~ np.log(Holders)', df)

# Fit the model with data, and find the sum of the residuals.
poisson_model_result = poisson_model.fit()
print(np.sum(poisson_model_result.resid))