import math, queue
from collections import Counter

####### Problem 1 #######

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    # construct heap from frequencies, the initial items should be
    # the leaves of the final tree
    for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))
    
    while (p.qsize() > 1):
        
        # greedily remove the two nodes x and y with lowest frequency,
        x = p.get()
        y = p.get()
        
        # create a new node z with x and y as children.
        z = TreeNode(x, y, (x.data[0] + y.data[0], ""))

        # insert z into the priority queue (using an empty character "")
        p.put(z)
        
    # return root of the tree
    return p.get()

# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}):

    if code is None:
        code = {}

    #If it s a leaf, then that means it is part of the alphabet set.

    if node.left is None and node.right is None:
        frequency, character = node.data
        code[character] = prefix or "0"
        return code

    #Recurse further down the tree.

    if node.left: #Add a 0 for left children.
        get_code(node.left, prefix + "0", code)
    
    if node.right: #Add a 1 for right children.
        get_code(node.right, prefix + "1", code)

    return code


# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
    #Base Case

    if not f:
        return 0

    # The total number of distinct alphabet 
    alphabets = len(f)

    #The bits required for a fixed length encoding is the log base 2 of the distinct alphabets with a ceiling.

    fixed_bit_size = math.ceil(math.log2(alphabets))

    total_symbols = sum(f.values())

    cost = fixed_bit_size * (total_symbols)
          
    return cost

        

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    if not f:
        return 0 
    
    cost=0
    
    for character, frequency in f.items():

        #To get the cost multiply the frequency by the bit size that was obtained in the coding.

        cost+= frequency * (len(C[character]))

    return cost
 

files = ["f1.txt", "alice29.txt", "asyoulik.txt", "grammar.lsp", "fields.c"]

for file in files:
    print(file)
    f = get_frequencies(file)

    fixed_cost = fixed_length_cost(f)
    print("Fixed-length cost:  %d" % fixed_cost)

    T = make_huffman_tree(f)
    C = get_code(T)
    huff_cost = huffman_cost(C, f)
    print("Huffman cost:  %d" % huff_cost)

    ratio = (huff_cost / fixed_cost) if fixed_cost else float("nan")
    print("Huffman vs Fixed-length:  %.4f" % ratio)
    print("---------------------")



