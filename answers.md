# CMPS 6610 Problem Set 04
## Answers

**Name:** Arjun Dadhwal


Place all written answers from `problemset-04.md` here for easier grading.




- **1d.**

File | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length
----------------------------------------------------------------------
f1.txt    |    1340                 |        826        | 826/1340 = 0.6164
alice29.txt    |   1039367                  |    676374            | 676374/1039367 = 0.6508
asyoulik.txt    |  876253                   |    606448           | 606448/876253 = 0.6921
grammar.lsp    |     26047                |      17356          | 17356/26047 = 0.6663
fields.c    |           78050          |     56206           | 56206/78050 = 0.7201



- A trend that I can observe is that the ratio of the total cost obtained by the Huffman encoding vs Fixed-length encoding, is always less than 1, with Huffman encoding always being cheaper, and the ratio seems to be in the 0.6-0.7 ratio, regardless of size, though for this I'll have to observe more samples and that too of hopefully diverse sizes to get a more accurate inference.

- The reason for this reason is that Fixed length uses B = ceiling of log base 2 of k bits per character for k distinct symbols whereas Huffman assigns shorter codes to the more frequent symbols.

-- For any source with empirical frequencies, the average Huffman length Lavg would obey H <= Lavg < H + 1, where H is the Shannon entropy (bits/char). For English text and k ~= 70-100, B is around 7 bits, and the typical H is around 4.5-5.0, which gives a ratio Lavg/B ~= 0.6-0.7 as was observed.

-- More sekewd frequencies would lead to a more smaller ratio and for more uniform frequencies, the ratio will approach 1.

- **e.**

- Let k = |sigma| be the number of distinct symbols.
- If all k symbols occur equally often, the Huffman will builds an almost balanced tree and will only use two code lengths:
1. the short length b = floor of log2 of k 
2. the long length b + 1.

- (Exactly 2^(b+1) - k symbols get length b; the rest get length b + 1)

- Expected bits per character

- Lavg = ( (2^(b+1) - k)b + (2k - 2^(b+1)) (b+1))/(k) = ceil(log2 of k) - ((2^(ceil of log2k) - k)/(k)) is between (log2k ,log2k + 1)

- The total expected cost for a document of length L: Cost = L * Lavg

- With equal frequencies, Lavg depends only on k, not on the particular document, so any two documents with the same alphabet size have the same per-character cost (the total scales by L).

- Special case: If k is a power of two, then Lavg = log2k and Huffman equals fixedl ength. Otherwise, Lavg < ceiling of log2k (Huffman is strictly better by (2^(ceiling of log2k) -k))/k bits/char.





- **2a.**



def min_heapify(a, n, i):
    l = 2*i + 1
    r = 2*i + 2

    #Keep track of whether current node is smaller than its children.

    smallest = i

    if l < n and a[l] < a[smallest]:
        smallest = l
    
    if r < n and a[r] < a[smallest]:
        smallest = r

    if smallest != i:
        
        #Swap the index with the smaller child.

        a[i], a[smallest] = a[smallest], a[i]
        min_heapify(a, n, smallest)

In the worst-case, min-heapify will 


def build_min_heap(a, n):

    #Start bottom-up using the leaves since they are already heaps.

    for i in range(n//2 -1, -1, -1): #n//2-1 is the last internal node of the tree

        min_heapify(a, n, i)

- Correctness
-- We store the heap in array depicting an almost-complete binary tree with the left child of i being 2*i+1 and right child of i being represented by 2*i+2.

--Invariant for the bottom-up approach: When we call min_heapify(a, n, i), both the subtrees rooted at i's children are already min-heaps.

---Base: all leaves ( i >= n//2) are heaps.
---Step: min_heapify compares a[i] with the smaller child, swaps if needed, and recurses only into that child. As the child's subtree was a heap, pushing the larger key down will mantain the heap property below. By the time the loop finishes at i=0, the whole tree is a heap.


- Each call to min_heapify(i) will cost O(hi) where hi is the height of the nodes at i, how many levels it can move down.
- In a complete binary tree, the number of nodes at height h is at most n/2^(h+1). 
-- Thus, the total work <= summation from h>=0 of (n/2^(h+1)) * O(h) = O(n * summation from h>=0 of ((h)/(2^(h+1)))) = O(n), since summation of all h>=0 of (h/2^(h+1)) = 1.


- **2b.**

- The algorithm is sequential in nature, therefore the span will be O(N) just like the work.

- Another approach is to do Level-parallel heapify: Grouping the nodes by the depth and then running sift_down in parallel for all the nodes at the same depth and then proceeding from the deepest internal level to the root.

-- The nodes on a level touch disjoint subtrees, so there are no conflicts and the childrne have already been heapified. 

-- The total work will remain O(N) but the span would be sum over the levels of the longest sift_down at that level: Summation from h = 1 to floor of (log2n)O(h) = O(log2n). 

--- In contrast, meldable heaps with parallel reduce via meld as was proven in the class have W(n) = O(nlogn), S(n) = O(log2n) as expected.

- **3a.**



- **3b.**




- **3c.**



- **4a.**



- **4b.**




- **4c.**


- **5a.**



- **5b.**




- **5c.**
