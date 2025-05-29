import random
random_number = random.randint(1,100)
#print(random_number)
game_count = 0;
while True :
    try : 
        my_num = int(input("1~100사이 정수를 입력하세요 : "))
        #print(my_num)
        if my_num < 1 or my_num > 100 :
            print("1과 100사이의 숫자만 입력해주세요.")
            continue

        if my_num > random_number :
            print("down")
        elif my_num < random_number :
            print("up")
        elif my_num == random_number :
            print(f"딩동댕.{game_count}번만에 맞췄습니다.")
            break
        game_count+=1
    except Exception as e :
        print("정수만 입력가능합니다.")
        print(e)
