import json
import math
import numpy as np 

json_load = None
with open('level2a.json', 'r') as json_file: #Loading json file
	json_load = json.load(json_file)

no_neighbourhoods = int(json_load['n_neighbourhoods'])
no_restaurants = int(json_load['n_restaurants'])
no_vehicles = len(json_load['vehicles'])
vehicles = json_load['vehicles']

neigh_data = {} #Key - Neighbourhood index, Value - [Distances, Order quantity]
neigh_label_template = 'n'

for i in range(no_neighbourhoods):  #Storing neighbourhood data into neigh_data dictionary
	neigh_label_template += str(i)

	neigh_data[neigh_label_template] = [json_load['neighbourhoods'][neigh_label_template]['distances'], json_load['neighbourhoods'][neigh_label_template]['order_quantity']]	

	neigh_label_template = 'n'

print(neigh_data)

tot_veh_capacity = {}
for vehicle in vehicles: #Storing vehicle capacity details
	tot_veh_capacity[vehicle] = json_load['vehicles'][vehicle]['capacity']

visited = [False] * no_neighbourhoods

result_dict = {}
for vehicle in vehicles:
	result_dict[vehicle] = []

curr_result = {}
for vehicle in vehicles:
	curr_result[vehicle] = ['r0']

res_to_neigh_distances = json_load['restaurants']['r0']['neighbourhood_distance']
k_closest_neigh_to_res_values = sorted(res_to_neigh_distances)[:no_vehicles]
closest_neigh_indices = [res_to_neigh_distances.index(val) for val in k_closest_neigh_to_res_values]

i = 0
for vehicle in vehicles:
	curr_result[vehicle].append('n' + str(closest_neigh_indices[i]))
	visited[closest_neigh_indices[i]] = True
	i+=1

max_val_index = None
min_dist_index = None

while not all(visited):
	for vehicle in vehicles:
		while curr_result[vehicle][-1]!='r0' and len(curr_result[vehicle])>=2:
		
			max_val = -math.inf
			orders = neigh_data[curr_result[vehicle][-1]][1]
			
			for i in range(len(neigh_data[curr_result[vehicle][-1]][0])):
				if neigh_data[curr_result[vehicle][-1]][0][i] == 0:
					continue
				if float(orders/neigh_data[curr_result[vehicle][-1]][0][i]) > max_val and not visited[i]:
					max_val = orders/neigh_data[curr_list[-1]][0][i]
					max_val_index = i

		if curr_capacity < orders:
			curr_list.append('r0')
			result_list.append(curr_list)
		else:
			visited[max_val_index] = True
			curr_list.append('n' + str(max_val_index))
			curr_capacity -= orders

	curr_list = ['r0']
	curr_capacity = tot_capacity
	min_dist = math.inf

	for i in range(len(res_to_neigh_distances)):
		if not visited[i] and res_to_neigh_distances[i]<min_dist:
			min_dist = res_to_neigh_distances[i]
			min_dist_index = i

	curr_list.append('n'+str(min_dist_index))
	curr_capacity -= orders
	visited[min_dist_index] = True

	if all(visited):
		curr_list.append('r0')
		result_list.append(curr_list)

result_dict = {}
for i in range(len(result_list)):
	result_dict['path'+str(i+1)] = result_list[i]

res_string = json.dumps(result_dict)
data = {
	"v0": result_dict
}

outfile_name = 'level1b_output.json'

with open(outfile_name, 'w') as json_file:
	json.dump(data, json_file, indent=4)'''