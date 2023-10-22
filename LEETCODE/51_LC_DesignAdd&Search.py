class TrieNode:
  def __init__(self):
    self.children: Dict[str, TrieNode] = {}
    self.iW = False


class WordDictionary:
  def __init__(self):
    self.root = TrieNode()

  def addWord(self, word):
    node: TrieNode = self.root
    for c in word:
      node = node.children.setdefault(c, TrieNode())
    node.iW = True

  def search(self, word):
    return self.fs(word, 0, self.root)

  def fs(self, word, s, node):
    if s == len(word):
      return node.iW
    if word[s] != '.':
      child: TrieNode = node.children.get(word[s], None)
      return self.fs(word, s + 1, child) if child else False
    return any(self.fs(word, s + 1, child) for child in node.children.values())
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
"""
Problem Link:
https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""
