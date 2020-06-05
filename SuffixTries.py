class SuffixTrie:
    def __init__(self):
        self.root = {}
        self.endnode = "*"

    def construct(self, string):
        for i in range(len(string)):
            self.helperConstructer(i, string)

    def helperConstructer(self, index, string):
        node = self.root
        for j in range(index, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endnode] = True

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return True

    def suffixcontains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endnode in node


t = SuffixTrie()
t.construct("babc")
print(t.contains("abc"))
print(t.suffixcontains("abc"))

