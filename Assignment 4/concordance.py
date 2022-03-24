from hash_quad import *
import string


class Concordance:
    def __init__(self):
        self.stop_table = None
        self.concordance_table = None

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.stop_table = HashTable(191)
        try:
            file_in = open(filename)
        except FileNotFoundError:
            raise FileNotFoundError("File Not Found")
        for line in file_in:
            self.stop_table.insert(line.splitlines()[0])
        file_in.close()

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table,
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        Process of adding new line numbers for a word (key) in the concordance:
            If word is in table, get current value (list of line numbers), append new line number, insert (key, value)
            If word is not in table, insert (key, value), where value is a Python List with the line number
        If file does not exist, raise FileNotFoundError"""
        self.concordance_table = HashTable(191)
        try:
            file_in = open(filename)
        except FileNotFoundError:
            raise FileNotFoundError("File Not Found")
        line_num = 0
        for line in file_in:
            line_str = ""
            line_num += 1
            line_dic = {}
            line_str += line
            for char in line:
                if char == "'":
                    line_str = line_str.replace(char, "")
                if char in string.punctuation:
                    line_str = line_str.replace(char, " ")
                if char == "\n":
                    line_str = line_str.replace(char, " ")
            line_lst = line_str.split(" ")
            for i in line_lst:
                if i.isalpha():
                    add = i.lower()
                    if line_dic.get(add) is None:
                        if self.stop_table.in_table(add) is False:
                            line_dic[add] = line_num
                            self.concordance_table.insert(add, line_num)
        file_in.close()

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        try:
            file_out = open(filename, "w")
        except FileNotFoundError:
            raise FileNotFoundError("File Not Found")
        word_lst = self.concordance_table.get_all_keys()
        word_lst.sort()

        first = word_lst[0]
        ln_num1 = self.concordance_table.get_value(first)
        ln_str1 = ""
        ln_str1 += " " + str(ln_num1[0])
        file_out.write(first + ":" + ln_str1)
        word_lst.remove(word_lst[0])

        for i in word_lst:
            ln_num = self.concordance_table.get_value(i)
            ln_str = ""
            for c in ln_num:
                ln_str += " " + str(c)
            file_out.write("\n" + i + ":" + ln_str)
        file_out.close()


