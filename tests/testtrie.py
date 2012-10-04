from trie import *
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def testAddOne(self):
        self.trie.add("abc")

        m = self.trie.matches("abc")
        self.assertEqual((1, 3), m)

        m = self.trie.matches("cab")
        self.assertEqual((0, 0), m)

        m = self.trie.matches("abd")
        self.assertEqual((0, 2), m)


    def testAddTwo(self):
        self.trie.add("abc")
        self.trie.add("abd")

        m = self.trie.matches("abc")
        self.assertEqual((1, 3), m)

        m = self.trie.matches("abd")
        self.assertEqual((1, 3), m)

        m = self.trie.matches("abe")
        self.assertEqual((0, 2), m)

    def testSuffixes(self):
        self.trie.add("abc")
        self.trie.add("abd")
        self.trie.add("abde")
        self.trie.add("abdefg")
        self.trie.add("abdefh")
        s = self.trie.getSuffixes("ab")
        expected = (2, set(("c", "d", "de", "defg", "defh")))
        self.assertEqual(expected, (s[0], set(s[1])))

        s = self.trie.getSuffixes("abd")
        expected = (3, set(("", "e", "efg", "efh")))
        self.assertEqual(expected, (s[0], set(s[1])))

        s = self.trie.getSuffixes("abdef")
        expected = (5, set(("g", "h")))
        self.assertEqual(expected, (s[0], set(s[1])))

        s = self.trie.getSuffixes("abc")
        self.assertEqual((3, [""]), s)

        s = self.trie.getSuffixes("bc")
        expected = (0, set(("abc", "abd", "abde", "abdefg", "abdefh")))
        self.assertEqual(expected, (s[0], set(s[1])))

if __name__ == "__main__":
    unittest.main()
