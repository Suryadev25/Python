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
# dict = [{'k1': 11, 'k2': 22, 'k3': 33}, {
#     'e1': 1, 'e2': 2, 'e3': 3}, {'f1': 1, 'f2': 2, 'f3': 3}]
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


# count = 5
# while(count > 0):
#     print('count is greater than 0')
#     count -= 1


# for i in range(1, 8, 2):
#     print(i)
# l = []
# for i in range(1, 10, 2):
#     l.append(i)
# print(l)


# letter = 'hello'
# for i in enumerate(letter):
#     print(i)


# l1 = [1, 2, 3]
# l2 = ['a', 'b', 'c', 'd']
# for i in zip(l2, l1):
#     print(i)


# print('x' in ['x','t'])
# print(0 in [1,2,3,4])


# x = ('apple', 'banana', 'orange')
# x = '#'.join(x)
# print(x)


# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# z = sum(x)
# print(z)
# z = sum(x, 14)
# print(z)


# l1 = [1, 2, 3, 4]
# l2 = [5, 6, 7, 8]
# result = [sum(i) for i in zip(l1, l2)]
# print(result)


# def add(x):
#     return x+x
# l = [1, 2, 3, 4]
# result = map(add, l)
# print(list(result))
# l = [1, 2, 3, 4, 5]
# result = map(lambda x: x+x, l)
# print(list(result))
# l1 = [1, 2, 3, 4, 5]
# l2 = [6, 7, 8, 9, 10]
# result = map(lambda x, y: x+y, l1, l2)
# print(list(result))
# l = ['lodu', 'gandu', 'chodu']
# result = list(map(list, l))


# l = [2,2,3,4,5]
# print(max(list(l)))
# print(min(list(l)))


# import functools
# import operator
# l = [1, 2, 3, 4, 5]
# print(functools.reduce(lambda x, y: x+y, l))
# print(functools.reduce(lambda x, y: x*y, l))
# print(functools.reduce(operator.add, l))
# print(functools.reduce(operator.mul, l))


# import itertools
# import operator
# l = [1, 2, 3, 4, 5]
# print(list(itertools.accumulate(l, lambda x, y: x+y)))
# print(list(itertools.accumulate(l, lambda x, y: x*y)))
# print(list(itertools.accumulate(l, operator.add)))
# print(list(itertools.accumulate(l, operator.mul)))


# l = 'hello'
# l = [x for x in l]
# print(l)
# l = [x for x in 'word']
# print(l)
# l = [x**2 for x in range(1, 6)]
# print(l)
# celcius = [0, 10, 20]
# farenheit = [(x * 9/5)+32 for x in celcius]
# print(farenheit)


# s = 'Print the words which start with s in this sentence'
# l = []
# for i in s.split():
#     if(i[0].capitalize() == 'S'):
#         l.append(i)
# print(l)


# def add(a, b):
#     return a+b
# print(add(2, 3))
# def check_even(a):
#     for i in a:
#         if(i % 2 == 0):
#             return True
#         pass
#     return False
# print(check_even([1,3,5]))

    # def wordplay(s):
    #     s.split()

    #     for i in range(0,len(l)):
    #         if(i[0] == i+1[0]):
    #             pass
    #         return False
        # return True
s = 'My Name is Khan'
