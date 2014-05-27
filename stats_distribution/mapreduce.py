import sys

from itertools import groupby
from operator import itemgetter

def read_input(file):
  for line in file:
    # split the line into words
    yield line.split(" ")

def mapper(separator = '\t', file = sys.stdin):
  # input comes from STDIN (standard input)
  data = read_input(file)
  countWords = 0
  for words in data:
    # write the results to STDOUT (standard output);
    # what we output here will be the input for the
    # Reduce step, i.e. the input for reducer.py
    #
    # tab-delimited; the trivial word count is 1
    for word in words:
      print '%s%s%d' % (word, separator, 1)
      countWords += 1
  return countWords

def read_mapper_output(file, separator='\t'):
  for line in file:
    yield line.rstrip().split(separator, 1)

def reducer(separator = '\t', file = sys.stdin):
  # input comes from STDIN (standard input)
  data = read_mapper_output(file, separator = separator)
  # groupby groups multiple word-count pairs by word,
  # and creates an iterator that returns consecutive keys and their group:
  #   current_word - string containing a word (the key)
  #   group - iterator yielding all ["&lt;current_word&gt;", "&lt;count&gt;"] items
  for current_word, group in groupby(data, itemgetter(0)):
    try:
      total_count = sum(int(count) for current_word, count in group)
      print "%s%s%d" % (current_word, separator, total_count)
    except ValueError:
      # count was not a number, so silently discard this item
      pass
