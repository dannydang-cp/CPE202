import unittest
import filecmp
from concordance import *

class TestConcordance(unittest.TestCase):
    def test_load_stop_table(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        try:
            conc.load_stop_table("1 2 3 +")
            self.fail()
        except FileNotFoundError as e:
            self.assertEqual(str(e), "File Not Found")

    def test_concordance_table(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        try:
            conc.load_stop_table("1 2 3 +")
            self.fail()
        except FileNotFoundError as e:
            self.assertEqual(str(e), "File Not Found")

    def test_write_concordance(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_con.txt")
        try:
            conc.load_stop_table("1 2 3 +")
            self.fail()
        except FileNotFoundError as e:
            self.assertEqual(str(e), "File Not Found")

    def test_1(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file1.txt")
        conc.write_concordance("file1_con.txt")
        self.assertTrue((filecmp.cmp("file1_con.txt", "file1_sol.txt")))
        result = filecmp.cmp("file1_con.txt", "file1_sol.txt")
        print(result)