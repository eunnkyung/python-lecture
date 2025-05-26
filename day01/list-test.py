fruits = ["딸기","바나나","참외"]
nums = [1,2,3,4,5]
fruitAndNum = ["딸기",1,"바나나",2,True]
print(nums[0])
print(fruits[0])
print(fruitAndNum[4])
fruits.append("수박")
fruits.append("수박")
fruits.append("수박")
fruits.append("수박")
print(fruits)
fruits.insert(0,"샤인머스켓")
print(fruits)
fruits.remove("딸기")
print(fruits)
print(fruits.count("수박"))
print(fruits[:2])
print(fruits[2:])
print(fruits)
print(fruits[1:3]) #인덱스 1부터 즉 두번째 요소부터 인덱스3 이전 까지 출력
print(sum(nums))
print(len(nums))
print(sum(nums)/len(nums)) #숫자에만 쓴다.
total = 0;
for num in nums:
    total+=num
print("total==",total)
num_tuple =(1,2,3,4,5)  # tutple 은 불변 객체 immutable   list는 가변 객체 mutable
#num_tuple[0] = 5

num_matrix = [
    [1,2],
    [3,4],
    [5,6],
]
print(num_matrix)
print(num_matrix[0][1])

#dictionary
#{key:value}
dic01 = {1:"a",2:"b","c":3}   #js에선 json이라 불리는 걸 dictionary
print(dic01[1])
print(dic01[2])
print(dic01["c"])
dic01["apple"]="사과"
print(dic01)
num_set = set([1,1,1,2,3,3,2,2,4,4,4,4])
print(num_set)
str_set = set("apple") #처음 한번만...
print(str_set)

#num_set에 요소 추가
num_set.add(5)
str_set.add("banana")
print(num_set)
print(str_set)
num_set.remove(1)  #없으면 오류
print(num_set)
num_set.discard(1)  #없어도 오류 안남
print(num_set)
words = ["love","car","house","love"]
word_set = set(words)
print(word_set)
word_set02 = set("".join(words))
print(word_set02)
