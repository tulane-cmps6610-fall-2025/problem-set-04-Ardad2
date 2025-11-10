# pip install bitarray
from collections import Counter
from bitarray.util import huffman_code

def get_frequencies(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        C = Counter()
        for line in f:
            C.update(line)
    return dict(C)

def fixed_length_cost(freq):
    if not freq:
        return 0
    k = len(freq)                               # distinct symbols
    bits_per_sym = (k - 1).bit_length()         # == ceil(log2(k))
    return bits_per_sym * sum(freq.values())

def huffman_cost_from_freq(freq):
    code = huffman_code(freq)                   # {symbol -> bitarray}
    return sum(len(code[s]) * f for s, f in freq.items())

files = ["f1.txt", "alice29.txt", "asyoulik.txt", "grammar.lsp", "fields.c"]

for file in files:
    print(file)
    freq = get_frequencies(file)

    fixed_cost = fixed_length_cost(freq)
    print("Fixed-length cost:  %d" % fixed_cost)

    huff_cost = huffman_cost_from_freq(freq)
    print("Huffman cost:  %d" % huff_cost)

    ratio = (huff_cost / fixed_cost) if fixed_cost else float("nan")
    print("Huffman vs Fixed-length:  %.4f" % ratio)
    print("---------------------")
