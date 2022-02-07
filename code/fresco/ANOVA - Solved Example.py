import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats import anova


# Loading the Dataset
icecream = sm.datasets.get_rdataset("Icecream", "Ecdat")
icecream_data = icecream.data

# Building the Model
model1 = smf.ols('cons ~ temp', icecream_data).fit()

# Now let's frame a null hypothesis: Value of B1, i.e., the coefficient of temp variable is zero.
# anova_lm method from anova module of statsmodels library can be used for performing ANOVA.
print(anova.anova_lm(model1))

# Now let's create a new model with two independent variables and one response variable
model2 = smf.ols('cons ~ income + temp', icecream_data).fit()
print(anova.anova_lm(model2))

#print(stats.f.sf(31.81, 2, 27))

print('\n\n\n----------------Comparing Model----------------')
print(anova.anova_lm(model1, model2))