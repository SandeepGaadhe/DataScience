import statsmodels.api as sm
import statsmodels.formula.api as smf

# Let's understand how to fit a linear regression model for Icecream dataset available from R Data Repository.

# Loading the Dataset
icecream = sm.datasets.get_rdataset("Icecream", "Ecdat")
icecream_data = icecream.data
print(icecream_data.columns)


# Creating a Model
linear_model1 = smf.ols('cons ~ price + temp', icecream_data)
# Fitting the Model
linear_result1 = linear_model1.fit()
print(linear_result1.summary())
print('-------------------------------------------\n\n\n\n\n')

# Now let's create a new model by considered income and temp dependent variables.
linear_model2 = smf.ols('cons ~ income + temp', icecream_data)
linear_result2 = linear_model2.fit()
print(linear_result2.summary())
print('-------------------------------------------\n\n\n\n\n')

# Now let's create a new model without considering intercept term.
linear_model3 = smf.ols('cons ~ -1 + income + temp', icecream_data)
linear_result3 = linear_model3.fit()
print(linear_result3.summary())
print('-------------------------------------------\n\n\n\n\n')