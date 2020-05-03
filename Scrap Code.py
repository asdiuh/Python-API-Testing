# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path

#os.chdir(default_path)
a = pd.read_csv('V3 - ECL - renamed columns.csv')
a

os.chdir('/home/redhwanzaman1989/Python Data Analysis/')
os.chdir('/home/redhwanzaman1989/Python API Test/')

red1 = pd.read_excel('/home/redhwanzaman1989/Python Data Analysis/nba-2.xlsx')
red1


# Function definition is here
def printme( str1 , str2 ):
   "This prints a passed string into this function"
   print(str1,str2)
   return;

# Now you can call printme function
printme("hello", "world")

a = df.assign(
new_column = 10
).assign(
new_column1 = 11
)

a2 = df.assign(red = df['Stage'].apply(lambda x: "Red1" if x == "Stage 1" else "Red2" if x == "Stage 2" else "Red3"))




import pandas as pd
a = pd.read_csv('V3 - ECL.csv')
a
#select column
a1 = a["2"]
#resolve column into true false
a2 = a1 == "MB2"
#apply true false vector to dataframe without subsetting any columns
a3 = a[a2]
#apply true false vector to dataframe THEN subset columns
a4 = a[a2][["2","3", "4"]]
#subset columns THEN subset columns
a5 = a[["2","3","4"]][a2]