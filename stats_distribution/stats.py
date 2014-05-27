import nltk
import logging
from stats_distribution.model import Tweets

logger = logging.getLogger()

class DBError(Exception):
  def __init__(self, expr, msg):
    self.expr = expr
    self.msg = msg

def readRelationalData(DbField):
  result = []
  if type(DbField) is not str:
    raise Exception("DbField is not string") 
  for tweet in Tweets.select():
    fields = tweet._data
    if not DbField in fields:
      raise DBError("Expr", "Field is not defined in model")
    text = fields[DbField]
    for word in nltk.word_tokenize(text):
      logger.debug(word)
      result.append(word)
  return result
