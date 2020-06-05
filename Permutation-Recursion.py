def perm(array):
    result = []
    permutation = []
    perHleper(array, permutation, result)
    print("----")
    print(result)


def perHleper(array, permutation, result):
    if len(array) == 0:
        result.append(permutation)
    else:
        for i in range(len(array)):
            # remove current index and form new array
            newArray = array[:i] + array[i + 1:]
            # removed item(Existingitem) + existing item
            newpermutation = permutation + [array[i]]
            # print("new array {0}, permut {1}".format(newArray,newpermutation))

            # recusrion
            perHleper(newArray, newpermutation, result)


perm(['a', 'b', 'c'])
perm([1, 2, 3])

# time complexity : O(n*n!)
# space complexity : O(n*n!)