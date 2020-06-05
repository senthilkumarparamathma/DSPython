def twoNumberSum(array, targetSum):
	array.sort()
	leftIndex = 0
	rightIndex = len(array) -1
	while leftIndex < rightIndex :
		totalSum = array[leftIndex] + array[rightIndex]
		if totalSum == targetSum:
			return sorted([array[rightIndex],array[leftIndex]])
		elif totalSum < targetSum:
			leftIndex +=1
		elif totalSum > targetSum:
			rightIndex -=1
	return []

if __name__ == "__main__":
	result = twoNumberSum([4,2,5,6,1,8,3,7],13)
	print(result)