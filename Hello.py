'''
#world_name = 'Python.Study'
#print('Hello ' + world_name + ' World', 3)
#print(world_name.split('.'))
#world_name = input('update : ')
#print(world_name)
#my_list = []
#print(type(my_list))
#my_list = input('list : ')
#print(my_list) #list
#my_str = """CUSTOMER
#VENDOR
#AUTHORITY"""
#print(my_str)

#my_str = 'my name is %s' % 'jeongmok'
#print(my_str)
#my_number = '%d' % 1
#print(my_number)

#my_str = 'my name is {}' .format('jeongmok')
#print(my_str)
#my_number = '{0} * {2} = {1}' .format(2, 3, 2*3)
#print(my_number)

my_name = 'choi jeongmok'
#print(my_name[5]) #j +는 0부터
#print(my_name[-3]) #m -는 1부터
print(my_name[5:]) 
print(my_name[:4]) 

fruit = 'Choi Jeong Mok'
fruits = fruit.split()
print(fruits)


print('Choi jeong mok', end='!!!')
#escape codes : \n, \t

#list = []
#print(type(list))
#list = 'A', 'B', 'C', 'D', 'E', 'F'
list = ['A', 'B', 'C', 'D', 'E', 'F']
print(list)
print(list[2])
#print(type(list))
#listB = list
A, B, C, D, E, F = list
print(A)
#print(list)

list.append('G')
print(list)
del list[0]
print(list)
list[2] = 'Y'
list[4] = 'Z'
print(list)
list.sort()
print(list)
list.append('X')
list.append('X')
print(list)
print(list.count('X'))
print(len(list))

tuple = ()
print(type(tuple))
#tuple = [1, 2, 3, 4, 5]
tuple = 1, 2, 3, 4, 5
print(tuple)
print(type(tuple))

num1, num2, num3, num4, num5 = tuple
print(num2)
num2 = num4
print(num2)

str = '1 2 3 4 5'
print(str)
print(str[2]) #빈칸도 읽네
str2 = str.split()
print(str2[2])
'''
'''
EDI = ['Customter', 'Vendor', 'Authority']
for Module in EDI:
    print(Module)

for i in range(1, 10):
    for j in range(1, 10):
        print('{}x{}={}'.format(i, j, i*j))

#numbers = [1,2,3,4,5,6,7,8,9,10]
numbers = range(0, 10)
odd_numbers = []

for number in numbers:
    if number % 2 == 1:
        odd_numbers.append(number)
        #print(odd_numbers)
print(odd_numbers)

numbers = range(0, 10)
odd_numbers = [n for n in numbers if n % 2 == 1]
print(odd_numbers)

# 무작위로 입력된 숫자를 sorting하여 정렬하는 소스 

numbers = input("여러개의 숫자를 입력해주세요 (구분자는 ','를 사용하세요) : ")
random = []

for number in numbers:
    randoms.append(number)
    for random in randoms
    
    print(number)

#연산자
A = B : B를 A에 할당한다.
A += B : A = A + B
A -= B : A = A - B
A *= B : A = A * B
A /= B : A = A / B

** : 제곱
// : 버림

def cls():
    print('\n' * 100)
'''
'''
#내장함수
#모듈의 함수
#사용자 정의 함수

def 함수이름 (인자 1, ...):
    명령1
    명령2
    return 결과
def add(num1, num2):
    return num1 + num2, num1 * num2

print(add(1,2))
'''
# random 모듈
import random
#EDI = ['Customter', 'Vendor', 'Authority']
students = ['제열','상원','성현','인기','재운','정목','기택','영진','팀장','시몬']

#Choice 함수
#print(random.choice(EDI))

#Sample 함수
#print(random.sample(EDI, 2))
print(random.sample(student, 2))
#print(random.sample(range(1, 46), 6))

#randint 함수
#print(random.randint(8, 10))
