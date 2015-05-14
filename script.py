import numpy as np

_map = [1,1,0,1,0]

def normalize(pos):
	total = np.sum(pos)
	pos[:] = pos/total

def update(pos,z,_map,pCorrect = 0.8):
	pFail = 1 - pCorrect
	for idx,val in enumerate(_map):
		if val == z:
			pos[idx] *= pCorrect
		else:
			pos[idx] *= pFail 
	normalize(pos)

def predict(pos,move,kernel=[0.1,0.8,0.1]):
	result = np.zeros(len(pos))
	offset = move - 1
	for i in range(len(pos)):
		for k in range(len(kernel)):
			index = (i - k - offset) % len(pos)
			result[i] += pos[index] * kernel[k]
	pos[:] = result[:]

def cycle():
	pos_belief = np.ones(5)/5
	z = [1,0,1,1,0]
	move = [1,1,1,1,1]
	for i in range(len(move)):
		update(pos_belief,z[i],_map)
		predict(pos_belief,move[i])
	print pos_belief