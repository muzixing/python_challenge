import pickle
import marshal

list = [1, 2]
list.append(list)

print list

#byte1 = marshal.dumps(list)
byte2 = pickle.dumps(list)
print byte2
