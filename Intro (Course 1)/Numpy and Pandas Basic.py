import numpy as np
import math
import re


# Array Creation

a = np.array([1, 2, 3])
print(a)

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b, b.shape)

d = np.zeros((2, 3))
print(d)
e = np.ones((2, 3))
print(e)

print(np.random.rand(4, 4))
print(np.arange(10, 50, 2))
print(np.linspace(0, 2, 15))

fahrenheit = np.array([0, -10, -5, -15, 0])
celsius = (fahrenheit - 32) * (5 / 9)
print(celsius > - 20)  # boolean array

a = np.array(([1, 1], [0, 1]))
b = np.array(([2, 0], [3, 4]))
print(a*b)

array1 = np.array(([1,2,3], [4, 5, 6]))
array2 = np.array(([7.1,8.2,9.1], [10.4, 11.2, 12.3]))
print(array1.dtype, array2.dtype)
array3 = array1+array2
print(array3, array3.dtype)

b = np.arange(1,16,1).reshape(3,5)
print(b)

a = np.array(([1,2], [3, 4], [5, 6]))
print(np.array([a[0, 0], a[1, 1], a[2, 1]]))
print(np.array(a[[0, 1, 2], [0, 1, 1]]))

a = np.array(([1,2,3,4], [1,3,6,9], [2,4,6,8]))
print(a[:3,:3])

wines = np.genfromtxt("/datasets/winequality-red.csv",
                      delimiter=";", skip_header=1)
print(wines[:, 0], 'line51')  # first column
print(wines[:, 0:1])  # first column, but different layout

print(wines[:, -1].mean())  # mean of quality

graduate_admission = np.genfromtxt("/datasets/Admission_Predict.csv",
                                   dtype=None, delimiter= ',', skip_header=1,
                                   names=('Serial_No', 'GRE_Score', ' TOEFL_Score', ' University_Rating',
                                             'SOP', ' LOR', 'CGPA', 'Research', 'Chance_of_Admit'))
print(graduate_admission['CGPA'][0:5])  # looking at the CGPA column but the first 5
graduate_admission['CGPA'] = graduate_admission['CGPA']/ 10 * 4
print(graduate_admission['CGPA'][:20])

print(len(graduate_admission[graduate_admission['Research'] == 1]))
print(graduate_admission[graduate_admission['Chance_of_Admit']> 0.8]['GRE_Score'].mean())
print(graduate_admission[graduate_admission['Chance_of_Admit']< 0.4]['GRE_Score'].mean())

print(graduate_admission[graduate_admission['Chance_of_Admit']> 0.8]['CGPA'].mean())
print(graduate_admission[graduate_admission['Chance_of_Admit']> 0.8]['CGPA'].mean())

# Regular Expression and Text Manipulation

text = 'This is a good day'

if re.search('good', text):
    print('wonderful')
else:
    print('alas :(')

text = 'Amy works hard, Amy is Smart, Our student Amy is successful'
print(re.split('Amy', text))
print(re.findall('Amy', text))

'''
^ means start, but inside a set operator ( [] ), it means to remove that pattern
$ means end
'''
print(re.search('^Amy', text))  # returns re.Match object - boolean object with the pattern

# Character Classes (Pattern)

grades = "ACAAAABCBCBAA"
print(re.findall('B', grades))
print(re.findall('[AB]', grades), 'line94') # Returns A and B, but not AB!!
print(re.findall(('A|B'), grades))  # Does work on strings!!
print(re.findall('[A][B-C]', grades))
print(re.findall('AB|AC', grades))
print(re.findall('[^A]', grades))  # caret character used to remove A from string
print(re.findall('^[^A]', grades))  # returns empty list as string begins as a list

# Quantifiers (number of times a pattern is matched)
'''
e{m, n}, where e = expression or characters, m is the min number of times, n is the max
if one number in {} then assumed as both numbers
'''

print(re.findall('A{2,10}', grades))  # finds a string of A's of length 2 to 10
print(re.findall('A{1,1}A{1,1}', grades))  # notice how output is different, only produces AA
print(re.findall('A{2}', grades))  # same as 'A{2,2}' and 'AA'

with open('../datasets/ferpa.txt', 'r') as file:
    wiki = file.read()

'''
headers are usually followed by square brackets, so we can use that to find the headers
'''
headers = re.findall(r'[a-zA-Z]{1,100}\[edit\]', wiki)  # only gives lasts word of header, and not v efficient
print(headers)

headers = re.findall(r'[\w]{1,100}\[edit]', wiki)
# [\w] represents all alphanumeric letters, called a metacharacter
# [\s] represents all white space, see documentation for all metacharacters
print(headers)

headers = re.findall(r'[\w]*\[edit]', wiki)  # astericks replaces the number as to larger than one
print(headers)
headers = re.findall(r'[\w ]*\[edit]', wiki)  # adding a space beside \w means we find spaces as well
print(headers)

for title in re.findall(r'[\w ]*\[edit]', wiki):
    print(re.split(r'\[', title)[0])

# Groups - using more than one pattern

headers = re.findall(r'([\w ]*)(\[edit])', wiki)
print(headers, '136')


# This returns a string, we would like a list to get different items out much easier - use finditer
for item in re.finditer(r'([\w ]+)(\[edit\])', wiki):
    print(item.group(1))

# Labelling - rarely used but important to know
'''
Syntax is (?P<name>) - () starts pattern and ends, ?P is used to indicate that this is an extension to basic regexes, 
and <name> is the dictionary index wrapped in <>
'''
for item in re.finditer('(?P<title>[|\w ]+)(?P<edit_link>\[edit\])', wiki):
    print(item.groupdict()['title'])  # groupdict returns all the groups of the dictionary

'''
[] is used for individual characters
() is to group patterns together
{} is used for quantifiers - like *, ?, m{n}

other characters; 
\d - any digit
. is a single character which is not a newline
'''

# Look ahead and Look Behind

for item in re.finditer('(?P<title>[\w ]+)(?=\[edit\])', wiki):
   print(item, 'line164')

# Wiki example 2

with open('../datasets/buddhist.txt', "r", errors='ignore') as file:
    wiki = file.read()

# Using this to look at verbose regex, or multiline regex which aims to make it easier to read but we
# need to indicate all white space characters with "\s" or "\"
print(wiki)
pattern="""
(?P<title>.*)               #the university title
(–\ located\ in\ )|          #an indicator of the location
(?P<city>\w*)|               #city the university is in
(,\ )|                       #separator for the state
(?P<state>\w*)              #the state the city is located in"""

for item in re.finditer(pattern, wiki, re.X):
    print(item.groupdict())  # This is their code and It doesn't work

# Example New York Times and Hashtags

with open('../datasets/nytimeshealth.txt', 'r', errors='ignore') as file:
    health = file.read()

pattern = '#[\w\d]*(?=\s)'
print(re.findall(pattern, health))  # prints all the hashtags, as it needs to start with a hashtag and
                                    # finish with a whitespace


# Names Task
simple_str = """Amy is 5 years old, and her sister Mary is 2 years old. 
Ruth and Peter, their parents, have 3 kids."""
pattern = '[A-Z]\w+'

def names():

    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""
    pattern = '[A-Z]\w+'
    names = re.findall(pattern, simple_string)
    return(names)

print(names())

assert len(names()) == 4, "True - There are 4 Names"


