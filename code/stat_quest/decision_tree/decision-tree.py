#!/usr/bin/env python
# coding: utf-8

# In[2]:


# # Task : 
# 1. Create a decision tree for the dataset
# 2. Create confusion matrix, Gini Impurity etc
# 3. Perform prediction & calculate accuracy
# 4. Build the same program using built-in lib

# # 1. Create a decision tree for the dataset

# 1.1 read the csv

# In[2]:

# imports section
import pandas as pd

# In[2]:


# df891 = pd.read_csv('../input/titanic893/titanic_893.csv') # kaggle

df_origDataSet = None
df = None

df_origDataSet = pd.read_csv(r'S:\SandeepG\Official\DataScience\gitHub\data\stat_quest\decision_tree\heart_disease.csv') # local

df = df_origDataSet.copy(deep = True) 


col_list = []
for col in df.columns:
    col_list = col_list + [col]

df = df.reindex(columns=['Index'] + col_list)
df["Index"] = df.index + 1

df_origDataSet.head(5)

df.head(5)


# # 2. Create confusion matrix, Gini Impurity etc

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
        
        # calculate gini for root
        
        total_1 = int(df_return[(df_return['feature_name'] == currColName) & (df_return['feature_value'] == 1)]['label_count_1']) + int(df_return[(df_return['feature_name'] == currColName) & (df_return['feature_value'] == 1)]['label_count_0'])
        total_0 = int(df_return[(df_return['feature_name'] == currColName) & (df_return['feature_value'] == 0)]['label_count_1']) + int(df_return[(df_return['feature_name'] == currColName) & (df_return['feature_value'] == 0)]['label_count_0'])
        gini_leaf_1 = float(df_return[(df_return['feature_name'] == currColName) & (df_return['feature_value'] == 1)]['gini_leaf'])
        gini_leaf_0 = float(df_return[(df_return['feature_name'] == currColName) & (df_return['feature_value'] == 0)]['gini_leaf'])
        
        gini_feature = ((total_1/(total_1 + total_0)) * gini_leaf_1) + ((total_0/(total_1 + total_0)) * gini_leaf_0)
        df_return['gini_feature'].mask(df_return['feature_name'] == currColName, gini_feature, inplace=True)
    
    # sort by gini_feature to identify root
    df_return = df_return.sort_values(by=['gini_feature'])    
    return df_return


# In[31]:

"""
df = pd.DataFrame(columns = ['feature_name', 'feature_value', 'label_count_1', 'label_count_0', 'gini_leaf', 'gini_feature'], dtype = object)

df = df.append({'feature_name' : 'Chest Pain', 'feature_value' : 0, 
                'label_count_1' : 34, 'label_count_0' : 125, 'gini_leaf' : 0.336221, 'gini_feature' : None}, 
               ignore_index = True)

df = df.append({'feature_name' : 'Chest Pain', 'feature_value' : 1, 
                'label_count_1' : 105, 'label_count_0' : 39, 'gini_leaf' : 0.394965, 'gini_feature' : None}, 
               ignore_index = True)


#df.head()

#      ColName ColValue Heart Disease_1 Heart Disease_0  gini_leaf  gini_feature
#0  Chest Pain        0              34             125   0.336221           NaN
#1  Chest Pain        1             105              39   0.394965           NaN

"""

# In[31]:

df_gini = cal_gini(p_df = df, p_index = 'Index', p_label = 'Heart Disease', p_unique_threshold = 3)


# In[31]:

#the code is completed up to this point
#next to do:
#    - identify root node which is GBC in this case based on lowest gini
#    - iteratively define branch node until a leaf node is identified
#    - start video at time https://youtu.be/7VeUPuFGJHk?t=612

# In[33]:


df_root = pd.DataFrame(df)

df_root['branch1_SexEqMale'] = df_root["Sex"].apply(lambda x: 1 if x == 'male' else 0)
df_root['branch2_SexNEqMale'] = df_root["Sex"].apply(lambda x: 1 if x == 'female' else 0)

#df_root['branch11_PclassEq3'] = df_root["Pclass"].apply(lambda x: 1 if (x == 3) else 0)
df_root['branch11_PclassEq3'] = df_root.apply(lambda x: 1 if x['branch1_SexEqMale'] == 1 and x['Pclass'] == 3 else 0, axis = 1)
df_root['branch12_PclassNEq3'] = df_root.apply(lambda x: 1 if x['branch1_SexEqMale'] == 1 and x['Pclass'] != 3 else 0, axis = 1)

df_root['branch111_EmbarkedEqS'] = df_root.apply(lambda x: 1 if x['branch11_PclassEq3'] == 1 and x['Embarked'] == 'S' else 0, axis = 1)
df_root['branch112_EmbarkedNEqS'] = df_root.apply(lambda x: 1 if x['branch11_PclassEq3'] == 1 and x['Embarked'] != 'S' else 0, axis = 1)

for col_name in df_root.filter(regex='^branch',axis=1).columns: 
    col_count = int(df_root[(df_root[col_name] == 1)].PassengerId.agg(['count']))
    survived = int(df_root[(df_root[col_name] == 1) & (df_root.Survived == 1)].PassengerId.agg(['count']))
    notSurvived = int(df_root[(df_root[col_name] == 1) & (df_root.Survived == 0)].PassengerId.agg(['count']))
    print(f'col_name : {col_name} col_count : {col_count} survived : {survived} notSurvived : {notSurvived} Percent : {(notSurvived/(survived + notSurvived))*100}')
    


# # 3. Perform prediction & calculate accuracy
# 
# Performing prediction for Male passenger only

# In[36]:


# our analysis says that Passenger = Male & Pclass = 3 has 86% chances of not surviving

# for our prediction, ,we will discard any row which is not male

for i in range(0,10):
    
    df_prediction = None
    correctPredCount = None
    inCorrectPredCount = None
    accuracy = None
    maxPassengerId = None
    minPassengerId = None
    
    r = random.randint(70, 100)
    
    df_test = df_root[(df_root['Sex'] == 'male')].sample(n = r)

    df_prediction = df_test[['PassengerId', 'Sex', 'Pclass', 'Survived']]

    df_prediction['Survived_Pred'] = df_prediction.apply(lambda x: 0 if x['Sex'] == 'male' and x['Pclass'] == 3 else 1, axis = 1)
    df_prediction['Pred_Match'] = df_prediction.apply(lambda x: 1 if x['Survived'] == x['Survived_Pred'] else 0, axis = 1)

    maxPassengerId = df_prediction['PassengerId'].max()
    minPassengerId = df_prediction['PassengerId'].min()
    correctPredCount = df_prediction[(df_prediction['Pred_Match'] == 1)].PassengerId.count()
    inCorrectPredCount = df_prediction[(df_prediction['Pred_Match'] == 0)].PassengerId.count()

    accuracy = int(((correctPredCount/(correctPredCount + inCorrectPredCount))) * 100)

    print(f'Iteration : {i}. Sample Size : {r} MaxPassengerId : {maxPassengerId} MinPassengerId : {minPassengerId} \tMy Decision Tress Accuracy : {accuracy} %. ')



# # ******************************* End Of Program -- Thank You -- ***********************
