# 무작위로 입력된 숫자를 sorting하여 정렬하는 소스 
number = input("여러개의 숫자를 입력해주세요 (구분자는 ','를 사용하세요) : ")
numbers = number.split(',')
numbers = list(map(int, numbers)) #형변환 필요함 *String Type일 경우 앞자리만 비교해서 안됨
new_numbers = []

# 정렬을 위한 소스
for i in range(len(numbers)-1):
    for j in range(len(numbers)-1):
        if (numbers[j] > numbers[j+1]):
            number = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = number
        #print(numbers)
    #print(numbers)

    if i not in new_numbers:
        new_numbers.append(i)

# 중복제거를 위한 소스
'''
for i in range(len(numbers)-1):
    if i not in new_numbers:
        new_numbers.append(i)
'''

print(new_numbers)