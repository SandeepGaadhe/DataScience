# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:33:20 2022

@author: admin
"""

# In[]:

import pandas as pd
import numpy as np

# In[]:


# In[]:

# list of weight
weights = [0.9, 1.8, 2.4, 3.5, 3.9, 4.4, 5.1, 5.6, 6.3]
  
# list of size
sizes = [1.4, 2.6, 1.0, 3.7, 5.5, 3.2, 3.0, 4.9, 6.3]


df_orig = pd.DataFrame(list(zip(weights, sizes)), columns =['weight', 'size'])

# In[]:
