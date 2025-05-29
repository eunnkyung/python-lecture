
def func() :
    print("hello")
    print("python")
func()    

def add(num01,num02) :  
    return num01+num02

result =  add(10,20)
print(result)

def addAndMultiple(num01,num02) :  
    result01 = num01+num02
    result02 = num01*num02
    return result01,result02
num02 = addAndMultiple(3,5)
print(num02)

def addAndMultiple(num01,num02) :  
    result01 = num01+num02
    result02 = num01*num02
    return result01,result02
_,num02 = addAndMultiple(3,5)
print(num02)

# 5!   5*4*3*2*1  재귀함수 (recursive)
def factorial(n) : 
    if n==0 :
        return 1
    else :
        return n*factorial(n-1)
print(factorial(12))


#구구단 몇다 ㄴ출력하기 함수로 정의해 보기