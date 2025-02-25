# f = open("newfile.txt", 'w')
# f.close()

# f = open("C:/Users/Dkdud/Desktop/python 기초 강의/newfile.txt", 'w')
# f.close()

# #w: 쓰기
# f = open('ex_memo.txt', 'w')
# students = ['김철수', '최영', '한석규', '김태희']
# for student in students:
#     msg = student
#     f.write(msg+"\n")
# f.close()

# file = open('hello.txt', 'w') #hello.txt 파일을 쓰기
# #모드 w로 열기. 파일 객체 변환
# file.write('Hello, world!')
# file.close()

# # a : 쓰기
# f = open('test.txt', 'a', encoding='UTF-8')

# for i in range (4, 10):
#     data = "%d 번째 줄 입니다. \n"%i
#     f.write(data)
# f.close

# dict1 = {'hello':1, 'brother':2}
# file1 = open("Original.txt", "w")

# str1 = repr(dict1)
# file1.write("dict1 = " + str1 + "\n")

# file1.close()

# test_file = open("test.txt", "w")

# a = 1
# b = 2
# test_file.write('%d + %d = %d' %(a, b, a+b))

# test_file.close

# from random import randint #난수 생성 랜덤 int를 가져옴옴

# with open('text3.txt', 'w') as f:
#     f.write('이번주 로또 번호는 ->')
#     for lotto in range(6):
#     f.write(str(randint(0, 50)))
# #f.close (with으로 할 경우 하지 않아도 됨)

# lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']

# with open('hello.txt' 'w') as file:
# #hello.txt 파일을 쓰기 모드(w)로 열기
#     file.writelines(lines)
# file.close()

# f = open("hz.txt", "a", encoding = 'UTF-8')
# f.writelines(["\n홈짱닷컴", "\nHomzzang.com"])
# f.close()

# #W: 쓰기
# f = open('ex_memo1.txt', 'w')
# students = ['김철수', '최영', '한석규', '김태희']
# for student in students:
#     msg = student
#     f.write(msg+"\n")
# f.close()

# f = open('ex_memo2.txt', 'w')
# students = ['김철수', '최영', '한석규', '김태희']
# f.writelines('\n'.join(students))
# f.close()

# #파일 r모드로 열기(파일을 따로 만들어야 됨)
# f = open('t2.txt', 'r')

# #read() 함수 이용해서 하나씩 읽어오기
# print('\n1. read()')
# print(f'위치 : {f.tell()}')

# s1 = f.read(1)
# print(s1)

# #readline() 함수 이용해서 한 라인씩 읽어오기
# print('\n2. realine()')
# print(f'위치 : {f.tell()}')

# s2 = f.readline()
# print(s2)

# #readlines() 함수 이용해서 모두 읽어오기기
# print('\n3. realines()')
# print(f'위치 : {f.tell()}')

# s3 = f.readlines()
# print(s3) 

#파일 r모드로 열기
f = open(r'text.txt')

#맨 처음 위치로 가서 한 줄 읽기
print('\n4. seek(0), readline()')

f.seek(0)
print(f'위치 : {f.tell()}')

s4 = f.readline()
print(s4)

#파일 닫기
f.close()