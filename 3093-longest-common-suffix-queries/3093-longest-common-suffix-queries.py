class TrieNode:

    def __init__(self):

        self.children = {}

        self.index = -1


class Solution:

    def stringIndices(self, wordsContainer, wordsQuery):

        root = TrieNode()

        best = min(range(len(wordsContainer)),
                   key=lambda i: (len(wordsContainer[i]), i))

        # BUILD TRIE
        for i, word in enumerate(wordsContainer):

            rev = word[::-1]

            node = root

            if node.index == -1 or \
               len(word) < len(wordsContainer[node.index]) or \
               (len(word) == len(wordsContainer[node.index]) and i < node.index):

                node.index = i

            for ch in rev:

                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                if node.index == -1 or \
                   len(word) < len(wordsContainer[node.index]) or \
                   (len(word) == len(wordsContainer[node.index]) and i < node.index):

                    node.index = i

        answer = []

        # QUERY
        for word in wordsQuery:

            rev = word[::-1]

            node = root

            for ch in rev:

                if ch not in node.children:
                    break

                node = node.children[ch]

            answer.append(node.index)

        return answer