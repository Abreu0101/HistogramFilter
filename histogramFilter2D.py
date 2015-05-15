import numpy as np

# 1 represent a door
# 0 represent a wall
_map = np.array([[1,0,0,1],
				 [0,0,0,0],
				 [0,1,0,0],
				 [0,0,1,0]])

#position belief
pos_belief = np.ones(_map.shape)/np.sum(_map)

#Normalize distribution
def normalize(pob_distribution):
	pob_distribution = pob_distribution / np.sum(pob_distribution)

#Get a Measure
def update(pos_belief,z,pCorrect=0.8):
	result = np.zeros(pos_belief.shape)
	for i in range(len(pos_belief)):
		for j in range(len(pos_belief[i])):
			if _map[i][j] == z:
				result[i][j] = pos_belief[i][j] * pCorrect
			else:
				result[i][j] = pos_belief[i][j] * (1-pCorrect)
	normalize(result)
	pos_belief[:] = result[:]

#Move
#kernel is the error by 1 position (Assumption)
def predict(pos_belief,move,kernel=[0.1,0.8,0.1]):
	result = np.zeros(pos_belief.shape)
	direction, step = move
	directionHead = (direction == 1)  # (0) up ** (1) down
	offset = (1 - directionHead) * (step - 1) + (directionHead) * (-step - 1) 
	for i in range(len(pos_belief)):
		for j in range(len(pos_belief[i])):
			for k in range(len(kernel)):
				index = (1 - directionHead) * (offset + k + i) % len(pos_belief) + directionHead * ((offset + k + j) % len(pos_belief[i]))
				result[i][j] += ((1 - directionHead) * pos_belief[index][j]  + directionHead * pos_belief[i][index]) * kernel[k]
	pos_belief[:] = result[:]

def cycle():
	#Measurements
	Z = [1,0,0,1]
	#Moves command - [0,+Up/-Down]  [1,-Left/+Right]
	M = [[0,-1],[0,-1],[1,-1],[1,-1]]
	for i in range(len(Z)):
		update(pos_belief,Z[i])
		predict(pos_belief,M[i])
	print pos_belief
