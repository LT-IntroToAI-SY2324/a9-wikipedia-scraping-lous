import re


string = "called piiig"
string1 = "turned fig"

pat = re.compile("ig")
result = pat.search(string)
print(result.group())

pat = re.compile("...ed")
result = pat.search(string)
print(result.group())