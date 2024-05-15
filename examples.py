
import re

# . (dot) any char
# \w word char
# \d digit
# \s whitespace \S non-whitspace
# + 1 or more
# * 0 or more
# [] set of char
# {} a number of instances

string = "called piiig"
pat = re.compile("iig")
result = pat.search(string)
print(result)
print(result.group())

string = "called piiig"
pat = re.compile("xiig")
result = pat.search(string)
print(result)

pat = re.compile("called")
result = pat.match(string)
print(result)

pat = re.compile("ig")
result = pat.search(string)
print(result.group())

pat = re.compile("...ed")
result = pat.search(string)
print(result.group())

pat = re.compile("x...g")
result = pat.search(string)
# print(result.group())

string = "called piiig much better: xyzg"
pat = re.compile("...g")
result = pat.search(string)
print(result.group())

pat = re.compile("...g")
result = pat.findall(string)
print(result)

string = "c.lled piiig much better: xyzg"
pat = re.compile("...g")
result = pat.findall(string)
print(result)

pat = re.compile("c\.l")
result = pat.search(string)
print(result.group())

string = 'blah :cat blah blah'
pat = re.compile(":\w\w\w")
result = pat.search(string)
print(result.group())

string = "blah :catxxx blah blah bah"
pat = re.compile(":\w\w\w")
result = pat.search(string)
print(result.group())

string = "blah :123 blah blah bah"
pat = re.compile(":\d\d\d")
result = pat.search(string)
print(result.group())

string = "1 2 3"
pat = re.compile("\d\s\d\s\d")
result = pat.search(string)
print(result.group())

string = "1       2       3      "
pat = re.compile("\d\s+\d\s+\d")
result = pat.search(string)
print(result.group())

string = "blah blah :lanetech blah blah"
pat = re.compile(":\w+")
result = pat.search(string)
print(result.group())

string = "blah blah :lanetech123 blah blah"
pat = re.compile(":\w+")
result = pat.search(string)
print(result.group())

string = "blah blah :lanetech123& blah blah"
pat = re.compile(":\w+")
result = pat.search(string)
print(result.group())

string = "blah blah :lanetech123& blah blah"
pat = re.compile(":\S+")
result = pat.search(string)
print(result.group())

string = "blah balh blah robert.berg@cps.edu blah blah blah"
pat = re.compile("\w+@\w+")
result = pat.search(string)
print(result.group())

pat = re.compile("[\w.]+@[\w.]+")
result = pat.search(string)
print(result.group())

pat = re.compile(".+")
result = pat.search(string)
print(result.group())

# Grouping
pat = re.compile("([\w.]+)@([\w.]+)")
result = pat.search(string)
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.groups())

string = "Card Number: 1234123412341234 CVV: 123"
pat = re.compile("(Card Number:) (?P<num>\d{16}) (CVV:) (?P<cvv>\d{3,4})")
result = pat.match(string)
print(result.group("num"))
print(result.group("cvv"))
