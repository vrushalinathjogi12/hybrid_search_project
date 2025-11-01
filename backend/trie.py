# # trie.py
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end = False
#         self.frequency = 0

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word, frequency=1):
#         node = self.root
#         word = word.lower()
#         for ch in word:
#             if ch not in node.children:
#                 node.children[ch] = TrieNode()
#             node = node.children[ch]
#         node.is_end = True
#         node.frequency = frequency

#     def _collect(self, node, prefix, out):
#         if node.is_end:
#             out.append((prefix, node.frequency))
#         for ch, child in node.children.items():
#             self._collect(child, prefix + ch, out)

#     def starts_with(self, prefix):
#         """Return list of (word, freq) starting with prefix."""
#         prefix = prefix.lower()
#         node = self.root
#         for ch in prefix:
#             if ch not in node.children:
#                 return []
#             node = node.children[ch]
#         out = []
#         self._collect(node, prefix, out)
#         return out


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        result = []
        self._dfs(node, prefix, result)
        return result

    def _dfs(self, node, prefix, result):
        if node.is_end:
            result.append(prefix)
        for char, child in node.children.items():
            self._dfs(child, prefix + char, result)
