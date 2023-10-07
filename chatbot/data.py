`python
import pandas as pd

def load_data():

data = pd.read_csv('data.csv')

# Cleaning data

data.dropna(inplace=True)

# Split data

train = data.sample(frac=0.8)
valid = data.drop(train.index)

train_x = list(train['question'])
train_y = list(train['answer'])

valid_x = list(valid['question'])
valid_y = list(valid['answer'])

return {
'train': (train_x, train_y),
'valid': (valid_x, valid_y)
}