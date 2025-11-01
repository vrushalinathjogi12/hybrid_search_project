# # hashmap.py
# class HashMap:
#     def __init__(self):
#         self.map = {}  # key -> frequency

#     def insert(self, key, value):
#         self.map[key.lower()] = int(value)

#     def get(self, key):
#         return self.map.get(key.lower(), None)

#     def search_prefix(self, prefix):
#         """Return list of (word, freq) whose key starts with prefix."""
#         prefix = prefix.lower()
#         results = []
#         for k, v in self.map.items():
#             if k.startswith(prefix):
#                 results.append((k, v))
#         return results

#     def size(self):
#         return len(self.map)

class HashMap:
    def __init__(self):
        self.data = {}

    def add(self, key, value):
        self.data[key] = value

    def exists(self, key):
        return key in self.data
