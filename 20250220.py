# a = '    test   !'
# b = '~~. test.~~ '
# c = '~test!'
# print(a.lstrip())
# print(b.lstrip('~'))
# print(c.lstrip('~!'))

# a = '    test   !   '
# b = ' ~~.test.~~'
# c = ' ~test!'
# print(a.rstrip(), end = '.')
# print(' ')
# print(b.rstrip('~'))
# print(c.rstrip('~!'))

# text = '000000water boils at 100 degrees 000'
# print(text.lstrip('0'))
# print(text.rstrip('0'))
# print(text.strip('0'))

# text = ',,,,,123.....water....pp'
# print(text.lstrip(',123.p'))
# print(text.rstrip(',123.p'))
# print(text.strip(',123.p'))

# a = '    test   !   '
# b = ' ~~.test.~~'
# c = ' ~test!'
# print(a.strip(), end = '.')
# print(' ')
# print(b.strip('~'))
# print(c.strip('~!'))

# test = 'Water boils at 100 degrees'
# print('['+test.rstrip()+']')
# print('['+test.lstrip()+']')
# print('['+test.strip()+']')

# txt = "  Hz  "
# x = txt.isspace()
# print(x)

# sentence = input("문자열을 입력하시오: ")
# table = {'알파벳': 0, "숫자": 0, "빈칸": 0}

# for i in sentence :
#     if (i.isalpha()):
#         table["알파벳"] += 1
#     elif (i.isdigit()): 
#           table["숫자"] += 1
#     elif (i.isdigit()): 
#           table["빈칸"] += 1
# print(table)

# s = '가나다라'
# n = 7

# answer = ''
# for i in range(n-len(s)): #문자열의 앞을 빈 문자열로 채우는 for 문문
#     answer += ' '

# answer += s

# print(answer)

# print(s.ljust(n))
# print(s.center(n))
# print(s.rjust(n))

# s = 'a b c d e f g'
# print(f's          : {s}')
# r = s.split()
# print(f's.split() : {r}')

# s = "aa.bb.cc.dd.ee.gg"
# print(f's                : {s}')

# r0 = s.split()
# r1 = s.split('.')
# r2 = s.split(sep='.')
# print(f"s.split()        : {r0}")
# print(f"s.split('.')     : {r1}")
# print(f"s.split(sep='.') : {r2}")

# s = "aa.bb.cc.BlockDMask.ee.ff.gg.python.example"
# print(f'{s}')

# r0 = s.split()
# r1 = s.split('.', 3)
# r2 = s.split(sep='.', maxsplit=3)
# r3 = s.split('.', maxsplit=3)
# print(f"\ns.split()\n{r0}")
# print(f"\ns.split('.', 3)\n{r1}")
# print(f"\ns.split(sep='.',maxplit=3)\n{r2}")
# print(f"\ns.split('.'), maxplit=3)\n{r3}")

# text = '123,456,789,999'

# replaceALL = text.replace(",","")
# replace_t1 = text.replace(",", "",1)
# replace_t2 = text.replace(",", "",2)
# replace_t3 = text.replace(",", "",3)
# print("결과: ")
# print(replaceALL)
# print(replace_t1)
# print(replace_t2)
# print(replace_t3)

# txt = "홈짱닷컴\nHomzzang.com"
# x = txt.splitlines()
# print(x)

# g = 'Milk/nChicken/r/nBread/rButter'
# print(g.splitlines())
# print(g.splitlines(True))
# g = 'Milk Chicken Bread Butter'
# print(g.splitlines())

# a = ['a', 'b', 'c', 'd', '1', '2', '3']
# print(a)
# print()
# #리스트를 문자열로 : join 이용
# result1 = "".join(a)
# print(result1)
# #리스트를 문자열로 : 하나하나 문자열을 더해서
# result2 = ''
# for v in a:
#     result2 += v
# print(result2)

# print("3".zfill(3))
# print("s".zfill(4))

# for x in range(3):
#     print(x)
#     print(str(x).zfill(4))

# str = '1234'
# str_zero = str.zfill(8)
# print(str_zero)

a = "abc"
print(a.rjust(10))
print(a.rjust(10,'#'))
b = "def"
print (b.ljust(15))
print (b.ljust(15, 'k'))