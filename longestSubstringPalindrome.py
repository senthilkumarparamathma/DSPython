#brute force -
# Time Complexity : O(n^3) . --> 2 for loop , 1 reverse stting

def longestSubStribng(string):
  for outerIndex in range(len(string)):
    #print(string[outerIndex])
    for innerIndex in range(outerIndex, len(string)):
      temp = string[outerIndex:innerIndex+1]
      if len(temp)> 1 and temp == temp[::-1]:
        print("result: {0}".format(temp))

print("---")
longestSubStribng("geeksskeeg")


#todo DP


def longestSubStribngDP(string):
    n = len(string)
    table = [[False for x in range(n)] for y in range(n)]

    # step 1 - 0 * 0 , 1*1 , .. mark as True
    for i in range(n):
        table[i][i] = True

    # print(table)

    # step 2 - check palindrome for 2 digit
    for i in range(n - 1):
        if string[i] == string[i + 1]:
            table[i][i + 1] = True

    # print(table)

    longestString = ''
    longestStringLength = 0
    # step 3 - digit 3 & above
    i = 3
    while i <= n:
        # print(" i -= {0}".format(i))
        for j in range(i - 1):
            # print(" j -= {0}".format(j))
            x = j
            y = i - 1  # make index as less than 1
            if string[x] == string[y] and table[x + 1][y - 1]:
                # print("----yes {0}".format(string[x:y+1]))
                table[x][y] = True
                palindromeString = string[x:y + 1]
                if longestStringLength < len(palindromeString):
                    longestStringLength = len(palindromeString)
                    longestString = palindromeString
        i += 1

    print(longestString)
    print(longestStringLength)
    # print(table)


longestSubStribngDP("forgeeksskeegfor")
