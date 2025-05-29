#while True : 
#    try :
#        number = int( input("숫자를 입력하세요. : "))
#        print(f"입력한 숫자는 {number}입니다.")
#    except ValueError:
#        print("숫자만 입력 가능합니다.")



try :
    number01 = int( input("숫자를 입력하세요. : "))
    number02 = int( input("숫자를 입력하세요. : "))
    result = number01/number02
    print(f"결과는 {result}입니다.")
except ZeroDivisionError :
    print("0으로 나눌 수 없습니다.")    
except ValueError:
    print("숫자만 입력 가능합니다.")
finally :
    print("프로그램을 종료합니다.")
