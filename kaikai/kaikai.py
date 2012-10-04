import collections

from .trie import Trie

class Vocab(object):

    def __init__(self):
        self.words = Trie()
        self.suffixes = collections.defaultdict(set)
        self.stems = dict()
        

    def update(self, words):
        for w in words:
            self.words.add(w)
        
        for w in self.words.words():
            index,suffixes = self.words.getSuffixes(w)
            for s in suffixes:
                if s:
                    self.suffixes[s].add(w)
        self.build()

    def build(self): 
        self.stems.clear()
        ignore = set()
        for w in self.words.words():
            if w in ignore: continue
            index, suffixes = self.words.getSuffixes(w)
            if w.isupper(): # ABC, ABCs, ABCi -> ABC
                if all(s.islower() for s in suffixes):
                    for s in suffixes:
                        iw = w + s
                        ignore.add(iw)
                        self.stems[iw] = w
            
            for s in suffixes: # 
                prefixes = self.suffixes[s]
                if len(prefixes) > 1:
                    iw = w + s
                    ignore.add(iw)
                    self.stems[iw] = w
            self.stems[w] = w
