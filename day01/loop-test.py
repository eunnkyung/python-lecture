print("0~9까지=======================")
for i in range(10) :
    print(i)
print("1~9까지=======================")
for i in range(1,10) :
    print(i)
print("10~1까지=======================")    
for i in range(10,0,-1) :
    print(i)

print("리스트 출력=======================")    
my_list = [1,2,3,4,5,"hello","python"]
for i in my_list :
    print(i)

#파이썬은 타입이 없다...
#range(1,11,2) 마지막 매개변수가 증감
for i in range(10,0,-1) :    
    print(i)

str01 = "hello_python"
for i in str01 :
    print(i)

a = 0;
while a < 10 :
    print(a)
    #a = a+1  a++ a-- ++a --a 없음 
    a+=1

b=0;
while True :
    print(b)
    b+=1
    if b>=10 :
        break

nums = [1,10,12,34,56]
for i in nums : 
    print(i)
names = ["유재석","정형돈","정준하","박명수"]    
for i, name in enumerate(names) : 
    print("i=",i,end=" ")
    print("name = ", name)

names = ["유재석","정형돈","정준하","박명수"]    
for i, name in enumerate(names,start=1) : 
    print("i = ",i,end=" / ")
    print("name = ", name)


#1부터 100까지 중 3의 배수만 출력

for i in range(3,101,3) :
    print(i)



#1부터 100까지 중 홀수만 출력
i=1;
while i<=100 :
    if i%2 == 1 :
        print(i)
    i+=1

#구구단 출력

for dan in range(2,10) :
    #print("====",dan,"단===")
    print(f"===={dan}단====")
    for i in range(1,10) :
        print(f"{dan} x {i} = {dan*i}")
print("====================================")
nums = [i for i in range(10)]
print(nums)

print("====================================")    
nums = [0 for i in range(10)]
print(nums)

def print_gugudan(n) :
    print(f"====={n}단=====")
    for i in range(1,10) :
        print(f"{n} x {i} = {n*i}")

print_gugudan(3)        
print_gugudan(32637)        