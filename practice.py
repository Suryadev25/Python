# s = 'HEllO'
# print(s[::-1])

# s = 'YNEOS'
# n = int(input("Enter 1 or 0\n"))
# print(s[n::2])

# a = 'Sir'
# b = 'Surya'
# print(a+" "+b)

# a = 'a'
# b = 'b'
# c = 'c'
# print(a*4+" "+b*3+" "+c*2)

# x = '1'
# y = int(x)
# print(y)
# print(type(y))

# x = 'hello world'
# print(x.split())

# l = []
# for i in x:
#     if(i == ' '):
#         continue
#     l.append(i)
# print(l)

# s = 8
# ss = 'Bye'
# print("She firs said {} and then just walked away with {} " .format(s, ss))
# print(f'She first said {s} and the just walked away with {ss}')

# f = 103.2345
# print('the float fomatting is done like this {x:1.2f}'.format(x=f))

# lst = []
# for i in range(0, 10):
#      x = int(input())
#      lst.append(x)
# lst.sort()
# print(lst)

# d = {1: 'hello', 2: 'bye'}
# print(d)
# d[3] = 'uff'
# print(d)
# print(d.items())
# print(d.keys())
# print(d.values())
# x = dict(word='sixtynine', word2='nintysix')
# print(x)

# t = ('a',2,'a')
# print(t)
# print(t.count(2))
# print(t.index('a'))

# l = []
# for i in range(0,10):
#     x = int(input())
#     l.append(x)
# print(set(l))
# print(len(set(l)))

# print(1>2)
# print(2>1)

# print(1>2 or 1<2)
# print(not(1>2 or 1<2))
# print(1>2 and 1<2)
# print(not(1>2 and 1<2))

# x = int(input())
# if(x>10):
#     print('x is greater than 10')
# elif(x==10):
#     print('x is equal to 10')
# else:
#     print('x is smaller than 10')

# s = 'hello World'
# l = ''
# for i in s:
#     l+=i
# print(l)
# l = 0
# for i in range(0,10):
#     l+=i
# print(l)
# tuple = [(1,2),(3,4),(5,6),(7,8),(9,10)]
# for i in tuple:
#     print(i)
# tuple = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
# for i, j in tuple:
#     print(i)
# for i, j in tuple:
#     print(j)
dict = [{'k1': 11, 'k2': 22, 'k3': 33}, {
    'e1': 1, 'e2': 2, 'e3': 3}, {'f1': 1, 'f2': 2, 'f3': 3}]
# for i in dict:
# print(i)
# for i in dict:
#     for j in i:
#         print(j)
#         print(i[j])
# tup = ()
# lst = []
# for i in dict:
    # tup = tuple(x for x in i)
    # print(tup)
#     tup += tuple(x for x in i)
#     lst.append(tup)
#     tup = ()
# ref = tuple(lst)
# print(ref)
