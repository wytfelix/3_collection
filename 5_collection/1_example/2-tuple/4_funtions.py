Tuple = [1,2,3,4,5,7]
print('len() = ',len(Tuple))
print('max() = ',max(Tuple))
print('min() = ',max(Tuple))
print('list(set) = ',tuple({1,2,3,4,5,6}))
print('list(tuple) = ',tuple({1,2,3,4,5,6}))
print('list(dict) = ',tuple({1: 'a',2: 'b',3: 'c'}))

#doesn't exist in python3
#tuple1, tuple2 = [1,'c'], [2, 'b']
#print(cmp(tuple))