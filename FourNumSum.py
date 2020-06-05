def fourNumberSum(array, targetSum):
    hashTable = {}  # key: [[]]
    resultArray = []
    for n in range(len(array)):
        for m in range(n + 1, len(array)):
            result = array[n] + array[m]
            if result not in hashTable:
                hashTable[result] = [[array[n], array[m]]]
            else:
                # earlierValue  = hashTable[result]
                hashTable[result].append([array[n], array[m]])

                # for k in range(0,n):

    print("---")
    print(hashTable)
    print("---")

    for value in hashTable:
        diff = targetSum - value
        if diff in hashTable and value != diff:
            for diffVal in hashTable[diff]:
                for currentVal in hashTable[value]:
                    notDuplicate = True
                    for dval in diffVal:
                        if dval in currentVal:
                            notDuplicate = False

                    if notDuplicate:
                        f1 = diffVal + currentVal
                        f1.sort()
                        if f1 not in resultArray:
                            resultArray.append(f1)

    return resultArray


result = fourNumberSum([7, 6, 4, -1, 1, 2], 16)
print(result)
