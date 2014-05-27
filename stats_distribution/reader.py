import sys
import argparse
import logging

from stats_distribution import setup_logging

logger = logging.getLogger()

class ReadError(Exception):
  def __init__(self, message):
    self.value  = message

  def __str__(self):
    return repr(self.value)

def readLine(line, criteria, position):
  columns = line.split(criteria)
  if position >= len(columns):
    raise ReadError("Line only have " + str(len(columns)) + " columns. " + 
      "( You're asking for line " + str(position))
  text = columns[position]
  return text

def readFile(fullText, criteriaForFile = "\n", criteriaForLine = "\t", position = 0):
  lines = fullText.split(criteriaForFile)
  newText = ""
  countLine = 0
  countLineOutput = 0
  for line in lines:
    try:
      countLine +=1
      if line == "":
        logger.warn("Warning: Empty fields at line: " + str(countLine))
        continue
      newText += readLine(line, criteriaForLine, position) + criteriaForFile
      countLineOutput += 1
    except Exception as e:
      logger.error("Failed at line: " + str(countLine) + ", " + str(e))
  return newText, countLine, countLineOutput
  
def reader(path, criteriaForFile = "\n", criteriaForLine = "\t", columnPosition =0):
  with open(path, "r") as contentFile:
    fullText = contentFile.read()
  [newText, countLine, countLineOutput] = readFile(fullText, criteriaForFile, criteriaForLine, columnPosition)
  logger.debug("Total lines = " + str(countLine) + ", output lines = " + str(countLineOutput))
  print(newText)
  return newText

def cat():
  #Parser input arguments
  parser = argparse.ArgumentParser()
  #positionals
  parser.add_argument('f',
    help = 'Input file path',
    type = str)
    
  #with default
  parser.add_argument('-cf',
    help = 'Split criteria for file, default = newline',
    default = '\n',
    type = str,
    required = False)
  parser.add_argument('-cl',
    help = 'Split criteria for line, default = tab',
    default = '\t',
    type = str,
    required = False)
  parser.add_argument('-cp',
    help = 'Column position of text',
    default = 0,
    type = int,
    required = False)
  
  args = parser.parse_args()
  try:
    setup_logging()
    reader(args.f, args.cf, args.cl, args.cp)
  except Exception as e:
    logger.error("Error found: " + str(e))
    sys.exit(1)
  sys.exit(0)
