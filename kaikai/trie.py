import collections

class Trie(object):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.children = collections.defaultdict(Trie)

    def add(self, word, index=0):
        if index == len(word):
            self.count += 1
            return
        self.children[word[index]].add(word, index+1)

    def matches(self, item, index=0):
        if index == len(item):
            return self.count, index
        elif item[index] in self.children:
            return self.children[item[index]].matches(item, index+1)
        else:
            return 0, index
              
    def words(self):
        res = []
        if self.count > 0:
            res.append("")
        for l,t in self.children.items():
            for w in t.words():
                res.append(l + w)
        return res

    def getSuffixes(self, item, index=0):
        if index == len(item) or item[index] not in self.children:
            return index, self.words()
        else:
            return self.children[item[index]].getSuffixes(item, index+1)

    def __repr__(self):
        res = ""
        words = self.words()
        for w in words:
            res += w + "\n"
            indent = " " * len(w)
            index, suffixes = self.getSuffixes(w)
            for s in suffixes:
                if s:
                    res += indent + s + "\n"
        return res

    __str__ = __repr__
