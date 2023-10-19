import numpy as np 
import pandas as pd 
from numpy import add

# read the csv file and convert it into pandas dataframe
df = pd.read_csv ('data.csv', encoding='latin1')

# using .to_json() method add a column in dataframe with csv converted to json format
# splitlines will split the json into multiple rows not a single one
df['json'] = df.to_json(orient='records', lines=True).splitlines()

# create a new dataframe with only json items
dfjson = df['json']

# print out the dataframe to a file
# Note that the timestamp forward slash will be escaped to stay true to JSON schema
np.savetxt(r'./output.txt', dfjson.values, fmt='%s')