
# Question 1
import pandas as pd
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj1 = pd.Series(sdata)
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj2 = pd.Series(sdata, index=states)
obj3 = pd.isnull(obj2)

print(obj2['California'] == None)

# Question 2
d = {'1': 'Alice','2': 'Bob','3': 'Rita','4': 'Molly','5': 'Ryan'}
S = pd.Series(d)

print(S.iloc[0:3])  # loc[] returns error as applied to integer?

# Question 3
# Question 4

d = {"gre score": [337, 324, 316, 322, 314],
      "toefl score": [118, 107, 104, 110, 103]}

df = pd.DataFrame(d)
print(df.where(df['toefl score'] >105).dropna())

# Question 5
# Question 6

d = {'one': [0, 4, 8, 13],
     'two': [1, 5, 9, 13],
     'three': [2, 6, 10, 14],
     'four': [3, 7, 11, 15]}

df= pd.DataFrame(d, index= ["Ohio", "Colorado" ,"Utah", "New York"])
print(df.drop(['Utah', 'Colorado']))

# Question 7

s1 = pd.Series({1: 'Alice', 2: 'Jack', 3: 'Molly'})
s2 = pd.Series({'Alice': 1, 'Jack': 2, 'Molly': 3})

print(s2.loc['Jack'])

# Question 8

s = pd.Series({"Apple":1, "Banana": 2, "Cheryy":3})
s1 = pd.Series({"Dragon":4, "Elf": 5, "Horse":6})


print(s.loc['Apple'])
print(pd.concat([s,s1]))

# Question 9
d = {"gre score": [337, 324, 316, 322, 314],
      "toefl score": [118, 107, 104, 110, 103]}

df = pd.DataFrame(d)

f_df = (df['toefl score'] > 105) & (df['toefl score'] < 115)  # produces a boolean map - when we want values

print(f_df)

# Question 10

d = {'Major': ['Maths', 'Sociology'],
    'Name': ['Alice', 'Jack'],
     'Age': [20,22],
     'Gender': ['F', 'M']}

df = pd.DataFrame(d).set_index('Major')
print(df.loc['Maths'])
print(df.T['Maths'])