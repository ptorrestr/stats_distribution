import unittest
from stats_distribution.mapreduce import read_input
from stats_distribution.mapreduce import mapper
from stats_distribution.mapreduce import read_mapper_output
from stats_distribution.mapreduce import reducer

class TestGeneralFunctions(unittest.TestCase):
  def testReadInput(self):
    test1 = ["this is an sample line for splitting"]
    sol1 = ["this", "is", "an", "sample", "line", "for", "splitting"]
    res1 = read_input(test1)
    for val in res1:
      self.assertEqual(val,  sol1)

  def testMapper(self):
    test1 = ["this is an sample for mapping many lines many lines"]
    self.assertEqual(10, mapper(file = test1))

