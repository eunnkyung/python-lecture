import random
def generate_lotto_num() :
    nums = random.sample(range(1,46),6)
    nums.sort()
    return nums

def generate_lotto_game(game_count) :
    for i in range(game_count) :
        print(f"{i+1}번째 로또번호 : {generate_lotto_num()}")

count = int(input("몇게임 하시겠습니까?"))
generate_lotto_game(count)
