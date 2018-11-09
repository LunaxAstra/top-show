import csv
import io
import sys

def jtrim(val):
	val = val.split('(')
	val = val[1].split(')')
	return val[0]

vals = []
keys = []
mixed = {}
notMixed = {}
for line in sys.stdin:
#	print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#	print("line is: " + str(type(line)))
	if line[0] == '"':
		f = io.StringIO(line)
		items = csv.reader(f, delimiter=',')
#		print("items is: " + str(type(items)))
		if not vals:
			for subItem in items:
#				print("subItem1 is: " + str(type(subItem)))
				for subItemItem in subItem:
#					print("subItemItem is: " + str(type(subItemItem)))
#					print(subItemItem)
					vals.append(subItemItem)
#				print("vals: " + str(vals))
#			print("num vals: " + str(len(vals)))
		elif not keys:
			for subItem in items:
				for subItemItem in subItem:
					try:
						f = float(subItemItem)
						keys.append(f)
					except ValueError:
						keys.append("FRED")
#				print("subItem2 is: " + str(type(subItem)))
#				print("keys: " + str(keys))
#			print("num keys: " + str(len(keys)))
		at = 0
		for key in keys:
			if isinstance(key, float):
				if not key in mixed:
#					print("EMPTY EMPTY EMPTY EMPTY EMPTY EMPTY EMPTY EMPTY EMPTY EMPTY ")
					f = vals[at]
					mixed[key] = [f]
				else:
					list = mixed[key]
#					print("list is: " + str(type(list)))
					f = vals[at]
					list.append(f)
#				mixed[key] = vals[at]
			else:
				if not key in mixed:
					notMixed[key] = [vals[at]]
				else:
					notMixed[key] = vals[at]
#			print("at=" + str(at))
			at = at + 1
#		print("mixed: " + str(mixed))
#		print("notMixed: " + str(notMixed))
#		for item in items:
#			print("###########################################################")
#			for subItem in item:
#				print(subItem)
#print("###########################################################")

keyList = []
for key in mixed:
	keyList.append(key)
keyList.sort()
keyList.reverse()
print("keyList: " + str(keyList))
item = 0
for key in keyList:
	print("==================================================================")
	print(key)
	for entry in mixed[key]:
		if item < 30:
			print(jtrim(entry))
		item = item + 1
