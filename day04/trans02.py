#구글에서 만든 라이브러리 있음  비동기 동작
import googletrans
import inspect
import asyncio
print(inspect.iscoroutinefunction(googletrans.Translator().translate))  

async def main() :
    translator = googletrans.Translator()

    #파일 같은거 열때 작업이 끝나면 지가 알아서 닫아준다.
    with open("day04/sing.txt","r",encoding="utf-8") as f :
       lines = [line.strip() for line in f if line.strip()] #리스트로 만들고
    
    task = [translator.translate(line,dest="zh-cn") for line in lines]
    result = await asyncio.gather(*task)

    with open("day04/translate_zh.txt","w",encoding="utf-8") as f :
        for original, translated in zip(lines,result) :
            f.write(f"{translated.text}\n")
asyncio.run(main())

#만약 print(inspect.iscoroutinefunction(googletrans.Translator().translate))   false라면 비동기 지원 안함...
#아래쪽 코드 실행
# import googletrans
# import inspect
# import asyncio
# print(inspect.iscoroutinefunction(googletrans.Translator().translate))  
# #만약 false이면 위에꺼 지우고 아래쪽 걸로 실행

# def main() :
#     translator = googletrans.Translator()

#     #파일 같은거 열때 작업이 끝나면 지가 알아서 닫아준다.
#     with open("day04/sing.txt","r",encoding="utf-8") as f :
#        lines = [line.strip() for line in f if line.strip()] #리스트로 만들고
    
#     #task = [translator.translate(line,dest="zh-cn") for line in lines]
#     result = [translator.translate(line,dest="zh-cn") for line in lines]

#     with open("day04/translate_zh.txt","w",encoding="utf-8") as f :
#         for original, translated in zip(lines,result) :
#             f.write(f"{translated.text}\n")
# main()