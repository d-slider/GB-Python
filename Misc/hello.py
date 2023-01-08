# digits=[1,2,3,5,8,15,23,38]
# list = [(i, i*i) for i in digits if i %2 == 0]
# print (list)


del_st = lambda x, y: " ".join([i for i in x.split() if y not in i])

print(del_st('абвгд гдежз жзе абв ыопыпт', 'абв'))