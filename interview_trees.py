
# recursive solution to searching a binary tree
def find(r, n):
	if not r:
		return None
	elif r.data < n:
		return find(r.right, n)
	elif r.data > n:
		return find(r.left, n)
	else:
		return r

# using a while loop to search a binary tree
def find(r, n):
	while r and r.data != n:
		if r.data < n:
			r = r.right
		else:
			r = r.left
	return r

