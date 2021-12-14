import sys

# start disk is current disk
# l is queue of pending requests
# increasing direction if cylinder numbers going up
# sample numbers 
"""
start = 2000
l = [2069, 1212,2296,2800,544,1618,356,1523,4965,3681]

increasing_direction = True
max_cylinder = 4999
"""


def fcfs(l, start):
	accessed_arr = [start]

	print("Start at: " + str(start))
	sum = 0
	sum += abs(l[0]-start)
	print("Move to: " + str(l[0]))
	accessed_arr.append(l[0])

	for i in range(1, len(l)):
		print("Move to: " + str(l[i]))
		sum += abs(l[i] - l[i-1])
		accessed_arr.append(l[i])

	print("Total distance: " + str(sum))
	return accessed_arr


def sstf(l, start):
	accessed_arr = [start]
	print("Start at: " + str(start))
	current_pos = start
	sum = 0

	for j in range(0, len(l)):
		closest_pos = sys.maxsize
		closest_pos_index = -1

		# calculates next closest position
		for i in range(0, len(l)):
			if(abs(l[i]-current_pos) < abs(closest_pos-current_pos)):
				closest_pos = l[i]
				closest_pos_index = i
	
		print("Move to: " + str(closest_pos))
		accessed_arr.append(closest_pos)
		sum += abs(current_pos-closest_pos)
		current_pos = closest_pos
		l[closest_pos_index] = -sys.maxsize
	
	print("Total distance: " + str(sum))
	return accessed_arr

def scan(l, increasing_direction, max_cylinder, start):
	accessed_arr = [start]
	print("Start at: " + str(start))
	current_pos = start
	l.append(max_cylinder)
	l.append(0)

	if(increasing_direction):
		l.sort()

		start_pos_index = -1
		#find current place in sorted list
		for i in range(0, len(l)):
			if(l[i] > current_pos):
				start_pos_index = i
				break
	else:
		l.sort(reverse=True)
		start_pos_index = -1
		#find current place in sorted list
		for i in range(0, len(l)):
			if(l[i] < current_pos):
				start_pos_index = i
				break

	#make list start at increasing one and jump back to smallest
	print(l)
	l_large = l[start_pos_index:]
	l_small = l[start_pos_index-1:0:-1]
	l_sorted = l_large + l_small
	print(l_large)
	print(l_small)
	print(l_sorted)

	print("Move to: " + str(l_sorted[0]))
	accessed_arr.append(l[0])
	sum = abs(current_pos-l_sorted[0])
	for i in range(1, len(l_sorted)):
		sum += abs(l_sorted[i] - l_sorted[i-1])
		print("Move to: " + str(l_sorted[i]))
		accessed_arr.append(l[i])
	
	print("Total distance: " + str(sum))
	return accessed_arr



def look(l, increasing_direction, start):
	accessed_arr = [start]
	print("Start at: " + str(start))
	current_pos = start
	l.append(0)

	if(increasing_direction):
		l.sort()
		start_pos_index = -1
		#find current place in sorted list
		for i in range(0, len(l)):
			if(l[i] > current_pos):
				start_pos_index = i
				break
	else:
		l.sort(reverse=True)
		start_pos_index = -1
		#find current place in sorted list
		for i in range(0, len(l)):
			if(l[i] < current_pos):
				start_pos_index = i
				break

	#make list start at increasing one and jump back to smallest
	l_large = l[start_pos_index:]
	l_small = l[start_pos_index:0:-1]
	l_sorted = l_large + l_small

	print(l_sorted)

	print("Move to: " + str(l_sorted[0]))
	accessed_arr.append(l[0])
	sum = abs(current_pos-l_sorted[0])
	for i in range(1, len(l_sorted)):
		print("Move to: " + str(l_sorted[i]))
		sum += abs(l_sorted[i] - l_sorted[i-1])
		accessed_arr.append(l[i])

	print("Total distance: " + str(sum))
	return accessed_arr



def cscan(l, increasing_direction, max_cylinder, start):
	accessed_arr = [start]
	print("Start at: " + str(start))
	current_pos = start
	l.append(0)
	l.append(max_cylinder)

	if(increasing_direction):
		l.sort()
		start_pos_index = -1
		#find current place in sorted list
		for i in range(0, len(l)):
			if(l[i] > current_pos):
				start_pos_index = i
				break
	else:
		l.sort(reverse=True)
		start_pos_index = -1
		#find current place in sorted list
		for i in range(0, len(l)):
			if(l[i] < current_pos):
				start_pos_index = i
				break

	#make list start at increasing one and jump back to smallest
	l_large = l[start_pos_index:]
	l_small = l[0:start_pos_index]
	l_sorted = l_large + l_small
	print(l_sorted)

	sum = abs(current_pos-l_sorted[0])
	print("Move to: " + str(l_sorted[0]))
	accessed_arr.append(l[0])
	for i in range(1, len(l_sorted)):
		print("Move to: " + str(l_sorted[i]))
		sum += abs(l_sorted[i] - l_sorted[i-1])
		accessed_arr.append(l[i])

	print("Total distance: " + str(sum))
	return accessed_arr




def clook(l, increasing_direction, start):
	accessed_arr = [start]
	print("Start at: " + str(start))
	current_pos = start

	if(increasing_direction):
		l.sort()
		start_pos_index = -1
		#find current place in sorted list
		for i in range(0, len(l)):
			if(l[i] > current_pos):
				start_pos_index = i
				break
	else:
		l.sort(reverse=True)
		start_pos_index = -1
		#find current place in sorted list
		for i in range(0, len(l)):
			if(l[i] < current_pos):
				start_pos_index = i
				break

	#make list start at increasing one and jump back to smallest
	l_large = l[start_pos_index:]
	l_small = l[0:start_pos_index]
	l_sorted = l_large + l_small

	sum = abs(current_pos-l_sorted[0])
	print("Move to: " + str(l_sorted[0]))
	accessed_arr.append(l[0])
	for i in range(1, len(l_sorted)):
		print("Move to: " + str(l_sorted[i]))
		sum += abs(l_sorted[i] - l_sorted[i-1])
		accessed_arr.append(l[i])

	print("Total distance: " + str(sum))
	return accessed_arr



#cscan()
#sstf()
#scan()
#fcfs()
#look()
#cscan()
#clook()






			





