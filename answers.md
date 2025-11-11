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

def change_pow2(N: int, k: int | None = none):

#Return the (minimum no. of coins, the breakdown of each coin with how many times used) for making a given amount N with the coin with denominations {2^0, 2^1, 2^2, …, 2^k}.

#Base cases

if N < 0:
	Error

if N == 0:
	return 0, {}

#If there is no cap on the denominations of the currency, then the highest denomination would be 2^(ceiling log2n of N)).

if k is None:
	k = max(0, N.bit_length() - 1)

coins_used = 0
breakdown = {}

for power in range(k, -1, -1): # Greedy: Go from 2^k down to 2^0

	coin = 1 << power #Calculate the value of the denomination 2^p.
	q, N = divmod(N, coin) #Take as many coins of this denomination that can fit.

	if q:
		breakdown[coin] = q
		coins_used += q
	if N == 0:
		break; #We are done.

Return coins_used, breakdown

- **3b.**
 - Given an amount N, let p, which is the maximum power denomination coin we can take, we have
 - p = min {floor(log2N), k}. If we have no provided value for k, then there are no restrictions, and we will take k as floor(log2N) since that is the maximum value.
 - The maximum amount of coins we can take of denomination p is q = floor(N/(2^p)).
 - Taking q coins of value 2^P, we can reduce N to N - q.2^p, and then repeat the same. N < 2^p, so the next p will be <= p -1. We will stop when N = 0.
 - Greedy Choice Property
 -- Claim: There exists an optima solution uses exactly q = floor(N/(2^p)) coins of value 2^p.
 -- Proof: 
 --- If we use more than q coins of 2^p, we would exceed N. 
 --- Suppose an optimal solution S uses fewer than q coins of value 2^p. Then at least 2^p of the amount will be left that needs to be covered by smaller coins: {2^0, .., 2^p-1}. Any total >= 2^p would require at least two coins, the largest smaller coin is 2^p-1 and at least another one 2^1 coin would be required. 
 --- These two coins can be replaced by one 2^p coin that keeps the sum the same and also reduces the coin count by 1.
 --- Repeating this until possible would yields a solution with more 2^p coins and strictly fewer coins overall, therefore contradicting the optimality of S.
 --- Therefore, an optimal solution must use exactly q coins of value 2^P.

- Optimal Substructure
-- Let R = N - q*2^p (so 0 <= R <= 2^P). 
-- Every optimal solution for N starts with those q coins of value 2^p.
-- The remaining part must solve the same problem on the amount R using only coins {2^0, ..., 2^p-1}, a coin > 2^p cannot appear because R <2^P). Therefore, we can represent the optimal substructure by: OPT(N, k) = q + OPT(R, p - 1)

--- Proving optimality by strong induction on N: The base cases N = 0 (cost 0) and N < 2^0 are trivial. For N > 0, by the greedy choice lemma, the first step in every optimal solution is to take q coins of value 2^p. The remain R < N is solved optimally by the inductive hypothesis, so the algorithm's total coin count is q + OPT(R, p - 1) which is optimal for N.


- **3c.**

- Work = O(min(k+1, floor(log2N) + 1))
-- Each loop iterations handles exactly one coin size 2^p with constant-time updates. It steps p down by 1 each time and never evisits a size, the so the number iteration is at most the number of avaliable sizes: k + 1 if there's a cap at 2^k or floor(log2N) + 1 if no such restriction is provided (largest coin chosen).
-- This is generally around O(logN) for the unbounded cases.

- Span = O(min(k+1, floor(log2N) + 1)), the same as work since the algorithm is sequential, with the iterations depending on the result of the previous ones.

- **4a.**

- Here are two examples which show that the previous greedy choice of picking the largest possible denomination as comapred to the given amount N dollars would not work or not work optimally.
- Eg 1. Let N = 100 and D = {40, 60, 70}. Greedy picks 70 first, remainder 30 is not representable so Greedy fails to make chance. Change can be made by taking 60 + 40, which is 2 coins.
- Eg 2. Let N = 100 and D = {10, 30, 80, 70}. Greedy picks 80 first, but to make 20, it will have to take 2 10's. Therefore taking 3 coins. If it had taking 70 and 30, it would have been done in just 2 coins. So while Greedy leads to a solution it is not optimal.
- Therefore, we have two examples that prove the greedy choice might not result in a solution and even if it did, it might not be the optimal one.



- **4b.**
- Optimal Substructure
- Define OPT(N) = the minimum number of coins whose values sum to N (and +infinity if impossible)
- For any N > 0 with OPT(N) < +infinity, there exists a coin d element of D with d <= N such that
- OPT(N) = 1 + OPT(N - d)
- The multiset of coins used for N - d in that equality is itself optimal for the amount N - d.
- Proof 
- Take any optimal solution S for N. Let d the element of S be one coin in that solution, and let S' = S \ {d}. Then S' sums to N - d and |S| = 1 + |S'| = OPT(N).
- If S' were not optimal for N - d, there would exist another solution T for N - d with |T| < |S'|. But then T U {d} is a solution for N using |T| + 1 < |S'| + 1 = OPT(N) coins, a contradiction.
- Therefore, S' must be optimal for N - d, giving the stated recurrence.




- **4c.**

Let D = {d1,..., dk} be the denominations.
dp[x] = the minimum no. of coints to make amount of coins (or +infinity if impossible to do so)

dp[0] = 0
for x = 1..N:
    dp[x] = +infinity
    for each d in D:
        if d<=x:
            dp[x] = min(dp[x], 1 + dp[x - d])
        
answer = dp[N]

- Work: W(N) = O(N * k). Each of the N amount states consider upto k denominations once and memoization ensures that no state is recomputed.
- Span: This implementation is sequential so O(N * k). 
- Possible Parallelization: FOr each x, the k candidates 1 + dp[x-d] can be min reduced in parallel, giving a per-state span of O(logK). Since dp[x] depends on smaller amounts, the states will execute in order and the overall span will be O(NlogK) with the same work.


- **5a.**



- **5b.**




- **5c.**
