import numpy as np
import pandas as pd

data_folder = 'data/'
books_filename = 'BL-Flickr-Images-Book.csv'

df = pd.read_csv(data_folder + books_filename)
print(df.head())
print(df)


