import pandas as pd
from pandas import DataFrame, Series
import numpy as np

def choose(file_name, keep_list=None, stop_list=None):
	file_df = pd.read_csv(file_name, sep='\t', header=None)
	if keep_list is not None:
		result = []
		for label in keep_list:
			label_df = file_df[file_df[1] == label]
			context_list = [
				[file_df.loc[index][0], file_df.loc[index][1]] for index in label_df.index
					]
			result += context_list
		return result
	elif keep_list is None:
		for label in file_df[1]:
			if label in stop_list:
				file_df = file_df[file_df[1] != label]
		result = [ 
			[file_df.loc[index][0], file_df.loc[index][1]] for index in file_df.index
				]
		return result

for result in choose('test_choose.txt', stop_list=['a', 'd']):
	print(result)
print('\n')
for result in choose('test_choose.txt', keep_list=['a', 'd']):
	print(result)
print('\n')
for result in choose('test_choose.txt', keep_list=['a', 'd'], stop_list=['c']):
	print(result)









