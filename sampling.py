import pandas as pd
import numpy as np
import string
import math
from pandas import DataFrame, Series

def is_english_char(char):
	if ord(char) in range(97, 123) or ord(char) in range(65, 91):
		return True
	else:
		return False

def sampling(file_name, sample_length=None):
	with open(file_name, 'rt', encoding='utf-8') as file_object:
		data = file_object.read()
	punc = list(string.punctuation)
	punc.append(' ')
	punc.append('	')
	sample_list = list(data[:sample_length])
	sample_list = [ 
		char for char in sample_list if char not in punc 
			]
	actual_str = ''
	for element in sample_list:
		actual_str += element
	if data[:sample_length].isdigit():
		return "The sample are all number!"
	else:
		sen_of_numandeng = ''
		for char in sample_list:
			if (is_english_char(char) or char.isdigit()):
				sen_of_numandeng += char
		sample_list = [ 
			char for char in sample_list if (not is_english_char(char)) and (not char.isdigit())
				]
		actual_length = len(sample_list) + int(math.sqrt(len(sen_of_numandeng)))
		return [actual_str, actual_length]

sample_list = sampling('sampling_data.txt', 40)
print(sample_list)







