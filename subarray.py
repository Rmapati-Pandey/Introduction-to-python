def kadane(a):
	Max = a[0]
	temp = Max
	for i in range(1,len(a)):
		temp += a[i]
		if temp < a[i]:
			temp = a[i]
		Max = max(Max,temp)
	return Max

def maxCircularSum(a):

	n = len(a)

