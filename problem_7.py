"""
Project 3: Problems vs Algorithms
Problem 7. HTTP Router using a Trie

In addition to a path, we need to know which function will handle the http request.
We will use a string that we can print out to ensure we got the right handler.

A Trie with a single path entry of: "/about/me" would look like:
   (root, None) -> ("about", None) -> ("me", "about me handler")

insert() in RouteTrie class takes O(n) time, where n is the size of path, and
        O(1) space, excluding the space for output result.

find() in RouteTrie class takes O(n) time, where n is the size of path, and
        O(1) space.

add_handler() in Route class takes O(n) time, where n is the length of input
path. It takes O(n) space for a list of tokens along the path.

lookup() in Route class takes O(n) time, where n is the length of input path.
It takes O(n) space for a list of tokens.
"""
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children, plus a handler
        self.children = {}
        self.handler = handler
        self.p = '/'  # prefix for debugging

    def insert(self, token):
        # Insert the token if it is not in children
        if token not in self.children:
            self.children[token] = RouteTrieNode()

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path
        # or home page node
        self.root = RouteTrieNode(root_handler)

    def insert(self, path, handler):
        # Assign the handler to the leaf node of this path.
        # Input path is a list of tokens.
        # Time: O(n), where n is the size of path
        # Space: O(1), excluding the space for output result
        c = self.root
        p = c.p  # prefix for debugging
        for token in path:  # A token is the part between '/'s in a URL.
            c.insert(token)
            c = c.children[token]
            p = p + token + '/'
            c.p = p
        # c is the leaf node of this path.
        c.handler = handler

    def find(self, path=[]):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        # Input path is a list of tokens.
        # Time: O(n), where n is the size of path
        # Space: O(1)
        c = self.root
        if len(path) == 0:
            return c.handler  # root handler
        for token in path:
            #print(f"find path={path} token={token} c.children={c.children} p={c.p}")
            if token in c.children:
                c = c.children[token]
            else:
                return None
        return c.handler

class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        self.trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, pathStr, handler):
        # Add a handler for a path
        # Input pathStr is a string
        # Time: O(n), where n is the length of input pathStr
        # Space: O(n) for nodes a list of tokens along the path
        if pathStr == None or pathStr == '' or pathStr == '/':
            return
        path = self.split_path(pathStr) # path is a list of tokens
        
        if path == None: # syntax error in pathStr
            return
        self.trie.insert(path, handler)

    def lookup(self, pathStr=''):
        # lookup path (by parts) and return the associated handler
        # return self.not_found_handler if it is not found
        # A trailing slash is processed.
        # e.g. /about and /about/ both return the /about handler
        # Input pathStr is a string.
        # Time: O(n), where n is the length of input pathStr
        # Space: O(n) for a list of tokens along the path
        if pathStr == None or pathStr == '' or pathStr == '/':
            return self.trie.root.handler
        path = self.split_path(pathStr) # path is a list of tokens
        
        if path == None: # syntax error in pathStr
            return self.not_found_handler
        handler = self.trie.find(path)
        if handler != None:
            return handler
        else:
            return self.not_found_handler

    def split_path(self, pathStr):
        # to split the path into tokens for both add_handler and loopup functions
        # Input pathStr is a string.
        # pathStr begins with '/'. Otherwise returns None.
        # pathStr is not None, '', or '/' because these are filtered by the caller.
        # A trailing slash is processed.
        # Returns a list of tokens, and a token is the part between two '/'s
        # Returns None for syntax error
        if len(pathStr) < 2:
            return None
        if pathStr[0] != '/':
            return None
        if pathStr[-1] == '/':
            pathStr = pathStr[:-1]
        path = pathStr[1:].split('/')
        #print(path)
        for token in path:
            if token == '':
                return None
        return path

router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler'
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler'
print(router.lookup("/home/about/me")) # should print 'not found handler'
router.add_handler("/home/about/me", "about me handler") # add a route
print(router.lookup("/home/about/me")) # should print 'about me handler'
print(router.lookup("home/about/me")) # should print 'not found handler'
print(router.lookup()) # should print 'root handler'
print(router.lookup(None)) # should print 'root handler'
print(router.lookup("/home/about///me/")) # should print 'not found handler'
router.add_handler("/google", "google handler") # add a route
router.add_handler("/google/email", "google email handler") # add a route
router.add_handler("/google/maps", "google maps handler") # add a route
print(router.lookup("/google")) # should print 'google handler'
print(router.lookup("/google/yy")) # should print 'not found handler'
print(router.lookup("/google/email")) # should print 'google email handler'
print(router.lookup("/google/maps")) # should print 'google maps handler'
print(router.lookup("/google/maps/")) # should print 'google maps handler'

def test_func(s1, s2):
    if s1 == s2:
        print("Pass")
    else:
        print("Fail")

test_func(router.lookup("/"), 'root handler')
test_func(router.lookup("/home"), 'not found handler')
test_func(router.lookup("/home/about"), 'about handler')
test_func(router.lookup("/home/about/"), 'about handler')
test_func(router.lookup("/home/about/me"), 'about me handler')
test_func(router.lookup("home/about/me"), 'not found handler')
test_func(router.lookup(), 'root handler')
test_func(router.lookup(None), 'root handler')
test_func(router.lookup("/home/about///me/"), 'not found handler')
test_func(router.lookup("/google"), 'google handler')
test_func(router.lookup("/google/yy"), 'not found handler')
test_func(router.lookup("/google/email"), 'google email handler')
test_func(router.lookup("/google/maps"), 'google maps handler')
test_func(router.lookup("/google/maps/"), 'google maps handler')

"""
Output:

root handler
not found handler
about handler
about handler
not found handler
about me handler
not found handler
root handler
root handler
not found handler
google handler
not found handler
google email handler
google maps handler
google maps handler
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
