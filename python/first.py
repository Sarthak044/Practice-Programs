# Simple Python program to print all permutations
# of a string that follow given constraint


def permute(str, l, r):

	# Check if current permutation is
	# valid
	if (l == r):
		if "AB" not in ''.join(str):
			print(''.join(str), end=" ")
		return

	# Recursively generate all permutation
	for i in range(l, r + 1):
		str[l], str[i] = str[i], str[l]
		permute(str, l + 1, r)
		str[l], str[i] = str[i], str[l]


# Driver Code
str = "ABC"
permute(list(str.), 0, len(str) - 1)

# mapping




