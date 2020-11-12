import pprint
import glob
from pyparsing import *


def magic_parse_function(fld_name, source):
   from pyparsing import Keyword, nestedExpr

   # define parser
   parser = Keyword(fld_name).suppress() + nestedExpr('{','}')("content")

   # search input string for matching keyword and following braced content
   matches = parser.searchString(source)

   # remove quotation marks
   return [[qs for qs in r[0].asList()] for r in matches]

conf_path = glob.glob("svn/rancid/PANs/configs/*")

for conf in conf_path:
  f = open(conf)
  ffile = f.read()
  tmp = magic_parse_function("nat",ffile)
  print('Firewall: ' + conf + '\n')
  pprint.pprint(tmp[0])
  print('\n')

exit()
