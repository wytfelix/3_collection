hello = ['h','e','l','l','o',]

digit = [6,8,2,4,1]
digit.sort()
print("Sorting digit : ", digit)
digit.reverse()
print("Reverse digit : ", digit)

hello1 = []
hello = hello.copy()
print("Copy hello1 : ",hello)
print("index hello : ", hello.index('o'))
print('count hello : ', hello.count('l'))

digit1 = [11,12]
digit2 = [13,14]
digit.extend(digit1)
digit.extend(digit2)
print("extend digit : ",digit)

digit.insert(1,[15,16])
digit.insert(1,(15,16))
print("insert digit : ",digit)