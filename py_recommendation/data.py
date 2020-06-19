

class ItemData(object):
	"""docstring for ItemData"""
	def __init__(self, itemName, itemTags="", itemDesc=""):
		self.itemName = itemName
		self.itemTags = itemTags
		self.itemDesc = itemDesc


class UserData(object):
	"""docstring for UserData"""
	def __init__(self, userId, triedItemData):
		self.userId = userId
		self.triedItemData = triedItemData
		
		