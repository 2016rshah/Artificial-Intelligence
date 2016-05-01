def findSwapPos(n):
	'''
	Find sequence of adjacent swap positions that generate permutations of [0..n-1]
	returns a list with swap position to get next permuation
	'''
	if n == 1: return []
	if n == 2: return [0]
	fs = findSwapPos(n-1)
	pfx = [[i for i in range(0, n-1)], [i for i in reversed(range(0, n-1))]]
	fsr = [pfx[i%2] + [fs[i] + (i%2)] for i in range(len(fs))]
	res = []
	for fsrsub in fsr:
		for elem in fsrsub:
			res.append(elem)
	return res
