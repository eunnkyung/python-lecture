num01=10;
num02=20;
if num01 == num02 :
    print("num01과 num02의 값은 같지 않습니다.")

if num01 != num02 : 
    print("num01과 num02의 값은 같지 않습니다.")


if num01 > num02 : 
    print("num01은 num02보다 큽니다.")
elif num01<num02 : 
    print("num02은 num01보다 큽니다.")
else : 
    print("num02은 num01은 같습니다")

str01 = "hello python"
if str01 == "hello python" : 
    print("hello python 문자열이 같습니다.")
if str01 == "hi python" : 
    print("hello python 문자열이 같습니다.")
if "hello" in str01 : 
    print("hello는 포함되어 있습니다.")

if "hello" not in str01 : 
    print("hello는 포함되어 있지 않습니다.")

while True : 
    user_input  =  input("정수를 입력하세요 q를 누르면 종료합니다.")
    if user_input == 'q' :
        print("프로그램을 종료합니다.")
        break

    num  =  int(user_input)
    if num > 0 : 
        print("양수")
    elif num < 0 :
        print("음수")
    else :    
        print("0입니다.")

