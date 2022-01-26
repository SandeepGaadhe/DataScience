#!/usr/bin/env python
# coding: utf-8

# https://www.youtube.com/watch?v=LsK-xG1cLYA

# In[58]:


import pandas as pd
import numpy as np
import random

# In[30]:


def cal_gini(p_df, p_label, p_index = 'Index', p_unique_threshold = 5):

    
    df_return = pd.DataFrame(columns = ['feature_name', 'feature_value', 'label_count_1', 'label_count_0', 'gini_leaf', 'gini_feature'], dtype = object)
    
    p_df[p_label] = p_df[p_label].replace(['Yes','No'],[1,0])

    for currColName in p_df.columns:
    
        if currColName == p_label or currColName == p_index: # skip if the column is target label or index
            continue
    
        if p_df[currColName].nunique() > p_unique_threshold: # skip considering it root node if distinct value is more than 9
            continue

        df_curr_col = p_df[[p_index, currColName, p_label]]
        
        # massaging df_curr_col
        df_curr_col[currColName] = df_curr_col[currColName].replace(['Yes','No'],[1,0])
        df_curr_col = df_curr_col[df_curr_col[currColName].notna()]
        
        for currColValue in df_curr_col[currColName].unique():
            
            labelCount1 = int((df_curr_col[(df_curr_col[currColName] == currColValue) & (df_curr_col[p_label] == 1)])[p_index].agg(['count']))
            labelCount0 = int((df_curr_col[(df_curr_col[currColName] == currColValue) & (df_curr_col[p_label] == 0)])[p_index].agg(['count']))
            total = labelCount1 + labelCount0
            
            gini_leaf = None #reset 
            if total != 0:
                gini_leaf = 1 - ((labelCount1/total)**2) - ((labelCount0/total)**2)
            
            #locals()[f' gini_leaf_{currColValue}'] = gini_leaf
            #locals()[f' total_{currColValue}'] = total
            
            #print(f'currColName : {currColName} currColValue : {currColValue} survived : {survived} notSurvived : {notSurvived} gini : {gini}')
            df_return = df_return.append({'feature_name' : currColName, 'feature_value' : currColValue, 'label_count_1' : labelCount1, 'label_count_0' : labelCount0, 'gini_leaf' : gini_leaf }, ignore_index = True)
        
        # reset variables
        total_1 = None
        gini_leaf_1 = None
        total_0 = None
        gini_leaf_0 = None
        
        # calculate gini_feature
        
        if not ((df_return[(df_return['feature_name'] == currColName) & (df_return['feature_value'] == 1)].empty) or (df_return[(df_return['feature_name'] == currColName) & (df_return['feature_value'] == 0)].empty)):
            total_1 = int(df_return[(df_return['feature_name'] == currColName) & (df_return['feature_value'] == 1)]['label_count_1']) + int(df_return[(df_return['feature_name'] == currColName) & (df_return['feature_value'] == 1)]['label_count_0'])
            gini_leaf_1 = float(df_return[(df_return['feature_name'] == currColName) & (df_return['feature_value'] == 1)]['gini_leaf'])
            total_0 = int(df_return[(df_return['feature_name'] == currColName) & (df_return['feature_value'] == 0)]['label_count_1']) + int(df_return[(df_return['feature_name'] == currColName) & (df_return['feature_value'] == 0)]['label_count_0'])
            gini_leaf_0 = float(df_return[(df_return['feature_name'] == currColName) & (df_return['feature_value'] == 0)]['gini_leaf'])
            gini_feature = ((total_1/(total_1 + total_0)) * gini_leaf_1) + ((total_0/(total_1 + total_0)) * gini_leaf_0)
            df_return['gini_feature'].mask(df_return['feature_name'] == currColName, gini_feature, inplace=True)
        
    # sort by gini_feature to identify root
    df_return = df_return.sort_values(by=['gini_feature'])    
    return df_return



# In[101]:

df = None
df = pd.DataFrame(columns = ['Chest Pain', 'Blocked Arteries', 'Patient Weight', 'Heart Disease'], dtype = object)


# In[102]:


# append rows to an empty DataFrame

df = df.append({'Chest Pain' : 'Yes', 'Blocked Arteries' : 'Yes', 'Patient Weight' : 205,'Heart Disease' : 'Yes'}, 
               ignore_index = True)

df = df.append({'Chest Pain' : 'No', 'Blocked Arteries' : 'Yes', 'Patient Weight' : 180,'Heart Disease' : 'Yes'}, 
               ignore_index = True)

df = df.append({'Chest Pain' : 'Yes', 'Blocked Arteries' : 'No', 'Patient Weight' : 210,'Heart Disease' : 'Yes'}, 
               ignore_index = True)

df = df.append({'Chest Pain' : 'Yes', 'Blocked Arteries' : 'Yes', 'Patient Weight' : 167,'Heart Disease' : 'Yes'}, 
               ignore_index = True)

df = df.append({'Chest Pain' : 'No', 'Blocked Arteries' : 'Yes', 'Patient Weight' : 156,'Heart Disease' : 'No'}, 
               ignore_index = True)

df = df.append({'Chest Pain' : 'No', 'Blocked Arteries' : 'Yes', 'Patient Weight' : 125,'Heart Disease' : 'No'}, 
               ignore_index = True)

df = df.append({'Chest Pain' : 'Yes', 'Blocked Arteries' : 'No', 'Patient Weight' : 168,'Heart Disease' : 'No'}, 
               ignore_index = True)

df = df.append({'Chest Pain' : 'Yes', 'Blocked Arteries' : 'Yes', 'Patient Weight' : 172,'Heart Disease' : 'No'}, 
               ignore_index = True)

df_Orig = df.copy()

lv_label = 'Heart Disease'

# In[103]:

# temporarily we have encoded patient weight if it is more than 176 lb or not
# to get how 176 lb was calculated, please see decision tree implementation

df['Patient Weight'] = df.apply(lambda x: 'Yes' if x['Patient Weight'] > 176 else 'No', axis = 1)
df.rename(columns={'Patient Weight': 'Patient Obese'}, inplace=True)

# In[103]:

feature_list = []
for feature in df.columns:
    feature_list = feature_list + [feature]
df = df.reindex(columns=['Index'] + feature_list)
df["Index"] = df.index + 1

feature_list.insert(0, 'Index')

# In[105]:

df['Sample Weight 0'] = 1/len(df)

# In[113]:


#def cal_gini(p_df, p_label, p_index = 'Index', p_unique_threshold = 5):

df_gini = cal_gini(p_df = df[feature_list], p_label = lv_label, p_index = 'Index')

# In[ ]:

df_amount_of_say = pd.DataFrame(columns = ['feature_name', 'total_error', 'amount_of_say'], dtype = object)

# bad practice to iterate over a dataframe
for row in (df_gini[['feature_name', 'gini_feature']].drop_duplicates(inplace = False)).itertuples():
    total_error = float(df[(df[row.feature_name] != df['Heart Disease'])]['Sample Weight 0'].agg('sum'))
    amount_of_say = round((1/2)*(np.log((1 - total_error)/total_error)), 2)
    df_amount_of_say = df_amount_of_say.append({'feature_name' : row.feature_name, 'total_error' : total_error, 'amount_of_say' : amount_of_say}, ignore_index = True)

# In[ ]:

# let's calculate the new sample weight

stump_0 = df_gini.loc[df_gini['gini_feature'].idxmin()]['feature_name']

amount_of_say = float(df_amount_of_say[(df_amount_of_say['feature_name'] == stump_0)]['amount_of_say'])

df['Sample Weight 1'] = df.apply(lambda x: (x['Sample Weight 0'] * np.exp(amount_of_say)) if x[stump_0] != x[lv_label] else (x['Sample Weight 0'] * np.exp(-amount_of_say)), axis = 1)

# regularize for new sample weight

sample_wt_1_sum = df['Sample Weight 1'].agg('sum')
df['Sample Weight 1'] = df.apply(lambda x: x['Sample Weight 1'] / sample_wt_1_sum, axis = 1)

# In[ ]:

# as mentioned in video, we can use weighted gini index 
# for next stump or we can make a new sample space using
# above sample weight 1 of same size as earlier(08 rows)

# below implementation is as per video where a new 
# sample space of 08 rows is created using sample weight 1


df['CumSum Sample Wt 1'] = df['Sample Weight 1'].cumsum()

# In[ ]:

df1 = pd.DataFrame(data=None, columns=df.columns, dtype = object)

# for loop just for illustration as how the more weighted rows 
# get picked more frequently

for i in range(8):
    r = random.random()
    df_firstRow = df[(df['CumSum Sample Wt 1'] >= r)].iloc[:1]
    df1 = df1.append(df_firstRow)

# In[ ]:

#df1.to_csv(r'S:\SandeepG\Official\DataScience\gitHub\code\stat_quest\ada_boost\df1.csv')


# In[ ]:


# for future reference here is the df1

# =============================================================================
# Index	Chest   Blocked     Patient Heart   Sample      Sample      CumSum
#         Pain	Arteries	Obese	Disease	Weight 0    Weight 1	Sample Wt 1
# 1	    Yes	    Yes	        Yes	    Yes	    0.125	    0.07        0.07163964756614223
# 4	    Yes	    Yes	        No	    Yes	    0.125	    0.49        0.7134414097354311
# 1	    Yes	    Yes	        Yes	    Yes	    0.125	    0.07        0.07163964756614223
# 4	    Yes	    Yes	        No	    Yes	    0.125	    0.49        0.7134414097354311
# 5	    No	    Yes	        No	    No	    0.125	    0.07        0.785081
# 8	    Yes	    Yes	        No	    No	    0.125	    0.07        1
# 4	    Yes	    Yes	        No	    Yes	    0.125	    0.49        0.7134414097354311
# 4	    Yes	    Yes	        No	    Yes	    0.125	    0.49        0.7134414097354311
# 
# 
# =============================================================================

# In[ ]:

# to keep program in sync we are overwriting
df1  = None
df1 = pd.DataFrame(columns = ['df0 Index', 'Chest Pain', 'Blocked Arteries', 'Patient Obese', 'Heart Disease', 'Sample Weight 0', 'Sample Weight 1', 'CumSum Sample Wt 1'], dtype = object)

df1 = df1.append({'df0 Index' : 1, 
                  'Chest Pain' : 'Yes', 
                  'Blocked Arteries' : 'Yes', 
                  'Patient Obese' : 'Yes',
                  'Heart Disease' : 'Yes',
                  'Sample Weight 0' : 0.125,
                  'Sample Weight 1' : np.NaN,
                  'CumSum Sample Wt 1' : np.NaN
                  }, ignore_index = True)
#2
df1 = df1.append({'df0 Index' : 4, 
                  'Chest Pain' : 'Yes', 
                  'Blocked Arteries' : 'Yes', 
                  'Patient Obese' : 'No',
                  'Heart Disease' : 'Yes',
                  'Sample Weight 0' : 0.125,
                  'Sample Weight 1' : np.NaN,
                  'CumSum Sample Wt 1' : np.NaN
                  }, ignore_index = True)
#3
df1 = df1.append({'df0 Index' : 1, 
                  'Chest Pain' : 'Yes', 
                  'Blocked Arteries' : 'Yes', 
                  'Patient Obese' : 'Yes',
                  'Heart Disease' : 'Yes',
                  'Sample Weight 0' : 0.125,
                  'Sample Weight 1' : np.NaN,
                  'CumSum Sample Wt 1' : np.NaN
                  }, ignore_index = True)
    
#4
df1 = df1.append({'df0 Index' : 4, 
                  'Chest Pain' : 'Yes', 
                  'Blocked Arteries' : 'Yes', 
                  'Patient Obese' : 'No',
                  'Heart Disease' : 'Yes',
                  'Sample Weight 0' : 0.125,
                  'Sample Weight 1' : np.NaN,
                  'CumSum Sample Wt 1' : np.NaN
                  }, ignore_index = True)
    
#5
df1 = df1.append({'df0 Index' : 5, 
                  'Chest Pain' : 'No', 
                  'Blocked Arteries' : 'Yes', 
                  'Patient Obese' : 'No',
                  'Heart Disease' : 'No',
                  'Sample Weight 0' : 0.125,
                  'Sample Weight 1' : np.NaN,
                  'CumSum Sample Wt 1' : np.NaN
                  }, ignore_index = True)
    
#6
df1 = df1.append({'df0 Index' : 8, 
                  'Chest Pain' : 'Yes', 
                  'Blocked Arteries' : 'Yes', 
                  'Patient Obese' : 'No',
                  'Heart Disease' : 'No',
                  'Sample Weight 0' : 0.125,
                  'Sample Weight 1' : np.NaN,
                  'CumSum Sample Wt 1' : np.NaN
                  }, ignore_index = True)
    
#7
df1 = df1.append({'df0 Index' : 4, 
                  'Chest Pain' : 'Yes', 
                  'Blocked Arteries' : 'Yes', 
                  'Patient Obese' : 'No',
                  'Heart Disease' : 'Yes',
                  'Sample Weight 0' : 0.125,
                  'Sample Weight 1' : np.NaN,
                  'CumSum Sample Wt 1' : np.NaN
                  }, ignore_index = True)
    
#8
df1 = df1.append({'df0 Index' : 4, 
                  'Chest Pain' : 'Yes', 
                  'Blocked Arteries' : 'Yes', 
                  'Patient Obese' : 'No',
                  'Heart Disease' : 'Yes',
                  'Sample Weight 0' : 0.125,
                  'Sample Weight 1' : np.NaN,
                  'CumSum Sample Wt 1' : np.NaN
                  }, ignore_index = True)
    
    
    
# In[ ]:

# now we will calculate the gini_index for df1

# note that df1 four rows that has df0 index = 4 row 
# we will keep the sample weight 0 as 1/8 and recalculate sampel wt 1 for df1

df1["Index"] = df1.index + 1
#feature_list.insert(0, 'Index')
df1_gini = cal_gini(p_df = df1[feature_list], p_label = lv_label, p_index = 'Index')

# In[ ]:

df1_amount_of_say = pd.DataFrame(columns = ['feature_name', 'total_error', 'amount_of_say'], dtype = object)

# bad practice to iterate over a dataframe
for row in (df1_gini[['feature_name', 'gini_feature']].drop_duplicates(inplace = False)).itertuples():
    total_error = float(df1[(df1[row.feature_name] != df1['Heart Disease'])]['Sample Weight 0'].agg('sum'))
    amount_of_say = round((1/2)*(np.log((1 - total_error)/total_error)), 2)
    df1_amount_of_say = df1_amount_of_say.append({'feature_name' : row.feature_name, 'total_error' : total_error, 'amount_of_say' : amount_of_say}, ignore_index = True)

# In[ ]:

# let's calculate the new sample weight for df1

stump_1 = df1_gini.loc[df1_gini['gini_feature'].idxmin()]['feature_name']

amount_of_say = float(df1_amount_of_say[(df1_amount_of_say['feature_name'] == stump_1)]['amount_of_say'])

df1['Sample Weight 1'] = df1.apply(lambda x: (x['Sample Weight 0'] * np.exp(amount_of_say)) if x[stump_1] != x[lv_label] else (x['Sample Weight 0'] * np.exp(-amount_of_say)), axis = 1)

# regularize for new sample weight

sample_wt_1_sum = df1['Sample Weight 1'].agg('sum')
df1['Sample Weight 1'] = df1.apply(lambda x: x['Sample Weight 1'] / sample_wt_1_sum, axis = 1)


# In[ ]:


df1['CumSum Sample Wt 1'] = df1['Sample Weight 1'].cumsum()



# In[ ]:


df2 = pd.DataFrame(data=None, columns=df.columns, dtype = object)

# for loop just for illustration as how the more weighted rows 
# get picked more frequently

for i in range(8):
    r = random.random()
    df1_firstRow = df1[(df1['CumSum Sample Wt 1'] >= r)].iloc[:1]
    df2 = df2.append(df1_firstRow)


# In[ ]:





# In[ ]:




