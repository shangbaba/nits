import hashlib
import random
from string import ascii_letters, digits

i = 0
y = 0
l = ''
lineText = ''
textBlock = []
h = []
symbols = '~!@#$%^&*()_+-={}[]:";\'<>,.?/|\\'
columnMarks = ascii_letters + digits + symbols

for x in range(0, 10001):
    x += 1
    h = random.choices(ascii_letters + digits)
    strh = ''.join(h)
    l = l + strh


while i <= 10000:
  if i != 0 and i % 93 == 0:
    lineNum = "{:03}".format(y+1)     #add leading zeros to line numbers
    if y % 3 == 0:
      textBlock.append(">>> " + columnMarks + "\n")
    textBlock.append("    " + lineText + ' ' + lineNum + "\n")
    lineText = ''
    lineText = lineText + l[i]
    i = i + 1
    y = y + 1
    if y > 101:
      break
  else:
    lineText = lineText + l[i]
    i = i + 1
    
print (''.join(textBlock))
