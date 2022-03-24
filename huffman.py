class HuffmanNode:
    def __init__(self, char_ascii, freq):
        self.char_ascii = char_ascii  # stored as an integer - the ASCII character code value
        self.freq = freq              # the frequency count associated with the node
        self.left = None              # Huffman tree (node) to the left
        self.right = None             # Huffman tree (node) to the right

    def __repr__(self):
        return "[%s: %i; (%s, %s)]" % (self.char_ascii, self.freq, self.left, self.right)

    def __lt__(self, other):
        return comes_before(self, other) # Allows use of Python List sorting

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

def comes_before(a, b):
    """Returns True if node a comes before node b, False otherwise"""
    if a.freq == b.freq:
        return a.char_ascii < b.char_ascii
    else:
        return a.freq < b.freq

def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values"""

    """
    Variables:
        a is a child node
        b is a child node
        new_node is a parent node containing a and b
        freq_total is the total frequency of both child nodes        
    """
    if a.char_ascii < b.char_ascii:
        c = a.char_ascii
    else:
        c = b.char_ascii
    freq_total = a.freq + b.freq
    new_node = HuffmanNode(c, freq_total)
    new_node.left = a
    new_node.right = b
    return new_node

def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file
    Returns a Python List with 256 entries - counts are initialized to zero.
    The ASCII value of the characters are used to index into this list for the frequency counts"""
    f = open(filename)
    countlist = []
    for x in range(256):
        countlist.append(0)
    while True:
        c = f.read(1)
        if not c:
            break
        if ord(c) < 256:
            countlist[ord(c)] += 1
    f.close()
    return countlist



def create_huff_tree(freq_list):
    """Input is the list of frequencies (provided by cnt_freq()).
    Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree. Returns None if all counts are zero."""

    def sort_min(source_list):
        sorted_list = []
        while source_list:
            minimum = source_list[0]
            for x in source_list:
                if comes_before(x, minimum):
                    minimum = x

            sorted_list.append(minimum)
            source_list.remove(minimum)
        return sorted_list
    source_list = []
    for x in range(len(freq_list)):
        if freq_list[x] != 0:
            source_list.append(HuffmanNode(x, freq_list[x]))

    sorted_list = sort_min(source_list)

    if len(sorted_list) == 0:
        return sorted_list

    if len(sorted_list) == 1:
        temp_node = HuffmanNode(sorted_list[0].char_ascii, sorted_list[0].freq)
        del sorted_list[0]
        sorted_list.append(temp_node)

    while len(sorted_list) > 1:
        node_1 = sorted_list[0]
        node_2 = sorted_list[1]

        if node_1.char_ascii < node_2.char_ascii:
            char = node_1.char_ascii
        else:
            char = node_2.char_ascii
        temp_node = HuffmanNode(char, node_1.freq + node_2.freq)
        temp_node.left = node_1
        temp_node.right = node_2
        del sorted_list[0]
        del sorted_list[0]
        sorted_list.append(temp_node)
        sorted_list = sort_min(sorted_list)

    return sorted_list[0]


def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman code for that character stored at that location.
    Characters that are unused should have an empty string at that location"""
    code_list = [0] * 256

    def iterator(tree, path=''):
        if tree.left == tree.right == None:
            code_list[tree.char_ascii] = path
        else:

            iterator(tree.left, path + '0')
            iterator(tree.right, path + '1')

    if node != []:
        iterator(node)
    return code_list

def create_header(freq_list):
    """Input is the list of frequencies (provided by cnt_freq()).
    Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    header = []
    for x in range(256):
        if freq_list[x] != 0:
            header.append(str(x))
            header.append(str(freq_list[x]))
    return " ".join(header)

def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""
    try:
        input = open(in_file, 'r')
    except:
        raise FileNotFoundError

    output = open(out_file, 'w')

    freq = cnt_freq(in_file)

    huffman_tree = create_huff_tree(freq)
    code_list = create_code(huffman_tree)
    code = ''

    for line in input:
        if line == '':
            break
        for char in line:
            code = code + str(code_list[ord(char)])

    header = create_header(freq)
    output.write(header + '\n')
    output.write(code)
    input.close()
    output.close()

freqlist = cnt_freq("file2.txt")
hufftree = create_huff_tree(freqlist)
