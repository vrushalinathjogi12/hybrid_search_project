# hybrid_dictionary.py
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.frequency = 0
        self.top_suggestions = []

class HybridDictionary:
    def __init__(self):
        self.exact_map = {}
        self.root = TrieNode()

    def insert(self, word: str, freq: int = 1):
        # Insert in hash map
        self.exact_map[word] = freq

        # Insert in trie
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            self._update_suggestions(node, word, freq)

        node.is_end = True
        node.frequency = freq

    def _update_suggestions(self, node, word, freq):
        # update or add word to suggestion list
        for i, (w, f) in enumerate(node.top_suggestions):
            if w == word:
                node.top_suggestions[i] = (word, freq)
                break
        else:
            node.top_suggestions.append((word, freq))
        node.top_suggestions.sort(key=lambda x: x[1], reverse=True)
        node.top_suggestions = node.top_suggestions[:5]

    def exact_lookup(self, word):
        return self.exact_map.get(word, None)

    def prefix_lookup(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        return [w for (w, f) in node.top_suggestions]
