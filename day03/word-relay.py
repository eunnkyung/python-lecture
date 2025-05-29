print("끝말잇기 시작")
prev_word = input("단어를 입력하세요.").strip()
used_words = set()
used_words.add(prev_word)

#set()을 이용해서 중복단어 허요 안되게끔
while True :
    next_word = input("단어를 입력하세요.").strip()
    if next_word == "끝" or  next_word == "end" :
        print("게임 종료")
        break

    if next_word in used_words :
        print("이미 사용한 단어입니다.")
        print("땡")
        continue

    if len(next_word) != 3 :
        print("3글자 단어만 쓸 수 있습니다.")
        print("땡")
        continue
    

    if prev_word[-1] == next_word[0] :
        print("딩동댕")
        used_words.add(next_word)
        prev_word = next_word
    else :
        print("땡")

#3글자 단어만...    