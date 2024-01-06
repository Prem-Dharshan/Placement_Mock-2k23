import json
import math
#import numpy as np
 
json_load = None
with open('level0.json', 'r') as json_file: #Loading json file
	json_load = json.load(json_file)

no_neighbourhoods = int(json_load['n_neighbourhoods'])
no_restaurants = int(json_load['n_restaurants'])

# print('No. of neighbourhoods: ', no_neighbourhoods)
# print('No. of restaurants: ', no_restaurants)

neighbourhood_distances = {} #Key - Neighbourhood index, Value - Distance to every other neighbourhood
neigh_label_template = 'n'

for i in range(no_neighbourhoods):  #Storing neighbourhood distance data into neighbourhood_distances dictionary
	neigh_label_template += str(i)
	# print('Neigh index: ', neigh_label_template)

	neighbourhood_distances[neigh_label_template] = json_load['neighbourhoods'][neigh_label_template]['distances']
	
	# print('Distance list: ', neighbourhood_distances[neigh_label_template])
	neigh_label_template = 'n'

rest_to_neigh_dist = json_load['restaurants']['r0']['neighbourhood_distance']
min_dist_neigh = rest_to_neigh_dist.index(min(rest_to_neigh_dist))

# # Approach 2 - Creating distance matrix

# dist_matrix = np.empty((0,no_neighbourhoods), int)

# for neigh_label, dist_list in neighbourhood_distances.items():
# 	# print(dist_list)
# 	dist_matrix = np.append(dist_matrix, np.array([dist_list]), axis=0)

# min_cost = findMinRoute(dist_matrix)
# print('Total Min Cost: ', min_cost)	


# Approach 1 - Starting from restaurant, then closest neighbourhood, at each neighbourhood finding min dist
result_list = ['r0', 'n13']
min_dist = math.inf
tot_cost = 510

while len(result_list) != no_neighbourhoods + no_restaurants: 
	min_dist = math.inf
	for dist in neighbourhood_distances[result_list[-1]]:
		# print(neighbourhood_distances[result_list[-1]])
		# print('Exploring neigh: ', result_list[-1])
		if dist==0:
			continue
		if dist<min_dist and 'n'+str(neighbourhood_distances[result_list[-1]].index(dist)) not in result_list:
			min_dist = dist
		
	tot_cost += min_dist
	result_list.append('n'+str(neighbourhood_distances[result_list[-1]].index(min_dist)))

result_list.append('r0')
print('Result Path: ', result_list)
print('Total cost: ', tot_cost)

data = {
	"v0": {
		"path": result_list
	}
}

outfile_name = 'level0_out.json'

with open(outfile_name, 'w') as json_file:
	json.dump(data, json_file, indent=4)