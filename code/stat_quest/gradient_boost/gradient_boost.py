# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 19:13:33 2022

@author: Sandeep Gaadhe
"""

# https://www.youtube.com/watch?v=3CC4N4z3GJc&t=0s

# In[]:

import pandas as pd
import numpy as np

# In[]:

# In[]:

df_orig = None
df_orig = pd.DataFrame(columns = ['Height', 'Favorite Color', 'Gender', 'Weight'], dtype = object)

# In[]:


# append rows to an empty DataFrame

df_orig = df_orig.append({'Height' : 1.6, 'Favorite Color' : 'Blue', 'Gender' : 'Male','Weight' : 88}, 
               ignore_index = True)

df_orig = df_orig.append({'Height' : 1.6, 'Favorite Color' : 'Green', 'Gender' : 'Female','Weight' : 76}, 
               ignore_index = True)

df_orig = df_orig.append({'Height' : 1.5, 'Favorite Color' : 'Blue', 'Gender' : 'Female','Weight' : 56}, 
               ignore_index = True)

df_orig = df_orig.append({'Height' : 1.8, 'Favorite Color' : 'Red', 'Gender' : 'Male','Weight' : 73}, 
               ignore_index = True)

df_orig = df_orig.append({'Height' : 1.5, 'Favorite Color' : 'Green', 'Gender' : 'Male','Weight' : 77}, 
               ignore_index = True)

df_orig = df_orig.append({'Height' : 1.4, 'Favorite Color' : 'Blue', 'Gender' : 'Female','Weight' : 57}, 
               ignore_index = True)


# In[]:

label = 'Weight'
feature_list = [x for x in df_orig.columns if x != label]

    
# In[]:

df_train = df_orig.copy()


# In[]:

def calc_pseudo_residual(df_train, predicated_column_name, residual_column_name):
    df_train[residual_column_name] = df_train[label] - df_train[predicated_column_name]


# In[]:

def assign_leaf_type(p_df):

    p_df['leaf_type'] = None # add a None column so that subsequent lambda do not fail
    p_df['leaf_type'] = p_df.apply(lambda x: 'leaf_11' if x['Gender'] == 'Female' and x['Height'] < 1.6 else x['leaf_type'], axis = 1)
    p_df['leaf_type'] = p_df.apply(lambda x: 'leaf_10' if x['Gender'] == 'Female' and x['Height'] >= 1.6 else x['leaf_type'], axis = 1)
    p_df['leaf_type'] = p_df.apply(lambda x: 'leaf_01' if x['Gender'] != 'Female' and x['Favorite Color'] != 'Blue' else x['leaf_type'], axis = 1)
    p_df['leaf_type'] = p_df.apply(lambda x: 'leaf_00' if x['Gender'] != 'Female' and x['Favorite Color'] == 'Blue' else x['leaf_type'], axis = 1)
    
    return p_df

# In[]:

def calc_leaf_weight(df_train, residual_column_name, leaf_column_name):

    # we need to determine how to identify root node for a regression
    # or how to use gini_impurity for regression
    
    # for now, we are taking Gender as root node
    
    # also, in gradient boost, we have to fix the number of leaf nodes
    # in this case, leaf_node = 4
    
    leaf_wt_11 = round(np.average(df_train[(df_train['Gender'] == 'Female') & (df_train['Height'] < 1.6) ][residual_column_name]), 2)
    leaf_wt_10 = round(np.average(df_train[(df_train['Gender'] == 'Female') & (df_train['Height'] >= 1.6) ][residual_column_name]), 2)
    leaf_wt_01 = round(np.average(df_train[(df_train['Gender'] != 'Female') & (df_train['Favorite Color'] != 'Blue') ][residual_column_name]), 2)
    leaf_wt_00 = round(np.average(df_train[(df_train['Gender'] != 'Female') & (df_train['Favorite Color'] == 'Blue') ][residual_column_name]), 2)
    
    df_train[leaf_column_name] = None # add a None column so that subsequent lambda do not fail
    df_train[leaf_column_name] = df_train.apply(lambda x: leaf_wt_11 if x['Gender'] == 'Female' and x['Height'] < 1.6 else x[leaf_column_name], axis = 1)
    df_train[leaf_column_name] = df_train.apply(lambda x: leaf_wt_10 if x['Gender'] == 'Female' and x['Height'] >= 1.6 else x[leaf_column_name], axis = 1)
    df_train[leaf_column_name] = df_train.apply(lambda x: leaf_wt_01 if x['Gender'] != 'Female' and x['Favorite Color'] != 'Blue' else x[leaf_column_name], axis = 1)
    df_train[leaf_column_name] = df_train.apply(lambda x: leaf_wt_00 if x['Gender'] != 'Female' and x['Favorite Color'] == 'Blue' else x[leaf_column_name], axis = 1)


# In[]:

def calc_predicated_weight(df_train, new_pred_col_name):
   
    df_train[new_pred_col_name] = df_train['pred_wt_0']
    
    # scope of imporvement, for loop not needed just use list comprehension
    for leaf_col in [leaf_col for leaf_col in df_train.columns if 'leaf_wt' in leaf_col]:
        df_train[new_pred_col_name] = df_train[new_pred_col_name] + (learning_rate * df_train[leaf_col])


# In[]:

total_trees = 6 # includes iter 0th tree
learning_rate = 0.1

df_train = assign_leaf_type(df_train)

for iter_no in range(total_trees):
    
    curr_pred_col_name = 'pred_wt_' + str(iter_no)
    curr_resd_col_name = 'resd_wt_' + str(iter_no)
    curr_leaf_col_name = 'leaf_wt_' + str(iter_no)
    
    prev_resd_col_name = 'resd_wt_' + str(iter_no - 1)
    
    if iter_no == 0:
        df_train[curr_resd_col_name] = 0
        df_train[curr_pred_col_name] = round(np.average(df_train[label]), 2)
        continue
    
    calc_leaf_weight(df_train, prev_resd_col_name, curr_leaf_col_name) 
    calc_predicated_weight(df_train, curr_pred_col_name)   
    calc_pseudo_residual(df_train, curr_pred_col_name, curr_resd_col_name)

#    prev_resd_col_name = 'resd_wt_' + str(iter_no - 1)
#    prev_leaf_col_name = 'leaf_wt_' + str(iter_no - 1)
#    
#    calc_leaf_weight(df_train, prev_resd_col_name, prev_leaf_col_name)
#    calc_pseudo_residual(df_train, curr_pred_col_name, curr_resd_col_name)

# In[]:

def get_model():
    
    # scope of improvement
    pred_col_list = ['leaf_type']
    for pred_col in [pred_col for pred_col in df_train.columns if 'pred' in pred_col]:
        pred_col_list.append(pred_col)
    
    #model_cols = 'leaf_type' + pred_col_list
    return df_train[pred_col_list].drop_duplicates()

# In[]:

def predict_weight(df_test):
    
    for pred_col in [pred_col for pred_col in df_train.columns if 'pred' in pred_col]:
        df_test[pred_col] = round(np.average(df_train[(df_train['leaf_type'] == df_test['leaf_type'])][pred_col]), 2)
        
        
    
# In[]:


# let's get a new unseen row and predict weight based on above model
df_test = None
df_test = pd.DataFrame(columns = ['Height', 'Favorite Color', 'Gender', 'Weight'], dtype = object)
df_test = df_test.append({'Height' : 1.7, 'Favorite Color' : 'Green', 'Gender' : 'Female','Weight' : None}, 
               ignore_index = True)

df_test = df_test.append({'Height' : 1.2, 'Favorite Color' : 'Blue', 'Gender' : 'Male','Weight' : None}, 
               ignore_index = True)

# In[]:

# assign leaf type and get model
assign_leaf_type(df_test)
df_model = get_model()
df_test = pd.merge(df_test, df_model, how="left", on=['leaf_type'])

# In[]:

# scope of improvement, we just need the last tree prediction or
# we can edit the model to just return the last tree prediction
for pred_col in [pred_col for pred_col in df_test.columns if 'pred' in pred_col]:
    df_test[label] = df_test[pred_col]
    

# In[]:
# The End - Thank you!!!
    
