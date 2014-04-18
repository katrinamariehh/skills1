
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

# searching a binary tree that is not a binary search tree
# depth-first search--you go all the way down, then come back up
def search (r, n):
	if not r:
		return False
	if r.data == n:
		return True
	# this
	return search(r.left) or search(r.right)

	# or this to return the data 
	if not r:
		return None
	if r.data == n:
		return r.data
	left = search(r.left, n)
	if left:
		return left
	right = search(r.right, nelse:
	if right:
		return search (r.left, n)

# breadth-first searching
# if we have a queue--we can put all of the things we need to search
# in the queue, we just have to go to the end of the queue
def search_bfs(r, n):
	# we want a queue
	q = [r]
	while len(q) > 0:
		node = q.pop(0)
		if node.data == n:
			return node
		if node.left:
			q.append(node.right)
		if node.right:
			q.append(node.left)