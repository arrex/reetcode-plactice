from typing import List


class Solution1:
    """
    Intuition:
        We keep track of the index up to which all prefixes match and
        traverse all strings in the array to increment that index.

    Runtime:
        Let n be the number of strings in strs and s be the len of the
        shortest string in strs.

        Our runtime is O(n * s).

    Memory:
        O(1).
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""

        ix = 0

        while True:
            if ix == len(strs[0]):
                break

            curr = strs[0][ix]
            ok = True

            for s in strs:
                # if we reached the end of str s or if there is mismatch
                if ix == len(s) or s[ix] != curr:
                    ok = False
                    break

            if not ok:
                break

            ix += 1

        return strs[0][:ix]


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr:
                curr[c] = {}

            curr = curr[c]

        # Mark end of word
        curr["#"] = {}

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr:
                return False

            curr = curr[c]

        return "#" in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr:
                return False

            curr = curr[c]

        return True


class Solution2:
    """
    Intuition:
        For prefix matching, we have tries. We can use it to insert every
        string given to us and find the longest prefix by checking at each
        iteration the number of keys stored in the current level of the trie.

        Note that this solution is a bit less optimal, but an interesting
        alternative.

    Runtime:
        O(N * k) to insert all the strings where N is the number of strings and
        k is the length of the longest string.

        O(s) to find the longest prefix where s is the length of the shortest
        string in the array.

        Overall runtime bounded by insertion i.e. O(N * k) which is slightly
        less optimal than Solution 1.

    Memory:
        The trie holds every character given to us in the input string array.
        Thus, the memory complexity is O(N * k) where N is the number of strings
        and k is the length of the longest string. This is also worse than the
        memory complexity of Solution 1.
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()

        for s in strs:
            trie.insert(s)

        curr = trie.root
        prefix = ""

        while len(curr) == 1:
            # grab first elmt
            key = next(iter(curr.keys()))

            if key == "#":
                break

            prefix += key
            curr = curr[key]

        return prefix
