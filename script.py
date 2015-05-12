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
	for _ in range(move):
		for i in range(-1,len(pos)-1):
			result[i+1] = pos[i] * kernel[1] + pos[i-1] * kernel[0] + pos[i+1] * kernel[2]
		pos[:] = result[:]

