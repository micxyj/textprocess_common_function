import pandas as pd
from pandas import DataFrame, Series
import numpy as np
from collections import deque

def tocols(file_name, col_number, default_value):
	file_df = pd.read_csv(file_name, sep='\t', header=None)
	deque_list = deque(default_value)
	if col_number <= len(file_df.columns):
		for j in range(col_number):
			for i in range(len(file_df.index)):
				if file_df.loc[i][j] is np.nan:
					file_df.loc[i][j] = deque_list.popleft()
		for column in file_df.loc[:, :(col_number - 1)].columns:
			yield list(file_df[column])
	else:
		for j in range(len(file_df.columns)):
			for i in range(len(file_df.index)):
				if file_df.loc[i][j] is np.nan:
					file_df.loc[i][j] = deque_list.popleft()
		while (len(file_df.columns) < col_number):
			file_df[file_df.columns[-1] + 1] = [ 
				deque_list.popleft() for i in file_df.index 
					]
		for column in file_df.columns:
			yield list(file_df[column])

for i in tocols('demo.txt', 3, [5, 6]):
	print (i)
print('\n')

for i in tocols('demo.txt', 5, [10, 6, 7]):
	print (i)
print('\n')

for i in tocols('demo.txt', 7, [5, 6, 7, 'f' ,2 ,3 ,4, 'g', 6, 7, 8]):
	print (i)







