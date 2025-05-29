#import random
#print(random.randint(1,100))
#random클래스의 메서드로 접근

#import random as myRandom
#print(myRandom.randint(1,100))

#from random import randint
#print(randint(1,10))

#from random import randint, random
#print(randint(1,10))
#print(random())
#random의 함수 호출


import random
print(random.random())
print(random.randint(1,46))
print(random.uniform(1.0,5.0))
print(random.choice(["apple","berry","peach"]))
print(random.choices([1,2,3,4,5,6,7,8,9,10],k=5))  #k=지정 변수명 바꿀 수 없다.

makeLotto
numbers = random.sample(range(1,46),6)
numbers.sort()
print(numbers)

