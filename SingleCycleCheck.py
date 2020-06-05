def hasSingleCyle(array):
  visitedItem = 0
  currentIndex = 0
  while visitedItem < len(array):
    if visitedItem > 0 and currentIndex == 0:
      return False
    nextMoveIndex = getIndex(currentIndex,array)
    visitedItem += 1
    currentIndex = nextMoveIndex
  return (currentIndex == 0)


def getIndex(currentIndex, array):
  nextMove = array[currentIndex]
  return (currentIndex + nextMove ) % len(array)

result = hasSingleCyle([2,3,1,-4,-4,2])
#result = hasSingleCyle([1,-1,1,-1])
print(result)