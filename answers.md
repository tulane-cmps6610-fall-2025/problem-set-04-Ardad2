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
    r = 2*i + 1

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


def build_min_heap(a, n):

    #Start bottom-up using the leaves since they are already heaps.

    for i in rage(n//2 -1, -1, -1): #n//2-1 is the last internal node of the tree

        min_heapify(a, n, i)





- **2b.**




- **3a.**



- **3b.**




- **3c.**



- **4a.**



- **4b.**




- **4c.**


- **5a.**



- **5b.**




- **5c.**
