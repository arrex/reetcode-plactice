from typing import List


class TrieNode:
    def __init__(self, optWord, optIx):
        self.optWord = optWord
        self.optIx = optIx
        self.children = {}


class Solution:
    """
    Intuition:
        Immediately with suffix matching we think of using a Trie. This problem
        does involve a trie to speed up suffix lookups, but with some added
        flavour.

        In a regular trie, we traverse the children in search of a prefix. Since
        we are dealing with suffixes, we simply insert the words in reverse order
        for the same effect. We also need to track the optimal match at each node
        since we can encounter suffixes that don't match with any word we inserted.

    Runtime:
        Inserting a word takes at most O(k) with k being the length of the longest
        word. With n words, this becomes O(n * k).

        Querying a suffix takes O(l) where l being the length of the longest suffix.
        With m queries, this becomes O(m * l).

        Overall, our runtime complexity is O(n * k + m * l).

    Memory:
        We have n words with at most k chars each. This means our trie takes up
        at most O(n * k) space.
    """

    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trieRoot = TrieNode(wordsContainer[0], 0)

        for ix, word in enumerate(wordsContainer):
            # insert into trie
            curr = trieRoot

            # adjust root if found shorter word
            if len(word) < len(curr.optWord):
                curr.optWord = word
                curr.optIx = ix

            for j in range(len(word) - 1, -1, -1):
                c = word[j]

                if c not in curr.children:
                    curr.children[c] = TrieNode(word, ix)

                curr = curr.children[c]

                # if found a better match
                if len(word) < len(curr.optWord):
                    curr.optWord = word
                    curr.optIx = ix

        res = []
        for query in wordsQuery:
            curr = trieRoot
            ix = curr.optIx

            for c in query[::-1]:
                if c not in curr.children:
                    ix = curr.optIx
                    break

                curr = curr.children[c]
                ix = curr.optIx

            res.append(ix)

        return res
