import random, trie, time

chars="abcdefghijklmnopqrstuvwxyz"

DATA = []
for i in range(20000):
    DATA.append(''.join(random.choice(chars)
                for _ in range(random.randint(2, 16))))

DATASET = set(DATA)

DATATRIE = trie.Trie()
for d in DATA:
    DATATRIE.add(d)

def testList():
    for d in DATA:
        if d in DATA:
            x = 1
        else:
            x = 2
    return x

def testSet():
    for d in DATA:
        if d in DATASET:
            x = 1
        else:
            x = 2
    return x

def testTrie():
    for d in DATA:
        if DATATRIE.matches(d)[0]:
            x = 1
        else:
            x = 2

def timeit(function):
    start = time.time()
    function()
    end = time.time()
    return end-start

FUNCTIONS = (testList, testSet, testTrie)

RESULT = {}

for f in FUNCTIONS:
    print("Running", f.__name__,"...",)
    t = timeit(f)
    print(t)
    RESULT[f.__name__] = t

print(RESULT)
