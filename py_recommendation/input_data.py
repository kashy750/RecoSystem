from py_recommendation.error import RecoError
from py_recommendation.data import ItemData, UserData
from py_recommendation.utils import Utils

import pandas as pd

class InputData(object):
	"""docstring for InputData"""
	def __init__(self, arg):
		pass

	def getData_csv(self, filePath, itemName_col, itemDesc_col="", itemTag_col="", itemTag_sep = ","):
		df = pd.read_csv(filePath)
		req_col = [itemName_col]
		if itemDesc_col:
			req_col.append(itemDesc_col)
		if itemTag_col:
			req_col.append(itemTag_col)
		df = df[req_col]

		print(df)

	def getData_csv(self, filePath, itemName_col, itemDesc_col="", itemTag_col="", itemTag_sep = ","):
		df = pd.read_excel(filePath)
		print(df)
		req_col = [itemName_col]
		if itemDesc_col:
			req_col.append(itemDesc_col)
		if itemTag_col:
			req_col.append(itemTag_col)
		df = df[req_col]

		print(df)

