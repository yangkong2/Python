
# test_list = ['one', 'two', 'three']
# for i in test_list:
#     print(i)

# for i in range(10):  
#     print(i)

# result = 0
# for i in range(1, 101):  
#     result = result + a
#print(result)

# result = 0
# for i in range(1, 101):  
    
#     result = result + a
#     print(f"(a)sum = (result)")
# print(result)

# result = 0
# for a in range(1, 101):  
#     result = result + a
#     print(f'(a): sum = (result)') 
#     if result > 100:
        
#         break
        
# print(result)

# index = 0
# s = "BlockDMask"
# for a in s:
#     print(a,end=' ')
#     if a == 'k':
#         break
#     index = index + 1
    
# print(index)

# student = [180, 170, 164, 199, 182, 172, 177]
# for a in student:
#     in a > 170:
# #     continue #키가 170보다 크면
# # print(a)

# # result = 0
# # for a in range(1, 101):
# #     if a %2 == 1: # 2로 나누었을 때 나머지가 1
# #         result = result + a
# # print(result)

# # l = ['Alice', 'Bob','Charlie']

# # for name in l:
# #     if name == 'Bob':
# #         print('!!BREAK!!')
# #         break
# #     print(name)
# # else:
# #     print('!!FINISH!!')

# sr = ['father', 'mother', 'brother']
# cnt = 0
# for s in sr:
#     print (s)
#     for c in s:
#         pirnt(c, end=' ')
#         if c == 'r':
#             print(' ')
#             cnt+= 1
# print(cnt)

# a = []

# for i in range(10):
#     a.append(0) #append로 요소 추가
    
# print(a)

# a = []

# for i in range(3):
#     line = [] #안쪽 리스트로 사용할 빈 리스트 생성
#     for j in range(2):
#         line.append(j+i) #안쪽 리스트에 0 추가
#     a.append(line) #전체 리스트에 안쪽 리스트를 추가
    
# print(a)

# l = ['Alice', 'Bob','Charlie']

# for name in l:
#     print(name)
    
# for i, name in enumerate(l):
#      print(i, name)

# for i in range(10, 0, -3):
#     print(i)


# a = 'I Love Python'
# print (len(a)) #공백 포함

# b = 'abcd'
# print (len(b)) #공백 포함


# a=[1, 2, 3]
# print(min(a))

# b='bBlockDMask'
# print(min(b))


# d = (6, 5, 4, 2)
# print (min(d))

# a=[1, 2, 3]
# print(max(a))


# b='bBlockDMask'
# print(max(b))


# d = (6, 5, 4, 2)
# print (max(d))


# a=[1, 2, 3]
# b=[1, 2, 4]
# print(min(a, b)
# #result
# [1, 2, 3]

# c = 'BlockDMask'
# d = 'BAAAlockDMask'
# print(min(c, d))
# #result
# BAAAlockDMask

# g = [2, 3,4]
# h = [2, 2, 2, 2, 2]
# i = [9, 8, 7, 6, 5]
# j = [1]
# k = [0]
# print(min(g, h, i, j, k))

# myString = "everdevel"
# print(myString.count('e'))
# #4

# #문자열 'BlockDMask'선언
# a = 'BlockDMask'
# #문자열에서 'k'가 몇 개 있는지?
# print('#1 a.count("k")')
# print(a.count('k'))
# #문자열에서 'DM'가 몇 개 있는지?
# print('#2 a.count("DM")')
# print(a.count('DM'))
# #result
# #1 a.count("k")
# 2
# #2 a.count("DM")
# 1

# str="BlockDMask Blog.";
# print(f"str:{str}\n")

# #find 예제1
# print("1.str.find('찾을 문자')")
# result1 = str.find('a')
# print(result1)
# #결과
# 1.str.find('찾을 문자')
# 7 -> 0부터 세기 때문


# #문자가 있는 경우
# result2 = str.find('Z')

# #문자가 없는 경우
# print(f"str.find('a'): {result1}")
# print(f"str.find('Z'): {result2}")
# result3 = str.find('ask')
# print("str.find('ask'):(result3)")