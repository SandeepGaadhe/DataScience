import pandas as pd
import statsmodels.formula.api as smf

# Poisson Model describes a process where dependent variable refers to success count of many attempts 
# and each attempt has a very low probability of success.

# Let's understand how to fit a Poisson regression model for a data set available at UCLA repository.

# The dataset contains details of a number of awards earned, type of program enrolled, 
# and score obtained in final math exam by students at a high school.

# The dataset is fetched as a pandas data frame as shown below.
awards_df = pd.read_csv("https://stats.idre.ucla.edu/stat/data/poisson_sim.csv")
print(awards_df.head(3))

# Now let's create a Poisson model with the patsy formula num_awards ~ math + C(prog).
poisson_model = smf.poisson('num_awards ~ math + C(prog)', awards_df)

# Fitting the Model
poisson_model_result = poisson_model.fit()

# Viewing Model Summary
# Analyzing Model Summary
# The coefficient for math variable is 0.07, which means for every one unit increase in math, the log count increases by 0.07.
# Having enrolled for prog=2, i.e., "Academic", instead of "Generic" program, changes the log count by 1.08.
# Having enrolled for prog=3, i.e., "Vocational", instead of "Generic" program, changes the log count by 0.37.

print(poisson_model_result.summary())