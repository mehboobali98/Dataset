import pandas as pd

# merge two lists into a dataframe
'''
input: 
	l1: list1
	l2: list2
	c1_label: label1
	c2_label: label2
'''
def merge_lists_df(l1, l2, c1_label, c2_label):
	if len(l1) != len(l2):
		print("Lists must be of equal size.")
		return
	else:
		list_of_tuples = list(zip(l1, l2))  
		df = pd.DataFrame(list_of_tuples, columns = [c1_label, c2_label])
		return df