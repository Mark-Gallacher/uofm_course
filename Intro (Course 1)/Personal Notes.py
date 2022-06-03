#!/usr/bin/env python
# coding: utf-8

# # Introduction to Python
import csv
import datetime as dt
import time as tm


# ## Python Functions
x = 1
y = 2
'''
def add_numbers(x,y):
    return x+y

print(add_numbers(1,2))

def add_numbers(x,y,z=None):
    if z != None:
        return x+y+z
    else:
        return x+y

print(add_numbers(1,2,3))

a = add_numbers
a(1,2)

# ## Python Types and Sequences

type('This is a string')

type(1)

type(1.2)

type(None)

type(a)

x = (1, 'a', 2, 'b')
type(x)

x = [1, 'a', 2, 'b']
type(x)


# ### List Functions

x.append(100)
print(x)

for item in x:
    print(item)

i = 0 
while( i != len(x)):
    print(x[i])
    i = i + 1

a = [1,2]+[3,4]
b = [1,2]*3
c = 1 in [1,2,3]


# ### Slicing!
x = 'This is a string'
print(x[0])
print(x[0:1])
print(x[0:2])

print(x[-1])
print(x[-4:-2])
print(x[:3])
print(x[3:])

firstname= 'Mark'
surname= 'Gallacher'

print(firstname + ' ' + surname)
print(firstname * 2)
print('ark' in firstname)

'''

# Splitting

firstname = "Mark Graham Gallacher".split(' ')[0]
surname = "Mark Graham Gallacher".split(' ')[-1]
middlename = "Mark Graham Gallacher".split(' ')[1]
print(firstname)
print(surname)
print(middlename)


# ### Dictionaries ( reqs {} and : )
'''
x={'Mark Gallacher': 'address@gmail.com', 'Bill Gates': 'Billsemail@gmail.com' }
name1 = x['Mark Gallacher']

for name in x:
    print(x[name])

for email in x.values():
    print(email)

for name, email in x.items():
    print(name)
    print(email)

x = ('Mark', 'Gallacher', 'EmailAddress')
fname, lname, email = x
'''
# ## More on Strings

print('Mark' + str(2))

sales_record = {'price': 3.24,
                'num_items': 4,
                'persons': 'Mark'}

sales_statement = '{} brought {} items(s) at a price of {} each for a total of {}'

print(sales_statement.format(sales_record['persons'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']))


# ## Reading and Writing CSV Files


with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))
    
# mpg[:3]
len(mpg)
mpg[0].keys()


# ### Needs to use float() as numbers are saved as strings, so we convert them to floats

sum(float(d['cty']) for d in mpg) / len(mpg)
sum(float(a['hwy'])for a in mpg) / len(mpg)

cylinders = set(d['cyl'] for d in mpg)

CtyMpgByCyl = []

for c in cylinders:
    summpg = 0
    cyltypecount = 0
    for d in mpg:
        if d['cyl'] == c:
            summpg += float(d['cty'])
            cyltypecount += 1
    CtyMpgByCyl.append((c, summpg / cyltypecount))
    
CtyMpgByCyl.sort(key=lambda x: x[0])

vehicleclass = set(d['class'] for d in mpg)

BwyMpgByClass = []

for t in vehicleclass:
    summpg = 0
    vclasscount = 0
    for d in mpg:
        if d["class"] == t:
            summpg += float(d['hwy'])
            vclasscount += 1
    BwyMpgByClass.append((t, summpg / vclasscount))
    
BwyMpgByClass.sort(key=lambda x: x[1])

# Note this doesn't use Pandas, which is much more efficient

# Dates and Times


tm.time()

dtnow = dt.datetime.fromtimestamp(tm.time())

delta = dt.timedelta(days=100)
today = dt.date.today()
today - delta

# ## Advanced Objects, map()


class Person:  # usually camel case (Person_Name_For_Example)

    department = ' School of Life Sciences'
    
    def set_name(self, new_name):  # Must include self and self. (maybe different in Pandas)
        self.name = new_name

    def set_location(self, new_location):
        self.location = new_location


person = Person()

person.set_name('Mark Gallacher')
person.set_location('Glasgow, Scotland')
print('{} lives in {} and works in the depart {}'.format(person.name, person.location, person.department))

# functional programming is side effect free?
# map(function, iterable, ... ) all must be iterable

store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]

cheapest = map(min, store1, store2)

# List comprehension

my_list = []
for number in range(0,1000):
    if number % 2 == 0:
        my_list.append(number)

print(my_list)

times_table() == [j*i for i in range(10) for j in range(10)]





