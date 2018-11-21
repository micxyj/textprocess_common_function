import pandas as pd
import numpy as np
from pandas import DataFrame, Series

def tsum(file_name, colnum, coltag):
	file_df = pd.read_csv(file_name, sep='\t', header=None)
	result_df = file_df.groupby(coltag)[colnum].sum()
	target_list = [ 
		[coltag, colnum] for coltag, colnum in zip(result_df.index, list(result_df))
			]
	return target_list

for item in tsum('tsum_data.txt', 1, 0):
	print(item)
print('\n')
for item in tsum('tsum_data.txt', 3, 2):
	print(item)