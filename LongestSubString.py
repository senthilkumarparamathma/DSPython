def longestSubString(word):
    strLength = len(word)
    # print("length:{0}".format(strLength))
    subStringLength = 1
    currentSubStringLength = 1
    subDic = {}
    subDic[word[0]] = True
    for i in range(1, strLength):
        # print("--{0},{1}, {2} \n".format(word[i],subStringLength, i))
        if word[i] in subDic:

            currentSubStringLength = max(currentSubStringLength, subStringLength)
            # print("current ,{0} \n".format(currentSubStringLength))
            subStringLength = 1
            subDic = {}
            subDic[word[i]] = True
        else:
            subDic[word[i]] = True
            subStringLength += 1
            currentSubStringLength = max(currentSubStringLength, subStringLength)

    print(currentSubStringLength)


longestSubString('ABDEFGABEF')