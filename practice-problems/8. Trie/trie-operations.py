# https://www.geeksforgeeks.org/trie-insert-and-search/
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        p = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if p.children[index] == None:
                p.children[index] = TrieNode()
            p = p.children[index]
        p.isEndWord = True

    def search(self, key):
        rootp = self.root
        for i in range(len(key)):
            index = ord(key[i]) - ord('a')
            if rootp.children[index] == None:
                return False
            rootp = rootp.children[index]
        if not rootp.isEndWord:
            return False
        return True

    def delete(self, key):
        rootp = self.root
        for i in range(len(key)):
            index = ord(key[i]) - ord('a')
            if rootp.children[index] == None:
                return "key does not exist in trie"
            rootp = rootp.children[index]
        if rootp.isEndWord:
            for i in rootp.children:
                if i != None:
                    rootp.isEndWord = False
                    return "deleted"
            p = self.root
            for i in range(len(key)):
                index = ord(key[i]) - ord('a')
                print(index)
                tmp = p.children[index]
                p.children[index] = None
                p = tmp
            rootp.isEndWord = False
            return "Deleted"
        else:
            return "key does not exist!"


#    def traversal(self,[]st,level):

#        if self.root


def main():
    t = Trie()
    words = ["geeks", "skp", "shani", "himm"]
    keys = ["hi", "skp", "how", "geeks"]
    for i in words:
        t.insert(i)
    for i in keys:
        print(t.search(i))
    print(t.delete("him"))
    print(t.search("him"))


if __name__ == '__main__':
    main()
