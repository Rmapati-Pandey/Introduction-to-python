def subarray(a):
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
	max_kadane = subarray(a)
	neg_a = [-1*x for x in a]
	max_neg_kadane = subarray(neg_a)
	max_wrap = -(sum(neg_a)-max_neg_kadane)

	res = max(max_wrap,max_kadane)
	return res if res != 0 else max_kadane

inarr= [int(item) for item in input().split(',')]
print(maxCircularSum(inarr))

