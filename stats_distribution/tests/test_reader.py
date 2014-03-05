import unittest
from stats_distribution.reader import ReadError
from stats_distribution.reader import readLine
from stats_distribution.reader import readFile
from stats_distribution.reader import reader

class TestReaderFunctions(unittest.TestCase):
  def testReadLine(self):
    test1 = "1230\tother field\tthe important text field\tother field"
    sol1 = "the important text field"
    self.assertEqual(readLine(test1, "\t", 2), sol1)

  def testReadLineNonExistingField(self):
    test1 = "1230\tother field\tthe important text field\tother field"
    self.assertRaises(ReadError, readLine, test1, "\t", 10)

  def testReadFile(self):
    test1 = "1230\tother field\tthe important text field in line 1\n1231\tother field\tthe important text field in line 2"
    sol1 = "the important text field in line 1\nthe important text field in line 2\n"
    [fullText, countLine, countLineOutput] = readFile(test1, position = 2)
    self.assertEqual(fullText, sol1)
    self.assertEqual(countLine, 2)
    self.assertEqual(countLineOutput, 2)

  def testReader(self):
    pathtest = "test/file1"
    sol1 = "the important text field in line 1\nthe important text field in line 2\nthe important text field in line 3\n"
    self.assertEqual(reader(pathtest, columnPosition = 2), sol1)
