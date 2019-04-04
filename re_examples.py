import re
# example code:
string_with_newlines = """something someotherthing"""

#re.match() # It matches the word in the Begining of the sentence.If it match it will return matched object.if not None.
print re.match('some', string_with_newlines)# matches
print re.match('someother',
               string_with_newlines) # won't match
print re.match('^someother', string_with_newlines,
               re.MULTILINE) # also won't match
#re.search --> It matches the word, anywhere in the sentence.If it match it will return matched object.if not None.
print re.search('someother',
                string_with_newlines).group() # finds something
print "inbetween",re.search('other',
                string_with_newlines)
print re.search('^someother', string_with_newlines,
                re.MULTILINE) # also finds something
#re.compile() -> it will compile the matched obj and keep itself. it will also return the Matched onject.
#The compiled obj has to get using re.match() or re.search()
m = re.compile('thing$', re.MULTILINE)
print "m",m
print m.match(string_with_newlines) # no match
print m.match(string_with_newlines, pos=4) # matches
print m.search(string_with_newlines,
               re.MULTILINE) # also matches

