
#Function that returns the minimum
# number greater than Maximum of the
# array that cannot be formed using the
# elements of the array

def findNumber(arr, n):

	arr = sorted(arr)

	
	Max = arr[n - 1]

	
	table = [10**9 for i in range((2 * Max) + 1)]

	table[0] = 0

	ans = -1

	
	for i in range(1, 2 * Max + 1):
		for j in range(n):
			if (arr[j] <= i):
				res = table[i - arr[j]]
				if (res != 10**9 and res + 1 < table[i]):
					table[i] = res + 1
			
		
		if (i > arr[n - 1] and table[i] == 10**9):
			ans = i
			break
		
	return ans


inarr= [int(item) for item in input().split(' ')]
n = len(inarr)

print(findNumber(inarr, n))

