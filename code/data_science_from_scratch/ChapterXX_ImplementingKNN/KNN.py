import math as m
import collections as c

# ---------------------------------------------------------------------------------------------------------------
# Source : https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

#This k-Nearest Neighbors tutorial is broken down into 3 parts:
    #Step 1: Calculate Euclidean Distance. ie build infra to calculate distance for any row when compare to a dataset
    #Step 2: Get Nearest Neighbors. ie find n number of matching neighbors for the unseen row
    #Step 3: Make Predictions. ie. for the n matched neighbors return the most repeating output as predicted value


# ----------------------------------------------------------------------------------------------------------------

# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    #print('\n')
    distance = 0.0
    for i in range(len(row1) - 1):
        #print(f"row1 : {row1} row2 : {row2} ")
        #print(f"row1[i] = {row1[i]} row2[i] = {row2[i]} distance = {distance}")
        distance += (row1[i] - row2[i])**2
    return m.sqrt(distance)

# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
    print(f"\ngetting {num_neighbors} neighbors for {test_row}")
    distances = list()
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors

# Make a classification prediction with neighbors
# basically, the function only check what is the most common output value
def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors] # row[-1] returns the last value in list
    prediction = max(set(output_values), key=output_values.count) # just return the most repeating value in set
    return prediction

# Test distance function
dataset = [[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,0],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]]

row0 = dataset[0]

# test Step 1: Calculate Euclidean Distance.
"""
for row in dataset:
	distance = euclidean_distance(row0, row)
	print(distance)
"""

# test Step 2: Get Nearest Neighbors.
"""
# print 03 nearest neighbour to dataset[0]
train_dataset = dataset
test_row = dataset[0]
neighbors = get_neighbors(train_dataset, test_row , 3)
for neighbor in neighbors:
	print(neighbor)


# print 03 nearest neighbour to dataset[0]
train_dataset = dataset
test_row = dataset[3]
neighbors = get_neighbors(train_dataset, test_row , 3)
for neighbor in neighbors:
	print(neighbor)
"""

# test Step 3: Make Predictions.    
prediction = predict_classification(dataset, [1,-1], 3)
print(prediction)

prediction = predict_classification(dataset, [5,-4], 3)
print(prediction)

# example below to understand predicition
"""
output_values = [10,20,30,20,10,10,20,20,20,30]
print(output_values)
print(c.Counter(output_values))
print(set(output_values))
print(f"output_values.count : {output_values.count}")
print(max(set(output_values), key=output_values.count))
"""




