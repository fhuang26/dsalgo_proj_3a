"""
Project 3: Problems vs Algorithms
Problem 5. Autocomplete with Tries

We build the trie from a set of words, and then support autocompletion
by using the trie and suffix calucation.

suffixes() in TrieNode class takes O(n) time, where n is the number of nodes
in the subtree. It takes O(n) space for the number of nodes and suffixes in
the subtree.

insert() in Trie class takes O(n) time, where n is the word length. It takes
O(n) space for nodes of chars in the word.

find() in Trie class takes O(n) time, where n is the word length, and
O(1) space.

"""
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
        self.p = ''  # prefix for debugging
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
    
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        # Time: O(n), where n is the number of nodes in the subtree.
        # Space: O(n) for the number of nodes and suffixes in the subtree.
        a = []
        if self.is_word and suffix != '':
            a = [suffix]
        for h in self.children:
            w = suffix + h
            tn = self.children[h]
            a.extend(tn.suffixes(w))
        return a
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        # Time: O(n), where n is the word length
        # Space: O(n) for nodes of chars in the word
        c = self.root  # current node
        p = c.p
        for h in word:
            c.insert(h)
            c = c.children[h]
            p = p + h
            c.p = p
        c.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        # Time: O(n), where n is the word length
        # Space: O(1)
        c = self.root
        for h in prefix:
            #print(f"find p={prefix} h={h} c.children={c.children} p={c.p} is_word={c.is_word}")
            if h in c.children:
                c = c.children[h]
            else:
                return None
        #print(f"find p={prefix} h={h} c.children={c.children} p={c.p} is_word={c.is_word}")
        return c

# to build the trie
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "trip", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
    #c = MyTrie.find(word)
    #print(f"w={word} find(w)={c} is_word={c.is_word} p={c.p}")

def f(prefix=''):
    if prefix == None:
        return None
    suffixes = []
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode != None:
            suffixes = prefixNode.suffixes()
        #if prefixNode:
        #    print('\n'.join(prefixNode.suffixes()))
        #else:
        #    print(prefix + " not found")
    return suffixes

def test_func(sf1, sf2):
    if sf1 == sf2:
        print("Pass")
    else:
        print("Fail")
test_func(f('a'), ['nt', 'nthology', 'ntagonist', 'ntonym'])
test_func(f('an'), ['t', 'thology', 'tagonist', 'tonym'])
test_func(f('ant'), ['hology', 'agonist', 'onym'])
test_func(f('anton'), ['ym'])
test_func(f(''), [])
test_func(f(None), None)
test_func(f('f'), ['un', 'unction', 'actory'])
test_func(f('fu'), ['n', 'nction'])
test_func(f('fun'), ['ction'])
test_func(f('function'), [])
test_func(f('xx'), [])
test_func(f('t'), ['rie', 'rigger', 'rigonometry', 'rip', 'ripod'])
test_func(f('tr'), ['ie', 'igger', 'igonometry', 'ip', 'ipod'])
test_func(f('tri'), ['e', 'gger', 'gonometry', 'p', 'pod'])
test_func(f('trie'), [])
test_func(f('trig'), ['ger', 'onometry'])
test_func(f('trigg'), ['er'])
test_func(f('trigo'), ['nometry'])
test_func(f('trigono'), ['metry'])
test_func(f('trip'), ['od'])
test_func(f('tripo'), ['d'])
test_func(f('tripod'), [])
test_func(f('fa'), ['ctory'])
test_func(f('fac'), ['tory'])
test_func(f('fact'), ['ory'])
test_func(f('facto'), ['ry'])
test_func(f('factor'), ['y'])
test_func(f('factory'), [])
#interact(f,prefix='')

"""
Output:

Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
"""