import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

#Match and Search 
last_name = "Love"
first_name = "Kenneth"
#print(re.match(last_name, data))
#print(re.search(first_name, data))

##print(re.match(r'\w, w', data))
##print(re.match(r'\d\d\d-\d\d\d\d', data))

#Searching phone number in entire raw string in hte first line
#print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data))

# Searches for phone number in first line
#print(re.search(r'\(?\d{3}\)? \d{3}-\d{4}', data))

# Searches for phone number on all lines format (222) 222-2222
# print(re.findall(r'\(?\d{3}\)? \d{3}-\d{4}', data))
# Searches for phone number on all lines format includes 222-222-2222 as well
# print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))

# Prints the first two words in the first line of string
#print(re.search(r'\w+, \w+', data))

# Prints the first two words from all lines
#print(re.findall(r'\w*, \w+', data))

# Email addresses
#print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))

# Tree house instances in data
print(re.findall(r'\b[treehous]+\b', data, re.IGNORECASE))
print(re.findall(r'\b[treehous]{9}\b', data, re.IGNORECASE))