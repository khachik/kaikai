import feedparser

import reader
from kaikai import Vocab

def pp(*args):
    import pprint
    out = open(1, 'w', encoding="utf-8", closefd=False)
    pprint.pprint(*args, stream=out)

def pr(*args):
    out = open(1, 'w', encoding="utf-8", closefd=False)
    print(*args, file=out)

FEEDLIST = [
    "../newnews/data/tert.am.xml",
    "../newnews/data/news.am.xml"
    "http://www.news.am/arm/rss/",
    "http://www.tert.am/rss/?language=am"
]

def readarticles(feedlist):
    articletitles = set()

    for feed in feedlist:
        f=feedparser.parse(feed)
        for e in f.entries:
            if e.title in articletitles: continue
            articletitles.add(e.title)
            yield e.title + " " + e.description

if __name__ == "__main__":
    vocab = Vocab()
    for content in readarticles(FEEDLIST):
        words = reader.getWords(reader.cleanHTML(content))
        vocab.update(words)
    pp(vocab.words)
    pp(vocab.suffixes)
    pp(vocab.stems)
